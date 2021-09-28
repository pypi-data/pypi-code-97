# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bandwidth.api_helper import APIHelper


class ConferenceRecordingMetadata(object):

    """Implementation of the 'ConferenceRecordingMetadata' model.

    TODO: type model description here.

    Attributes:
        account_id (string): TODO: type description here.
        conference_id (string): TODO: type description here.
        name (string): TODO: type description here.
        recording_id (string): TODO: type description here.
        duration (string): Format is ISO-8601
        channels (int): TODO: type description here.
        start_time (datetime): TODO: type description here.
        end_time (datetime): TODO: type description here.
        file_format (FileFormatEnum): TODO: type description here.
        status (string): The current status of the recording. Current possible
            values are 'processing', 'partial', 'complete', 'deleted', and
            'error'. Additional states may be added in the future, so your
            application must be tolerant of unknown values.
        media_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "conference_id": 'conferenceId',
        "name": 'name',
        "recording_id": 'recordingId',
        "duration": 'duration',
        "channels": 'channels',
        "start_time": 'startTime',
        "end_time": 'endTime',
        "file_format": 'fileFormat',
        "status": 'status',
        "media_url": 'mediaUrl'
    }

    def __init__(self,
                 account_id=None,
                 conference_id=None,
                 name=None,
                 recording_id=None,
                 duration=None,
                 channels=None,
                 start_time=None,
                 end_time=None,
                 file_format=None,
                 status=None,
                 media_url=None):
        """Constructor for the ConferenceRecordingMetadata class"""

        # Initialize members of the class
        self.account_id = account_id
        self.conference_id = conference_id
        self.name = name
        self.recording_id = recording_id
        self.duration = duration
        self.channels = channels
        self.start_time = APIHelper.RFC3339DateTime(start_time) if start_time else None
        self.end_time = APIHelper.RFC3339DateTime(end_time) if end_time else None
        self.file_format = file_format
        self.status = status
        self.media_url = media_url

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
        account_id = dictionary.get('accountId')
        conference_id = dictionary.get('conferenceId')
        name = dictionary.get('name')
        recording_id = dictionary.get('recordingId')
        duration = dictionary.get('duration')
        channels = dictionary.get('channels')
        start_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("startTime")).datetime if dictionary.get("startTime") else None
        end_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("endTime")).datetime if dictionary.get("endTime") else None
        file_format = dictionary.get('fileFormat')
        status = dictionary.get('status')
        media_url = dictionary.get('mediaUrl')

        # Return an object of this model
        return cls(account_id,
                   conference_id,
                   name,
                   recording_id,
                   duration,
                   channels,
                   start_time,
                   end_time,
                   file_format,
                   status,
                   media_url)
