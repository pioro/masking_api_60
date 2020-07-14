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


class SsoReady(object):
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
        'is_sso_ready': 'bool'
    }

    attribute_map = {
        'is_sso_ready': 'isSsoReady'
    }

    def __init__(self, is_sso_ready=None):  # noqa: E501
        """SsoReady - a model defined in Swagger"""  # noqa: E501

        self._is_sso_ready = None
        self.discriminator = None

        self.is_sso_ready = is_sso_ready

    @property
    def is_sso_ready(self):
        """Gets the is_sso_ready of this SsoReady.  # noqa: E501

        Whether or not the Masking Engine is ready to have SSO enabled.  # noqa: E501

        :return: The is_sso_ready of this SsoReady.  # noqa: E501
        :rtype: bool
        """
        return self._is_sso_ready

    @is_sso_ready.setter
    def is_sso_ready(self, is_sso_ready):
        """Sets the is_sso_ready of this SsoReady.

        Whether or not the Masking Engine is ready to have SSO enabled.  # noqa: E501

        :param is_sso_ready: The is_sso_ready of this SsoReady.  # noqa: E501
        :type: bool
        """
        if is_sso_ready is None:
            raise ValueError("Invalid value for `is_sso_ready`, must not be `None`")  # noqa: E501

        self._is_sso_ready = is_sso_ready

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
        if issubclass(SsoReady, dict):
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
        if not isinstance(other, SsoReady):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
