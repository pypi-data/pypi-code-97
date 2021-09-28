# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TwoFactorCodeRequestSchema(object):

    """Implementation of the 'TwoFactorCodeRequestSchema' model.

    TODO: type model description here.

    Attributes:
        to (string): The phone number to send the 2fa code to.
        mfrom (string): The application phone number, the sender of the 2fa
            code.
        application_id (string): The application unique ID, obtained from
            Bandwidth.
        scope (string): An optional field to denote what scope or action the
            2fa code is addressing.  If not supplied, defaults to "2FA".
        message (string): The message format of the 2fa code.  There are three
            values that the system will replace "{CODE}", "{NAME}", "{SCOPE}".
            The "{SCOPE}" and "{NAME} value template are optional, while
            "{CODE}" must be supplied.  As the name would suggest, code will
            be replace with the actual 2fa code.  Name is replaced with the
            application name, configured during provisioning of 2fa.  The
            scope value is the same value sent during the call and partitioned
            by the server.
        digits (float): The number of digits for your 2fa code.  The valid
            number ranges from 2 to 8, inclusively.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "mfrom": 'from',
        "application_id": 'applicationId',
        "message": 'message',
        "digits": 'digits',
        "scope": 'scope'
    }

    def __init__(self,
                 to=None,
                 mfrom=None,
                 application_id=None,
                 message=None,
                 digits=None,
                 scope=None):
        """Constructor for the TwoFactorCodeRequestSchema class"""

        # Initialize members of the class
        self.to = to
        self.mfrom = mfrom
        self.application_id = application_id
        self.scope = scope
        self.message = message
        self.digits = digits

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        application_id = dictionary.get('applicationId')
        message = dictionary.get('message')
        digits = dictionary.get('digits')
        scope = dictionary.get('scope')

        # Return an object of this model
        return cls(to,
                   mfrom,
                   application_id,
                   message,
                   digits,
                   scope)
