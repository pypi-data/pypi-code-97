# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bandwidth.api_helper import APIHelper
from bandwidth.voice.models.conference_member_state import ConferenceMemberState


class ConferenceState(object):

    """Implementation of the 'ConferenceState' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        name (string): TODO: type description here.
        created_time (datetime): TODO: type description here.
        completed_time (datetime): TODO: type description here.
        conference_event_url (string): TODO: type description here.
        conference_event_method (ConferenceEventMethodEnum): TODO: type
            description here.
        tag (string): TODO: type description here.
        active_members (list of ConferenceMemberState): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "created_time": 'createdTime',
        "completed_time": 'completedTime',
        "conference_event_url": 'conferenceEventUrl',
        "conference_event_method": 'conferenceEventMethod',
        "tag": 'tag',
        "active_members": 'activeMembers'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 created_time=None,
                 completed_time=None,
                 conference_event_url=None,
                 conference_event_method=None,
                 tag=None,
                 active_members=None):
        """Constructor for the ConferenceState class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.created_time = APIHelper.RFC3339DateTime(created_time) if created_time else None
        self.completed_time = APIHelper.RFC3339DateTime(completed_time) if completed_time else None
        self.conference_event_url = conference_event_url
        self.conference_event_method = conference_event_method
        self.tag = tag
        self.active_members = active_members

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
        id = dictionary.get('id')
        name = dictionary.get('name')
        created_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdTime")).datetime if dictionary.get("createdTime") else None
        completed_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("completedTime")).datetime if dictionary.get("completedTime") else None
        conference_event_url = dictionary.get('conferenceEventUrl')
        conference_event_method = dictionary.get('conferenceEventMethod')
        tag = dictionary.get('tag')
        active_members = None
        if dictionary.get('activeMembers') is not None:
            active_members = [ConferenceMemberState.from_dictionary(x) for x in dictionary.get('activeMembers')]

        # Return an object of this model
        return cls(id,
                   name,
                   created_time,
                   completed_time,
                   conference_event_url,
                   conference_event_method,
                   tag,
                   active_members)
