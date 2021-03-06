# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OnTheFlyMaskingSource(object):
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
        'connector_id': 'int',
        'connector_type': 'str'
    }

    attribute_map = {
        'connector_id': 'connectorId',
        'connector_type': 'connectorType'
    }

    def __init__(self, connector_id=None, connector_type=None):  # noqa: E501
        """OnTheFlyMaskingSource - a model defined in Swagger"""  # noqa: E501

        self._connector_id = None
        self._connector_type = None
        self.discriminator = None

        self.connector_id = connector_id
        if connector_type is not None:
            self.connector_type = connector_type

    @property
    def connector_id(self):
        """Gets the connector_id of this OnTheFlyMaskingSource.  # noqa: E501

        The ID number of the source connector for the OnTheFly masking job.  # noqa: E501

        :return: The connector_id of this OnTheFlyMaskingSource.  # noqa: E501
        :rtype: int
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this OnTheFlyMaskingSource.

        The ID number of the source connector for the OnTheFly masking job.  # noqa: E501

        :param connector_id: The connector_id of this OnTheFlyMaskingSource.  # noqa: E501
        :type: int
        """
        if connector_id is None:
            raise ValueError("Invalid value for `connector_id`, must not be `None`")  # noqa: E501

        self._connector_id = connector_id

    @property
    def connector_type(self):
        """Gets the connector_type of this OnTheFlyMaskingSource.  # noqa: E501

        The type of the source connector for the OnTheFly masking job.  # noqa: E501

        :return: The connector_type of this OnTheFlyMaskingSource.  # noqa: E501
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """Sets the connector_type of this OnTheFlyMaskingSource.

        The type of the source connector for the OnTheFly masking job.  # noqa: E501

        :param connector_type: The connector_type of this OnTheFlyMaskingSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["DATABASE", "FILE", "VSAM"]  # noqa: E501
        if connector_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connector_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connector_type, allowed_values)
            )

        self._connector_type = connector_type

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
        if issubclass(OnTheFlyMaskingSource, dict):
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
        if not isinstance(other, OnTheFlyMaskingSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
