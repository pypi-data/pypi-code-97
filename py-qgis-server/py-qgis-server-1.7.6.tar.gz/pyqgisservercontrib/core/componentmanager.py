#
# Copyright 2020 3liz
# Author David Marteau
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""" Components are a way to register objects using
    contract ids. A contract id is attached to an interface or a set 
    of interface.

    It is designed to have a general way about passing objects or behaviors to plugins
    or extension or other modules. It then enables for these modules or extensions to rely on the calling
    module behaviors without the need for these to do explicit imports
"""

import logging

from collections import namedtuple
from typing import Any, Callable

class ComponentManagerError(Exception):
    pass

class FactoryNotFoundError(ComponentManagerError):
    pass

class NoRegisteredFactoryError(ComponentManagerError):
    pass


LOGGER = logging.getLogger('SRVLOG')

FactoryEntry = namedtuple('FactoryEntry',('create_instance', 'service'))


class ComponentManager:

    def __init__(self) -> None:
        """ Component Manager
        """
        self._contractIDs = {}

    def register_entrypoints( self, category, *args, **kwargs ) -> None:
        """ Load extension modules 

            Loaded modules will do self-registration
        """
        from pkg_resources import iter_entry_points
        for ep in iter_entry_points(category):
            LOGGER.info("Loading module: %s:%s", category, ep.name)
            ep.load()(*args, **kwargs)

    def register_factory( self, contractID: str, factory: Callable[[],None] ) -> None:
        """ Register a factory for the given contract ID
        """
        if not callable(factory):
            raise ValueError('factory must be a callable object')

        LOGGER.debug("Registering factory: %s", contractID)
        self._contractIDs[contractID] = FactoryEntry(factory, None)

    def register_service( self, contractID: str, service: Any ) -> None:
        """ Register an instance object as singleton service
        """
        def nullFactory():
            raise NoRegisteredFactoryError(contractID)

        LOGGER.debug("Registering service: %s", contractID)
        self._contractIDs[contractID] = FactoryEntry( nullFactory , service )

    def create_instance( self, contractID: str ) -> Any:
        """ Create an instance of the object referenced by its
            contract id.
        """
        fe = self._contractIDs.get( contractID )
        if fe:
            return fe.create_instance()
        else:
            raise FactoryNotFoundError(contractID)

    def get_service( self, contractID: str ) -> Any:
        """ Return instance object as singleton
        """
        fe = self._contractIDs.get( contractID )
        if fe is None:
            raise FactoryNotFoundError(contractID)
        if fe.service is None:
            fe = fe._replace(service=fe.create_instance())
            self._contractIDs[contractID] = fe
        return fe.service


gComponentManager = ComponentManager()


def get_service( contractID: str ) -> Any:
    """ Alias to component_manager.get_service
    """
    return gComponentManager.get_service( contractID )


def create_instance( contractID: str ) -> Any:
    """ Alias to component_manager.create_instance
    """
    return gComponentManager.create_instance( contractID )


def register_entrypoints( category: str, *args, **kwargs ) -> None:
    """ Alias to component_manager.register_components
    """
    gComponentManager.register_entrypoints( category, *args, **kwargs )

#
# Declare factories or services with decorators
#

def register_service( contractID: str ) -> Any:
    def wrapper(obj: Any):
        gComponentManager.register_service(contractID, obj)
        return obj
    return wrapper


def register_factory( contractID: str ) -> Any:
    def wrapper(obj: Any):
        gComponentManager.register_factory(contractID, obj)
        return obj
    return wrapper


