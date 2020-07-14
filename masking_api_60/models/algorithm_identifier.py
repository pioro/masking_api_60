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


class AlgorithmIdentifier(object):
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
        'algorithm_name': 'str'
    }

    attribute_map = {
        'algorithm_name': 'algorithmName'
    }

    def __init__(self, algorithm_name=None):  # noqa: E501
        """AlgorithmIdentifier - a model defined in Swagger"""  # noqa: E501

        self._algorithm_name = None
        self.discriminator = None

        self.algorithm_name = algorithm_name

    @property
    def algorithm_name(self):
        """Gets the algorithm_name of this AlgorithmIdentifier.  # noqa: E501


        :return: The algorithm_name of this AlgorithmIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        """Sets the algorithm_name of this AlgorithmIdentifier.


        :param algorithm_name: The algorithm_name of this AlgorithmIdentifier.  # noqa: E501
        :type: str
        """
        if algorithm_name is None:
            raise ValueError("Invalid value for `algorithm_name`, must not be `None`")  # noqa: E501
        if algorithm_name is not None and len(algorithm_name) > 100:
            raise ValueError("Invalid value for `algorithm_name`, length must be less than or equal to `100`")  # noqa: E501

        self._algorithm_name = algorithm_name

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
        if issubclass(AlgorithmIdentifier, dict):
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
        if not isinstance(other, AlgorithmIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
