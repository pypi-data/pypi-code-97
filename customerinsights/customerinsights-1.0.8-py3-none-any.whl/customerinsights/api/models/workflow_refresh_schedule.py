# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WorkflowRefreshSchedule(Model):
    """Represents a DAG refresh schedule.

    :param operation_type: Possible values include: 'none', 'ingestion',
     'derivedEntity', 'hierarchy', 'dataPreparation', 'map',
     'realtimeM3Search', 'match', 'merge', 'profileStore', 'search',
     'activity', 'contact', 'attributeMeasures', 'entityMeasures', 'measures',
     'segmentation', 'segmentMembership', 'enrichment', 'preEnrichment',
     'transform', 'intelligence', 'aiBuilder', 'insights', 'export',
     'modelManagement', 'relationship', 'roleAssignment', 'analysis',
     'semanticEntity', 'all'
    :type operation_type: str or ~dynamics.customerinsights.api.models.enum
    :param sub_type: Possible values include: 'noSubType',
     'templatedMeasures', 'createAnalysisModel', 'linkAnalysisModel',
     'singleActivityMapping', 'powerPlatform'
    :type sub_type: str or ~dynamics.customerinsights.api.models.enum
    :param identifiers: Gets the identifiers of the schedule
    :type identifiers: list[str]
    :param job_type: Possible values include: 'full', 'incremental'
    :type job_type: str or ~dynamics.customerinsights.api.models.enum
    :param is_active: Gets a value indicating whether the schedule is active.
    :type is_active: bool
    :param timezone_id: Gets the ID of the timezone
    :type timezone_id: str
    :param cron_schedules: Gets the schedule in CRON format
    :type cron_schedules: list[str]
    :param schedule_id: Gets the ID of the schedule
    :type schedule_id: str
    :param instance_id: Customer Insights instance id associated with this
     object.
    :type instance_id: str
    """

    _attribute_map = {
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'sub_type': {'key': 'subType', 'type': 'str'},
        'identifiers': {'key': 'identifiers', 'type': '[str]'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'timezone_id': {'key': 'timezoneId', 'type': 'str'},
        'cron_schedules': {'key': 'cronSchedules', 'type': '[str]'},
        'schedule_id': {'key': 'scheduleId', 'type': 'str'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WorkflowRefreshSchedule, self).__init__(**kwargs)
        self.operation_type = kwargs.get('operation_type', None)
        self.sub_type = kwargs.get('sub_type', None)
        self.identifiers = kwargs.get('identifiers', None)
        self.job_type = kwargs.get('job_type', None)
        self.is_active = kwargs.get('is_active', None)
        self.timezone_id = kwargs.get('timezone_id', None)
        self.cron_schedules = kwargs.get('cron_schedules', None)
        self.schedule_id = kwargs.get('schedule_id', None)
        self.instance_id = kwargs.get('instance_id', None)
