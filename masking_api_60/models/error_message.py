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


class ErrorMessage(object):
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
        'error_message': 'str'
    }

    attribute_map = {
        'error_message': 'errorMessage'
    }

    def __init__(self, error_message=None):  # noqa: E501
        """ErrorMessage - a model defined in Swagger"""  # noqa: E501

        self._error_message = None
        self.discriminator = None

        self.error_message = error_message

    @property
    def error_message(self):
        """Gets the error_message of this ErrorMessage.  # noqa: E501

        The error message.  # noqa: E501

        :return: The error_message of this ErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ErrorMessage.

        The error message.  # noqa: E501

        :param error_message: The error_message of this ErrorMessage.  # noqa: E501
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501
        if error_message is not None and len(error_message) > 255:
            raise ValueError("Invalid value for `error_message`, length must be less than or equal to `255`")  # noqa: E501

        self._error_message = error_message

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
        if issubclass(ErrorMessage, dict):
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
        if not isinstance(other, ErrorMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other