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


class BreakpointTimeout(object):
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
        'timeout': 'int'
    }

    attribute_map = {
        'timeout': 'timeout'
    }

    def __init__(self, timeout=None):  # noqa: E501
        """BreakpointTimeout - a model defined in Swagger"""  # noqa: E501

        self._timeout = None
        self.discriminator = None

        self.timeout = timeout

    @property
    def timeout(self):
        """Gets the timeout of this BreakpointTimeout.  # noqa: E501

        The time, in seconds, to wait for the task before timing out.  # noqa: E501

        :return: The timeout of this BreakpointTimeout.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this BreakpointTimeout.

        The time, in seconds, to wait for the task before timing out.  # noqa: E501

        :param timeout: The timeout of this BreakpointTimeout.  # noqa: E501
        :type: int
        """
        if timeout is None:
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501

        self._timeout = timeout

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
        if issubclass(BreakpointTimeout, dict):
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
        if not isinstance(other, BreakpointTimeout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
