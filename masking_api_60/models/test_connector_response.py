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


class TestConnectorResponse(object):
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
        'response': 'str'
    }

    attribute_map = {
        'response': 'response'
    }

    def __init__(self, response=None):  # noqa: E501
        """TestConnectorResponse - a model defined in Swagger"""  # noqa: E501

        self._response = None
        self.discriminator = None

        if response is not None:
            self.response = response

    @property
    def response(self):
        """Gets the response of this TestConnectorResponse.  # noqa: E501

        Success or failure of the connection test.  # noqa: E501

        :return: The response of this TestConnectorResponse.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this TestConnectorResponse.

        Success or failure of the connection test.  # noqa: E501

        :param response: The response of this TestConnectorResponse.  # noqa: E501
        :type: str
        """

        self._response = response

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
        if issubclass(TestConnectorResponse, dict):
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
        if not isinstance(other, TestConnectorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other