# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataRefreshSchedule(Model):
    """Represents a refresh schedule for the state machine.

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
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'timezone_id': {'key': 'timezoneId', 'type': 'str'},
        'cron_schedules': {'key': 'cronSchedules', 'type': '[str]'},
        'schedule_id': {'key': 'scheduleId', 'type': 'str'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
    }

    def __init__(self, *, is_active: bool=None, timezone_id: str=None, cron_schedules=None, schedule_id: str=None, instance_id: str=None, **kwargs) -> None:
        super(DataRefreshSchedule, self).__init__(**kwargs)
        self.is_active = is_active
        self.timezone_id = timezone_id
        self.cron_schedules = cron_schedules
        self.schedule_id = schedule_id
        self.instance_id = instance_id
