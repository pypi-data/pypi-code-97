import asyncio
import inspect
import logging
from typing import Dict, List, Callable

from . import api
from .channel import public_channel_factory, PublicChannel
from .gateway import Gateway, Requestable
from .guild import Guild
from .interface import AsyncRunnable, MessageTypes
from .message import RawMessage, Event, PublicMessage, PrivateMessage
from .user import User

log = logging.getLogger(__name__)


class Client(Requestable, AsyncRunnable):
    """
    The bridge between khl.py internal components and khl server.

    Translates network package into khl.py concepts/object for internal to use.

    reminder: Client.loop only used to run handle_event() and registered handlers.
    """
    _handler_map: Dict[MessageTypes, List[Callable]]

    def __init__(self, gate: Gateway):
        self.gate = gate

        self._handler_map = {}
        self._pkg_queue = asyncio.Queue()

    def register(self, type: MessageTypes, handler: Callable):
        if not asyncio.iscoroutinefunction(handler):
            raise TypeError('handler must be a coroutine.')

        params = list(inspect.signature(handler).parameters.items())
        if len(params) != 1 or not issubclass(params[0][1].annotation, RawMessage):
            raise TypeError('handler must have one and only one param, and the param inherits RawMessage')

        if type not in self._handler_map:
            self._handler_map[type] = []
        self._handler_map[type].append(handler)

    async def handle_pkg(self):
        """
        Pop `pkg` from `event_queue`,
        spawn `msg` according to `pkg`,
        pass `msg` to corresponding handlers defined in `_handler_map`
        """
        while True:
            pkg: Dict = await self._pkg_queue.get()
            log.debug(f'upcoming pkg: {pkg}')

            msg: RawMessage
            if pkg['type'] == MessageTypes.SYS.value:
                msg = Event(**pkg)
            else:
                if pkg['channel_type'] == 'GROUP':
                    msg = PublicMessage(**pkg, _gate_=self.gate)
                elif pkg['channel_type'] == 'PERSON':
                    msg = PrivateMessage(**pkg, _gate_=self.gate)
                else:
                    log.error(f'can not spawn msg from pkg: {pkg}')
                    self._pkg_queue.task_done()
                    continue

            # dispatch msg
            if msg.type in self._handler_map and self._handler_map[msg.type]:
                for handler in self._handler_map[msg.type]:
                    asyncio.ensure_future(handler(msg), loop=self.loop)

            self._pkg_queue.task_done()

    async def create_asset(self, file: str) -> str:
        """upload ``file`` to khl, and return the url to the file"""
        return (await self.gate.exec_req(api.Asset.create(file=open(file, 'rb'))))['url']

    async def fetch_me(self) -> User:
        """fetch detail of the ``User`` on the client"""
        return User(_gate_=self.gate, _lazy_loaded_=True, **(await self.gate.exec_req(api.User.me())))

    async def fetch_public_channel(self, channel_id: str) -> PublicChannel:
        """fetch details of a public channel from khl"""
        channel_data = await self.gate.exec_req(api.Channel.view(channel_id))
        return public_channel_factory(_gate_=self.gate, **channel_data)

    async def list_guild(self) -> List[Guild]:
        """list guilds which the client joined"""
        guilds_data = (await self.gate.exec_pagination_req(api.Guild.list()))
        return [Guild(_gate_=self.gate, _lazy_loaded_=True, **i) for i in guilds_data]

    async def run(self):
        asyncio.ensure_future(self.handle_pkg(), loop=self.loop)
        await self.gate.run(self._pkg_queue)
