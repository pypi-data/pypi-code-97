"""

This Is For Security Purpose Only
As Many Noobs Using Cheap Tricks To Hack userbot.
We here to save them

~ @TeamUltroid

"""

# Lol You Are So desperate.
# You came all here just to see this
# 😂😂😂😂

import os

_discared = ["API_ID","API_HASH","SESSION", "VC_SESSION", "REDIS_PASSWORD", "REDISPASSWORD", "HEROKU_API", "BOT_TOKEN"]

_get_sys = {}


# Class Var Clean up
def cleanup_cache(what_u_doing_here=None):
    #from pyUltroid import ultroid_bot
    #from telethon.sessions import StringSession
    from pyUltroid.configs import Var
    #ultroid_bot.session = StringSession(None)
    os_stuff()
    for z in _discared:
        if z in Var.__dict__.keys():
            _get_sys.update({z: Var.__dict__[z]})
            setattr(Var, z, "")


# Env clean up
def os_stuff():
    all = os.environ
    for z in all.keys():
        if z in _discared:
            all.update({z: ""})

# Getting them back for re-start & soft update
def call_back():
    from pyUltroid.configs import Var
    for z in _get_sys:
        if _get_sys[z]:
            setattr(Var, z, str(_get_sys[z]))
            os.environ[z] = str(_get_sys[z])
    

DANGER = [
    "SESSION",
    "BOT_TOKEN", 
    "VC_SESSION",
    "DANGER",
    "DeleteAccountRequest",
    "HEROKU_API",
    "base64",
    "bash",
    "call_back",
    "get_me()",
    "exec",
    "phone",
    "REDIS_PASSWORD",
    "load_addons",
    "load_other_plugins",
    "os.system",
    "subprocess",
    "await locals()",
    "aexec",
    ".session.save()",
    ".auth_key.key",
    "INSTA_USERNAME",
    "INSTA_PASSWORD",
    "INSTA_SET",
    "SUDOS", 
    "FULLSUDO",
    "DEVLIST."
]
