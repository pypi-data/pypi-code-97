# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EmailSubscriptionMetadata(Model):
    """Represents a email subscription for the instance.

    :param email_subscription: Possible values include: 'finishData'
    :type email_subscription: str or
     ~dynamics.customerinsights.api.models.enum
    :param email: Gets the email for the subscription.
    :type email: str
    :param status: Gets the current status for the subscription.
    :type status: str
    """

    _attribute_map = {
        'email_subscription': {'key': 'emailSubscription', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, email_subscription=None, email: str=None, status: str=None, **kwargs) -> None:
        super(EmailSubscriptionMetadata, self).__init__(**kwargs)
        self.email_subscription = email_subscription
        self.email = email
        self.status = status
