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


class JvmPermissionClassName(object):
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
        'jvm_permission_class_name_id': 'int',
        'value': 'str'
    }

    attribute_map = {
        'jvm_permission_class_name_id': 'jvmPermissionClassNameId',
        'value': 'value'
    }

    def __init__(self, jvm_permission_class_name_id=None, value=None):  # noqa: E501
        """JvmPermissionClassName - a model defined in Swagger"""  # noqa: E501

        self._jvm_permission_class_name_id = None
        self._value = None
        self.discriminator = None

        if jvm_permission_class_name_id is not None:
            self.jvm_permission_class_name_id = jvm_permission_class_name_id
        self.value = value

    @property
    def jvm_permission_class_name_id(self):
        """Gets the jvm_permission_class_name_id of this JvmPermissionClassName.  # noqa: E501

        The ID number of the permission class. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The jvm_permission_class_name_id of this JvmPermissionClassName.  # noqa: E501
        :rtype: int
        """
        return self._jvm_permission_class_name_id

    @jvm_permission_class_name_id.setter
    def jvm_permission_class_name_id(self, jvm_permission_class_name_id):
        """Sets the jvm_permission_class_name_id of this JvmPermissionClassName.

        The ID number of the permission class. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param jvm_permission_class_name_id: The jvm_permission_class_name_id of this JvmPermissionClassName.  # noqa: E501
        :type: int
        """

        self._jvm_permission_class_name_id = jvm_permission_class_name_id

    @property
    def value(self):
        """Gets the value of this JvmPermissionClassName.  # noqa: E501

        The name of the permission class.  # noqa: E501

        :return: The value of this JvmPermissionClassName.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JvmPermissionClassName.

        The name of the permission class.  # noqa: E501

        :param value: The value of this JvmPermissionClassName.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 255:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `255`")  # noqa: E501

        self._value = value

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
        if issubclass(JvmPermissionClassName, dict):
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
        if not isinstance(other, JvmPermissionClassName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
