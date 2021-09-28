#!/usr/bin/python
# -*- coding: ascii -*-
"""
Serialized object abstract implementation.

:date:      2021
:author:    Christian Wiche
:contact:   cwichel@gmail.com
:license:   The MIT License (MIT)
"""

from abc import ABC, abstractmethod
from typing import Optional


# -->> Definitions <<------------------


# -->> API <<--------------------------
class AbstractSerialized(ABC):
    """
    Serialized object abstraction.
    This class implements the expected interface for a serialized object.
    """
    def __repr__(self) -> str:
        """
        Representation string.
        """
        return f'{self.__class__.__name__}(serialized=0x{self.serialize().hex()})'

    def __eq__(self, other: object) -> bool:
        """
        Check if the object is equal to the input.
        """
        if isinstance(other, self.__class__):
            return self.serialize() == other.serialize()
        return False

    def __ne__(self, other: object):
        """
        Check if the object is different to the input.
        """
        return not self.__eq__(other)

    @abstractmethod
    def serialize(self) -> bytearray:
        """
        Serializes the item into a bytearray.

        :returns: Serialized object.
        :rtype: bytearray.
        """

    @classmethod
    @abstractmethod
    def deserialize(cls, data: bytearray) -> Optional['AbstractSerialized']:
        """
        Deserializes an object from a bytearray.

        :param bytearray data: Data to extract the object from.

        :returns: Deserialized object if available, None otherwise.
        :rtype: Optional['AbstractSerialized']
        """


class AbstractSerializedCodec(ABC):
    """
    Serialized object codec abstraction.
    This class implements the logic used to encode/decode a serialized object.
    """
    @abstractmethod
    def encode(self, data: AbstractSerialized) -> bytearray:
        """
        Encodes a serialized object into a byte array.

        :param AbstractSerialized data: Object to encode.

        :returns: Encoded serialized data.
        :rtype: bytearray
        """

    @abstractmethod
    def decode(self, data: bytearray) -> Optional[AbstractSerialized]:
        """
        Decodes a serialized object from a byte array.

        :param bytearray data: Bytes to decode.

        :returns: Deserialized object if able, None otherwise.
        :rtype: Optional[AbstractSerialized]
        """
