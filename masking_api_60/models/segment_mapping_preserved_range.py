# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SegmentMappingPreservedRange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'offset': 'int',
        'length': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'length': 'length'
    }

    def __init__(self, offset=None, length=None):  # noqa: E501
        """SegmentMappingPreservedRange - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._length = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if length is not None:
            self.length = length

    @property
    def offset(self):
        """Gets the offset of this SegmentMappingPreservedRange.  # noqa: E501

        The character offset of the range of input to preserve  # noqa: E501

        :return: The offset of this SegmentMappingPreservedRange.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SegmentMappingPreservedRange.

        The character offset of the range of input to preserve  # noqa: E501

        :param offset: The offset of this SegmentMappingPreservedRange.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def length(self):
        """Gets the length of this SegmentMappingPreservedRange.  # noqa: E501

        The character length of the range of input to preserve  # noqa: E501

        :return: The length of this SegmentMappingPreservedRange.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this SegmentMappingPreservedRange.

        The character length of the range of input to preserve  # noqa: E501

        :param length: The length of this SegmentMappingPreservedRange.  # noqa: E501
        :type: int
        """

        self._length = length

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SegmentMappingPreservedRange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SegmentMappingPreservedRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
