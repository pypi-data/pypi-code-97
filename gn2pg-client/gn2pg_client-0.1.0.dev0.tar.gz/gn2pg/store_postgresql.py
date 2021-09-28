#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Methods to store data to Postgresql database."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, NoReturn, Optional

import pkg_resources
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    create_engine,
    exc,
    func,
    select,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID, insert
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import and_

from . import _, __version__

# logger = logging.getLogger("transfer_gn.store_postgresql")
logger = logging.getLogger("transfer_gn.store_postgresql")


class StorePostgresqlException(Exception):
    """An exception occurred while handling download or store."""


class DataItem:
    """Properties of an observation, for writing to DB."""

    def __init__(
        self, source: str, metadata: MetaData, conn: Any, elem: dict
    ) -> NoReturn:
        """Item elements

        Args:
            source (str): GeoNature source name, for column storage
            metadata (str): SqlAlchemy metadata for data table.
            conn (str): SqlAlchemy connection to database
            elem (dict): Single observation to process and store.

        Returns:
            None
        """
        self._source = source
        self._metadata = metadata
        self._conn = conn
        self._elem = elem

    @property
    def source(self) -> str:
        """Return source name

        Returns:
            str: Source name
        """
        return self._source

    @property
    def metadata(self) -> MetaData:
        """Return SqlAlchemy metadata

        Returns:
            str: SqlAlchemy metadata
        """
        return self._metadata

    @property
    def conn(self) -> Any:
        """Return db connection

        Returns:
            str: db connection
        """
        return self._conn

    @property
    def elem(self) -> dict:
        """Return Single observation to process and store

        Returns:
            str: Observation
        """
        return self._elem


# def store_1_observation(item: DataItem) -> None:
#     """Process and store a single observation.

#     - find insert or update date
#     - store json in Postgresql

#     Args:
#         item (dict): ObservationItem, Observation item containing all parameters.

#     Returns:
#         None
#     """
#     # Insert simple observations,
#     # each row contains uniq_id, update timestamp and full json body
#     elem = item.elem
#     uniq_id = elem["ID_perm_SINP"]
#     logger.debug(
#         f"Storing observation {uniq_id} to database",
#     )
#     # Find last update timestamp
#     if "Date_modification" in elem:
#         update_date = elem["Date_modification"]
#     else:
#         update_date = elem["Date_creation"]

#     # Store in Postgresql
#     metadata = item.metadata
#     source = item.source
#     insert_stmt = insert(metadata).values(
#         uuid=uniq_id,
#         source=source,
#         update_ts=update_date,
#         item=elem,
#     )
#     do_update_stmt = insert_stmt.on_conflict_do_update(
#         constraint=metadata.primary_key,
#         set_=dict(update_ts=update_date, item=elem),
#         where=(metadata.c.update_ts < update_date),
#     )

#     item.conn.execute(do_update_stmt)
#     return None


class PostgresqlUtils:
    """Provides create and delete Postgresql database method."""

    def __init__(self, config) -> NoReturn:
        self._config = config
        self._db_url = {
            "drivername": "postgresql+psycopg2",
            "username": self._config.db_user,
            "password": self._config.db_password,
            "host": self._config.db_host,
            "port": self._config.db_port,
            "database": self._config.db_name,
        }
        if self._config.db_querystring:
            self._db_url["query"] = self._config.db_querystring

    # ----------------
    # Internal methods
    # ----------------

    def _create_table(self, name, *cols) -> NoReturn:
        """Check if table exists, and create it if not

        Parameters
        ----------
        name : str
            Table name.
        cols : list
            Data returned from API call.

        """
        # Store to database, if enabled
        if (
            self._config.db_schema_import + "." + name
        ) not in self._metadata.tables:
            logger.info("Table %s not found => Creating it", name)
            table = Table(name, self._metadata, *cols)
            table.create(self._db)
        else:
            logger.info("Table %s already exists => Keeping it", name)

    def _create_download_log(self) -> NoReturn:
        """Create download_log table if it does not exist."""
        self._create_table(
            "download_log",
            Column("source", String, nullable=False, index=True),
            Column("controler", String, nullable=False),
            Column(
                "download_ts",
                DateTime,
                server_default=func.now(),
                nullable=False,
            ),
            Column("error_count", Integer, index=True),
            Column("http_status", Integer, index=True),
            Column("comment", String),
        )

    def _create_increment_log(self) -> NoReturn:
        """Create increment_log table if it does not exist."""
        self._create_table(
            "increment_log",
            Column("source", String, nullable=False),
            Column("controler", String, nullable=False),
            Column(
                "last_ts", DateTime, server_default=func.now(), nullable=False
            ),
            PrimaryKeyConstraint(
                "source", "controler", name="increment_log_pk"
            ),
        )

    def _create_error_log(self) -> NoReturn:
        """Create error_log table if table does not exist."""
        self._create_table(
            "error_log",
            Column("source", String, nullable=False),
            Column("id_data", Integer, nullable=False, index=True),
            Column("controler", String, nullable=False),
            Column(
                "last_ts", DateTime, server_default=func.now(), nullable=False
            ),
            Column("item", JSONB),
            Column("error", String),
        )

    def _create_datasets_json(self) -> NoReturn:
        """Create entities_json table if it does not exist."""
        self._create_table(
            "datasets_json",
            Column("uuid", UUID, nullable=False),
            Column("source", String, nullable=False),
            Column("item", JSONB, nullable=False),
            PrimaryKeyConstraint("uuid", "source", name="meta_json_pk"),
        )

    def _create_data_json(self) -> NoReturn:
        """Create observations_json table if it does not exist."""
        self._create_table(
            "data_json",
            Column("source", String, nullable=False),
            Column("controler", String, nullable=False),
            Column("type", String, nullable=False),
            Column("id_data", Integer, nullable=False, index=True),
            Column("uuid", UUID, index=True),
            Column("item", JSONB, nullable=False),
            Column(
                "update_ts",
                DateTime,
                server_default=func.now(),
                nullable=False,
            ),
            PrimaryKeyConstraint(
                "id_data", "source", "type", name="pk_source_data"
            ),
        )

    def create_json_tables(self) -> NoReturn:
        """Create all internal and jsonb tables."""
        logger.info(
            f"Connecting to {self._config.db_name} database, to finalize creation"
        )
        self._db = create_engine(URL(**self._db_url), echo=False)
        conn = self._db.connect()
        # Create extensions
        try:
            ext_queries = (
                "CREATE EXTENSION IF NOT EXISTS pgcrypto;",
                'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";',
                "CREATE EXTENSION IF NOT EXISTS postgis;",
            )
            for q in ext_queries:
                logger.debug(f"Execute: {q}")
                conn.execute(q)
            logger.info("PostgreSQL extensions successfully created")
        except Exception as e:
            logger.critical(f"PostgreSQL extensions create failed : {e}")
        # Create import schema
        try:
            query = f"""
            CREATE SCHEMA IF NOT EXISTS {self._config.db_schema_import}
            AUTHORIZATION {self._config.db_user};
            """
            logger.debug(f"Execute: {query}")
            conn.execute(query)
            logger.info(
                (
                    f"Schema {self._config.db_schema_import} "
                    f"owned by {self._config.db_user} successfully created"
                )
            )
        except Exception as e:
            logger.critical(
                f"Failed to create {self._config.db_schema_import} schema"
            )
            logger.critical(f"{e}")

        # Set path to include VN import schema
        dbschema = self._config.db_schema_import
        self._metadata = MetaData(schema=dbschema)
        self._metadata.reflect(self._db)

        # Check if tables exist or else create them
        self._create_download_log()
        self._create_increment_log()
        self._create_error_log()
        self._create_datasets_json()
        self._create_data_json()

        conn.close()
        self._db.dispose()

    def count_json_data(self):
        """Count observations stored in json table, by source and type.

        Returns:
            dict: Count of observations by site and taxonomy.
        """

        result = None
        # Store to database, if enabled
        logger.info(_("Counting datas in database for all sources"))
        # Connect and set path to include VN import schema
        logger.info(_("Connecting to database %s"), self._config.db_name)
        self._db = create_engine(URL(**self._db_url), echo=False)
        conn = self._db.connect()
        dbschema = self._config.db_schema_import
        self._metadata = MetaData(schema=dbschema)
        # self._metadata.reflect(self._db)
        text = """
            SELECT source, COUNT(uuid)
                FROM {}.data_json
                GROUP BY source;
            """.format(
            dbschema
        )

        result = conn.execute(text).fetchall()

        return result

    def custom_script(self, script: str = "to_gnsynthese") -> NoReturn:
        """EXecute custom script on DB.
        eg.:  triggers to populate local tables like GeoNature synthese

        Args:
            script (str, optional): custom script path. Defaults to "to_gnsynthese".
        """
        logger.info(_(f"Start to execute {script} script"))
        self._db = create_engine(URL(**self._db_url), echo=False)
        conn = self._db.connect()
        dbschema = self._config.db_schema_import
        if script == "to_gnsynthese":
            file = pkg_resources.resource_filename(
                __name__, "data/to_gnsynthese.sql"
            )
            logger.info(
                _(
                    f"You choosed to use internal to_geonature.sql script in schema {self._config.db_schema_import}"
                )
            )
        else:
            if Path(script).is_file():
                logger.info(_(f"file {script} exists, continue"))
                file = Path(script)
            else:
                logger.critical(_(f"file {script} DO NOT EXISTS, exit"))
                exit
        with open(file) as filecontent:
            sqlscript = filecontent.read()
            sqlscript = sqlscript.replace(
                "gn2pg_import", self._config.db_schema_import
            )

        self._metadata = MetaData(schema=dbschema)
        # self._metadata.reflect(self._db)
        try:
            conn.execute(sqlscript)
            logger.info(_(f"script {script} successfully applied"))
        except Exception as e:
            logger.critical(f"{str(e)}")
            logger.critical(f"failed to apply script {script}")


class StorePostgresql:
    """Provides store to Postgresql database method."""

    def __init__(self, config):
        self._config = config
        self._db_url = {
            "drivername": "postgresql+psycopg2",
            "username": self._config.db_user,
            "password": self._config.db_password,
            "host": self._config.db_host,
            "port": self._config.db_port,
            "database": self._config.db_name,
        }
        if self._config.db_querystring:
            self._db_url["query"] = self._config.db_querystring

        dbschema = self._config.db_schema_import
        self._metadata = MetaData(schema=dbschema)
        logger.info(f"Connecting to database {self._config.db_name}")

        # Connect and set path to include VN import schema
        self._db = create_engine(URL(**self._db_url), echo=False)
        self._conn = self._db.connect()

        # Get dbtable definition
        self._metadata.reflect(bind=self._db, schema=dbschema)

        # Map Import tables in a single dict for easy reference
        self._table_defs = {
            "data": {"type": "data", "metadata": None},
            "meta": {"type": "metadata", "metadata": None},
        }

        self._table_defs["data"]["metadata"] = self._metadata.tables[
            dbschema + ".data_json"
        ]
        self._table_defs["meta"]["metadata"] = self._metadata.tables[
            dbschema + ".datasets_json"
        ]

        return None

    def __enter__(self):
        logger.debug("Entry into StorePostgresql")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Finalize connections."""
        logger.debug(
            "Closing database connection at exit from StorePostgresql"
        )
        self._conn.close()

    @property
    def version(self):
        """Return version."""
        return __version__

    # ----------------
    # Internal methods
    # ----------------
    def store_1_data(
        self,
        controler: str,
        elem: dict,
        id_key_name: str = "id_synthese",
        uuid_key_name: str = "id_perm_sinp",
    ) -> None:
        """Store 1 item in db (using upsert statement)

        Args:
            controler (str): Destionation table
            elem (dict): json data as dict
            id_key_name (str, optional): Data id in source database. Defaults to "id_synthese".
            uuid_key_name (str, optional): Universal unique identifier of the data. Defaults to "id_perm_sinp".
        """
        metadata = self._table_defs[controler]["metadata"]
        logger.debug(elem[id_key_name])
        try:
            insert_stmt = insert(metadata).values(
                id_data=elem[id_key_name],
                controler=controler,
                type=self._config.data_type,
                uuid=elem[uuid_key_name],
                source=self._config.std_name,
                item=elem,
                update_ts=datetime.now(),
            )
            do_update_stmt = insert_stmt.on_conflict_do_update(
                constraint=metadata.primary_key,
                set_=dict(item=elem, update_ts=datetime.now()),
            )
            self._conn.execute(do_update_stmt)
        except exc.StatementError as error:
            self.error_log(controler, elem, str(error))
            logger.critical(
                f"One error occured for data from source {self._config.std_name} whith "
                f"{id_key_name} = {elem[id_key_name]}"
            )

    def store_data(
        self,
        controler: str,
        items: list,
        id_key_name: str = "id_synthese",
        uuid_key_name: str = "id_perm_sinp",
    ) -> int:
        """Write items_dict to database.

        Args:
            controler (str): Name of API controler.
            items_dict (dict): Data returned from API call.
            id_key_name (str, optional): id key name from source. Defaults to "id_synthese".
            uuid_key_name (str, optional): uuid key name from source. Defaults to "id_perm_sinp".

        Returns:
            int: items dict length
        """
        # Loop on data array to store each element to database
        i = 0
        ne = 0
        for elem in items:
            try:
                i = i + 1
                # Convert to json
                self.store_1_data(controler, elem, id_key_name, uuid_key_name)

            except exc.StatementError as error:
                # assert isinstance(error.orig, ForeignKeyViolation)  # proves the original exception
                # raise StorePostgresqlException from error
                ne = ne + 1
                self.error_log(controler, elem, str(error))
                logger.critical(
                    f"One error occured for data from source {self._config.std_name} whith "
                    f"{id_key_name} = {elem[id_key_name]}"
                )
        logger.info(
            f"{i} items have been stored in db from {controler} of source {self._config.std_name} ({ne} error occured)"
        )
        return len(items)

    # ----------------
    # External methods
    # ----------------

    def delete_data(
        self,
        items: list,
        id_key_name: str = "id_synthese",
        controler: str = "data",
    ) -> int:
        """Delete observations stored in database.

        Args:
            items (list): items to delete
            id_key_name (str, optional): id key name from source. Defaults to "id_synthese".
            controler (str, optional): Name of API controler. Defaults to "data".

        Returns:
            int: Count of items deleted.
        """
        del_count = 0
        # Store to database, if enabled
        for item in items:
            logger.debug(
                f"Deleting item with id {item[id_key_name]} from source {self._config.name} (controler {controler})"
            )
            nd = self._conn.execute(
                self._table_defs["data"]["metadata"]
                .delete()
                .where(
                    and_(
                        self._table_defs["data"]["metadata"].c.id_data
                        == item[id_key_name],
                        self._table_defs["data"]["metadata"].c.controler
                        == controler,
                        self._table_defs["data"]["metadata"].c.source
                        == self._config.name,
                    )
                )
            )
            del_count += nd.rowcount

        return del_count

    def download_log(
        self,
        controler: str,
        error_count: int = 0,
        http_status: int = 0,
        comment: str = "",
    ):
        """Write download log entries to database.

        Args:
            source (str): GeoNature source name.
            controler (str): Name of API controler.
            error_count (int, optional): Number of errors during download. Defaults to 0.
            http_status (int, optional):  HTTP status of latest download. Defaults to 0.
            comment (str, optional): Optional comment, in free text.. Defaults to "".

        Returns:
            None
        """
        # Store to database, if enabled
        metadata = self._metadata.tables[
            self._config.db_schema_import + "." + "download_log"
        ]
        stmt = metadata.insert().values(
            source=self._config.std_name,
            controler=controler,
            error_count=error_count,
            http_status=http_status,
            comment=comment,
        )
        self._conn.execute(stmt)

        return None

    def increment_log(self, controler: str, last_ts: datetime) -> NoReturn:
        """Store last increment timestamp to database.

        Args:
            controler (str): controler name
            last_ts (datetime): last increment timestamp

        Returns:
            NoReturn: ...
        """
        # Store to database, if enabled
        metadata = self._metadata.tables[
            self._config.db_schema_import + "." + "increment_log"
        ]

        insert_stmt = insert(metadata).values(
            source=self._config.std_name, controler=controler, last_ts=last_ts
        )
        do_update_stmt = insert_stmt.on_conflict_do_update(
            constraint=metadata.primary_key, set_=dict(last_ts=last_ts)
        )
        self._conn.execute(do_update_stmt)

        return None

    def download_get(self, controler: str) -> Optional[str]:
        """Get last download timestamp from database.

        Args:
            controler (str): Controler name

        Returns:
            Optional[str]: Return last increment timestamp if exists
        """
        row = None
        metadata = self._metadata.tables[
            self._config.db_schema_import + "." + "download_log"
        ]
        stmt = (
            select([metadata.c.download_ts])
            .where(
                and_(
                    metadata.c.source == self._config.std_name,
                    metadata.c.controler == controler,
                )
            )
            .order_by(metadata.c.download_ts.desc())
        )
        result = self._conn.execute(stmt)
        row = result.fetchone()

        return row[0] if row is not None else None

    def increment_get(self, controler: str) -> Optional[str]:
        """Get last increment timestamp from database.

        Args:
            controler (str): Controler name

        Returns:
            Optional[str]: Return last increment timestamp if exists
        """
        row = None
        metadata = self._metadata.tables[
            self._config.db_schema_import + "." + "increment_log"
        ]
        stmt = select([metadata.c.last_ts]).where(
            and_(
                metadata.c.source == self._config.std_name,
                metadata.c.controler == controler,
            )
        )
        result = self._conn.execute(stmt)
        row = result.fetchone()

        return row[0] if row is not None else None

    def error_log(
        self,
        controler: str,
        item: dict,
        error: str,
        id_key_name: str = "id_synthese",
        last_ts: datetime = datetime.now(),
    ) -> None:
        """Store errors in database

        Args:
            controler (str): Controler name
            item (dict): [description]
            error (str): [description]
            id_key_name (str, optional): [description]. Defaults to "id_synthese".
            last_ts (datetime, optional): [description]. Defaults to datetime.now().

        Returns:
            [type]: [description]
        """

        metadata = self._metadata.tables[
            self._config.db_schema_import + "." + "error_log"
        ]
        insert_stmt = insert(metadata).values(
            source=self._config.std_name,
            controler=controler,
            id_data=item[id_key_name],
            item=item,
            last_ts=last_ts,
            error=error,
        )
        self._conn.execute(insert_stmt)

        return None
