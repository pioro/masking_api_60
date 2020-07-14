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


class RecordType(object):
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
        'record_type_id': 'int',
        'record_type_name': 'str',
        'file_format_id': 'int'
    }

    attribute_map = {
        'record_type_id': 'recordTypeId',
        'record_type_name': 'recordTypeName',
        'file_format_id': 'fileFormatId'
    }

    def __init__(self, record_type_id=None, record_type_name=None, file_format_id=None):  # noqa: E501
        """RecordType - a model defined in Swagger"""  # noqa: E501

        self._record_type_id = None
        self._record_type_name = None
        self._file_format_id = None
        self.discriminator = None

        if record_type_id is not None:
            self.record_type_id = record_type_id
        if record_type_name is not None:
            self.record_type_name = record_type_name
        if file_format_id is not None:
            self.file_format_id = file_format_id

    @property
    def record_type_id(self):
        """Gets the record_type_id of this RecordType.  # noqa: E501

        The ID number of the record type. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The record_type_id of this RecordType.  # noqa: E501
        :rtype: int
        """
        return self._record_type_id

    @record_type_id.setter
    def record_type_id(self, record_type_id):
        """Sets the record_type_id of this RecordType.

        The ID number of the record type. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param record_type_id: The record_type_id of this RecordType.  # noqa: E501
        :type: int
        """

        self._record_type_id = record_type_id

    @property
    def record_type_name(self):
        """Gets the record_type_name of this RecordType.  # noqa: E501

        The name of the record type.  # noqa: E501

        :return: The record_type_name of this RecordType.  # noqa: E501
        :rtype: str
        """
        return self._record_type_name

    @record_type_name.setter
    def record_type_name(self, record_type_name):
        """Sets the record_type_name of this RecordType.

        The name of the record type.  # noqa: E501

        :param record_type_name: The record_type_name of this RecordType.  # noqa: E501
        :type: str
        """
        if record_type_name is not None and len(record_type_name) > 255:
            raise ValueError("Invalid value for `record_type_name`, length must be less than or equal to `255`")  # noqa: E501

        self._record_type_name = record_type_name

    @property
    def file_format_id(self):
        """Gets the file_format_id of this RecordType.  # noqa: E501

        The ID number of the file format that the record type refers to.  # noqa: E501

        :return: The file_format_id of this RecordType.  # noqa: E501
        :rtype: int
        """
        return self._file_format_id

    @file_format_id.setter
    def file_format_id(self, file_format_id):
        """Sets the file_format_id of this RecordType.

        The ID number of the file format that the record type refers to.  # noqa: E501

        :param file_format_id: The file_format_id of this RecordType.  # noqa: E501
        :type: int
        """

        self._file_format_id = file_format_id

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
        if issubclass(RecordType, dict):
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
        if not isinstance(other, RecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other