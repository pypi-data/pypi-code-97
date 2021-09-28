"""
The layer for initializing the database
"""

from ._db import get_db
from .base import BaseModel


def make_base(host, name, login=None, password=None):
    """ Declare the base class of the model """

    class Base(BaseModel):
        """ Base model with the initialized database """

        _db = get_db(host, name, login, password)

        @property
        def _name(self) -> str:
            """ Database name """

            return None

    return Base
