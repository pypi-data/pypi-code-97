from datetime import datetime
from typing import List, Optional
from uuid import UUID

import attr

from dbnd._core.tracking.schemas.base import ApiObjectSchema
from dbnd._core.utils.basics.nothing import NOTHING
from dbnd._vendor.marshmallow import fields, post_load


class GetRunningDagRunsResponseSchema(ApiObjectSchema):
    dag_run_ids = fields.List(fields.Integer())
    last_seen_dag_run_id = fields.Integer(allow_none=True)
    last_seen_log_id = fields.Integer(allow_none=True)


class UpdateLastSeenValuesRequestSchema(ApiObjectSchema):
    last_seen_dag_run_id = fields.Integer()
    last_seen_log_id = fields.Integer()


class UpdateAirflowMonitorStateRequestSchema(ApiObjectSchema):
    airflow_version = fields.String(required=False, allow_none=True)
    airflow_export_version = fields.String(required=False, allow_none=True)
    airflow_monitor_version = fields.String(required=False, allow_none=True)
    monitor_status = fields.String(required=False, allow_none=True)
    monitor_error_message = fields.String(required=False, allow_none=True)
    airflow_instance_uid = fields.UUID(required=False, allow_none=True)


class GetAllDagRunsRequestSchema(ApiObjectSchema):
    min_start_time = fields.DateTime(allow_none=True)
    dag_ids = fields.String(allow_none=True)


class TaskSchema(ApiObjectSchema):
    upstream_task_ids = fields.List(fields.String())
    downstream_task_ids = fields.List(fields.String())
    task_type = fields.String()
    task_source_code = fields.String(allow_none=True)
    task_source_hash = fields.String(allow_none=True)
    task_module_code = fields.String(allow_none=True)
    module_source_hash = fields.String(allow_none=True)
    dag_id = fields.String()
    task_id = fields.String()
    retries = fields.Integer()
    command = fields.String(allow_none=True)
    task_args = fields.Dict()


class DagSchema(ApiObjectSchema):
    description = fields.String()
    root_task_ids = fields.List(fields.String())
    tasks = fields.Nested(TaskSchema, many=True)
    owner = fields.String()
    dag_id = fields.String()
    schedule_interval = fields.String()
    catchup = fields.Boolean()
    start_date = fields.DateTime(allow_none=True)
    end_date = fields.DateTime(allow_none=True)
    is_committed = fields.Boolean()
    git_commit = fields.String()
    dag_folder = fields.String()
    hostname = fields.String()
    source_code = fields.String(allow_none=True)
    module_source_hash = fields.String(allow_none=True)
    is_subdag = fields.Boolean()
    tags = fields.List(fields.String(), allow_none=True)
    task_type = fields.String()
    task_args = fields.Dict()
    is_active = fields.Boolean(allow_none=True)
    is_paused = fields.Boolean(allow_none=True)


class DagRunSchema(ApiObjectSchema):
    dag_id = fields.String()
    run_id = fields.String(required=False)
    dagrun_id = fields.Integer()
    start_date = fields.DateTime(allow_none=True)
    state = fields.String()
    end_date = fields.DateTime(allow_none=True)
    execution_date = fields.DateTime()
    task_args = fields.Dict()


class TaskInstanceSchema(ApiObjectSchema):
    execution_date = fields.DateTime()
    dag_id = fields.String()
    state = fields.String(allow_none=True)
    try_number = fields.Integer()
    task_id = fields.String()
    start_date = fields.DateTime(allow_none=True)
    end_date = fields.DateTime(allow_none=True)
    log_body = fields.String(allow_none=True)
    xcom_dict = fields.Dict()


class MetricsSchema(ApiObjectSchema):
    performance = fields.Dict()
    sizes = fields.Dict()


class AirflowExportMetaSchema(ApiObjectSchema):
    airflow_version = fields.String()
    plugin_version = fields.String()
    request_args = fields.Dict()
    metrics = fields.Nested(MetricsSchema)


class InitDagRunsRequestSchema(ApiObjectSchema):
    dags = fields.Nested(DagSchema, many=True)
    dag_runs = fields.Nested(DagRunSchema, many=True)
    task_instances = fields.Nested(TaskInstanceSchema, many=True)

    airflow_export_meta = fields.Nested(AirflowExportMetaSchema, required=False)
    error_message = fields.String(required=False, allow_none=True)
    syncer_type = fields.String(allow_none=True)


class OkResponseSchema(ApiObjectSchema):
    ok = fields.Boolean()


class UpdateDagRunsRequestSchema(ApiObjectSchema):
    dag_runs = fields.Nested(DagRunSchema, many=True)
    task_instances = fields.Nested(TaskInstanceSchema, many=True)
    last_seen_log_id = fields.Integer(allow_none=True)

    airflow_export_meta = fields.Nested(AirflowExportMetaSchema, required=False)
    error_message = fields.String(required=False, allow_none=True)
    syncer_type = fields.String(allow_none=True)


# ----- Datasource Tracking ------

# Datasource Monitor
@attr.s
class DatasourceMonitorState(object):
    datasource_monitor_version = attr.ib(default=NOTHING)  # type: str
    monitor_status = attr.ib(default=NOTHING)  # type: str
    monitor_error_message = attr.ib(default=NOTHING)  # type: str
    monitor_start_time = attr.ib(default=NOTHING)  # type: datetime
    last_sync_time = attr.ib(default=NOTHING)  # type: datetime
    last_transaction_sync_time = attr.ib(default=NOTHING)  # type: datetime

    def as_dict(self):
        # don't serialize data which didn't changed: as_dict should be able to return
        # None value when it set, specifically for monitor_error_message - when not set
        # at all (=NOTHING, didn't changed, =None changed)
        return attr.asdict(self, filter=lambda field, value: value is not NOTHING)


class DatasourceMonitorStateSchema(ApiObjectSchema):
    datasource_monitor_version = fields.String(required=False, allow_none=True)
    monitor_status = fields.String(required=False, allow_none=True)
    monitor_error_message = fields.String(required=False, allow_none=True)
    monitor_start_time = fields.DateTime(required=False, allow_none=True)
    last_sync_time = fields.DateTime(required=False, allow_none=True)
    last_transaction_sync_time = fields.DateTime(required=False, allow_none=True)

    @post_load
    def make_object(self, data, **kwargs):
        return {"monitor_state": DatasourceMonitorState(**data)}


# Dataset Objects
@attr.s
class SyncedDatasetMetadata(object):
    num_bytes = attr.ib()  # type: int
    records = attr.ib()  # type: int
    schema = attr.ib()  # type: dict

    def as_dict(self):
        return attr.asdict(self)


@attr.s
class SyncedDataset(object):
    uri = attr.ib()  # type: str
    created_date = attr.ib()  # type: datetime
    last_modified_date = attr.ib()  # type: datetime
    metadata = attr.ib()  # type: SyncedDatasetMetadata

    def as_dict(self):
        return attr.asdict(self)


@attr.s
class DatasetsReport(object):
    sync_event_uid = attr.ib()  # type: UUID
    monitor_state = attr.ib()  # type: DatasourceMonitorState

    sync_event_timestamp = attr.ib()  # type: datetime
    datasets = attr.ib()  # type: SyncedDataset

    source_type = attr.ib(default=None)  # type: Optional[str]
    syncer_type = attr.ib(default=None)  # type: Optional[str]

    def as_dict(self):
        return attr.asdict(self, filter=lambda field, value: value is not NOTHING)


# Dataset schemas
class SyncedDatasetMetadataSchema(ApiObjectSchema):
    num_bytes = fields.Integer()
    records = fields.Integer()

    schema = fields.Dict()
    # TODO: ADD -> Preview

    @post_load
    def make_object(self, data, **kwargs):
        return SyncedDatasetMetadata(**data)


class SyncedDatasetSchema(ApiObjectSchema):
    uri = fields.String()  # {storage_type://region/project_id/scheme_name/table_name}
    created_date = fields.DateTime()
    last_modified_date = fields.DateTime(allow_none=True)

    metadata = fields.Nested(SyncedDatasetMetadataSchema)

    @post_load
    def make_object(self, data, **kwargs):
        return SyncedDataset(**data)


class DatasetsReportSchema(ApiObjectSchema):
    sync_event_uid = fields.UUID()
    monitor_state = fields.Nested(DatasourceMonitorStateSchema)
    source_type = fields.String(allow_none=True)  # bigquery / snowflake / etc
    syncer_type = fields.String(allow_none=True)

    sync_event_timestamp = fields.DateTime(required=False, allow_none=True)
    datasets = fields.Nested(SyncedDatasetSchema, many=True)

    @post_load
    def make_object(self, data, **kwargs):
        return {
            "datasets_report": DatasetsReport(**data),
        }


@attr.s
class SyncedTransactionOperation(object):
    op_type = attr.ib()  # type: str
    records_count = attr.ib()  # type: int
    started_date = attr.ib()  # type: datetime

    dataset_uri = attr.ib()  # type: str
    dataset_uid = attr.ib(default=None)  # type: UUID

    def as_dict(self, fields_to_ignore=None):
        fields_to_ignore = fields_to_ignore or []
        return attr.asdict(
            self, filter=lambda field, _: field.name not in fields_to_ignore
        )


@attr.s
class SyncedTransaction(object):
    datasource_transaction_id = attr.ib()  # type: str

    created_date = attr.ib()  # type: datetime
    started_date = attr.ib()  # type: datetime
    ended_date = attr.ib()  # type: datetime

    write_operation = attr.ib()  # type: Optional[SyncedTransactionOperation]
    read_operations = attr.ib()  # type: List[SyncedTransactionOperation]

    query_string = attr.ib()  # type: str

    def as_dict(self):
        return attr.asdict(self)


@attr.s
class SyncedTransactionsReport(object):
    sync_event_uid = attr.ib()  # type: UUID
    source_type = attr.ib()  # type: str
    syncer_type = attr.ib()  # type: str
    sync_event_timestamp = attr.ib()  # type: datetime

    monitor_state = attr.ib()  # type: DatasourceMonitorStateSchema
    transactions = attr.ib()  # type: List[SyncedTransaction]

    def as_dict(self):
        return attr.asdict(self, filter=lambda field, value: value is not NOTHING)


class SyncedTransactionOperationSchema(ApiObjectSchema):
    op_type = fields.String()
    started_date = fields.DateTime()  # type: datetime
    records_count = fields.Integer()

    dataset_uri = fields.String()
    dataset_uid = fields.UUID(allow_none=True)

    @post_load
    def make_object(self, data, **kwargs):
        return SyncedTransactionOperation(**data)


class SyncedTransactionSchema(ApiObjectSchema):
    datasource_transaction_id = fields.String()
    created_date = fields.DateTime()
    started_date = fields.DateTime()
    ended_date = fields.DateTime()

    write_operation = fields.Nested(SyncedTransactionOperationSchema)
    read_operations = fields.Nested(
        SyncedTransactionOperationSchema, many=True, allow_none=True
    )

    query_string = fields.String()

    @post_load
    def make_object(self, data, **kwargs):
        return SyncedTransaction(**data)


class SyncedTransactionsReportSchema(ApiObjectSchema):
    sync_event_uid = fields.UUID()
    sync_event_timestamp = fields.DateTime()
    source_type = fields.String(allow_none=True)  # bigquery / snowflake / etc
    syncer_type = fields.String(allow_none=True)

    monitor_state = fields.Nested(DatasourceMonitorStateSchema)
    transactions = fields.Nested(SyncedTransactionSchema, many=True)

    @post_load
    def make_object(self, data, **kwargs):
        return {
            "transactions_report": SyncedTransactionsReport(**data),
        }
