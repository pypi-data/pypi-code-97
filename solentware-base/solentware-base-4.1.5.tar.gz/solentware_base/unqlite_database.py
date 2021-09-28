# unqlite_database.py
# Copyright 2019 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Access an UnQLite database without deferring index updates.

The unqlite module provides the database interface.

Prefer to use the unqlitedu_database module when adding lots of new
records.  It will be a lot quicker because it defers index updates.

"""
import unqlite

from .core import _nosql


class Database(_nosql.Database):
    """Define Database class using unqlite module.

    Behaviour comes from the _nosql.Database class.

    The UnQLite engine comes from the unqlite module.
    """

    def open_database(self, **k):
        """Delegate to superclass with unqlite as database engine module.

        The first super().open_database() call in a run will raise a
        SegmentSizeError, if the actual segment size is not the size given in
        the FileSpec, after setting segment size to that found in database.
        Then the super().open_database() call in except path should succeed
        because segment size is now same as that on the database.
        """
        try:
            super().open_database(
                unqlite, unqlite.UnQLite, unqlite.UnQLiteError, **k
            )
        except self.__class__.SegmentSizeError:
            super().open_database(
                unqlite, unqlite.UnQLite, unqlite.UnQLiteError, **k
            )
