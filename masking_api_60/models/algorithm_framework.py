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


class AlgorithmFramework(object):
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
        'framework_id': 'int',
        'framework_name': 'str',
        'framework_type': 'str',
        'plugin': 'PluginBase',
        'extension_schema': 'object'
    }

    attribute_map = {
        'framework_id': 'frameworkId',
        'framework_name': 'frameworkName',
        'framework_type': 'frameworkType',
        'plugin': 'plugin',
        'extension_schema': 'extensionSchema'
    }

    def __init__(self, framework_id=None, framework_name=None, framework_type=None, plugin=None, extension_schema=None):  # noqa: E501
        """AlgorithmFramework - a model defined in Swagger"""  # noqa: E501

        self._framework_id = None
        self._framework_name = None
        self._framework_type = None
        self._plugin = None
        self._extension_schema = None
        self.discriminator = None

        if framework_id is not None:
            self.framework_id = framework_id
        if framework_name is not None:
            self.framework_name = framework_name
        if framework_type is not None:
            self.framework_type = framework_type
        if plugin is not None:
            self.plugin = plugin
        if extension_schema is not None:
            self.extension_schema = extension_schema

    @property
    def framework_id(self):
        """Gets the framework_id of this AlgorithmFramework.  # noqa: E501

        The id of the algorithm framework installed using Plugin API.  # noqa: E501

        :return: The framework_id of this AlgorithmFramework.  # noqa: E501
        :rtype: int
        """
        return self._framework_id

    @framework_id.setter
    def framework_id(self, framework_id):
        """Sets the framework_id of this AlgorithmFramework.

        The id of the algorithm framework installed using Plugin API.  # noqa: E501

        :param framework_id: The framework_id of this AlgorithmFramework.  # noqa: E501
        :type: int
        """

        self._framework_id = framework_id

    @property
    def framework_name(self):
        """Gets the framework_name of this AlgorithmFramework.  # noqa: E501

        The name of the algorithm framework installed using Plugin API.  # noqa: E501

        :return: The framework_name of this AlgorithmFramework.  # noqa: E501
        :rtype: str
        """
        return self._framework_name

    @framework_name.setter
    def framework_name(self, framework_name):
        """Sets the framework_name of this AlgorithmFramework.

        The name of the algorithm framework installed using Plugin API.  # noqa: E501

        :param framework_name: The framework_name of this AlgorithmFramework.  # noqa: E501
        :type: str
        """
        if framework_name is not None and len(framework_name) > 255:
            raise ValueError("Invalid value for `framework_name`, length must be less than or equal to `255`")  # noqa: E501

        self._framework_name = framework_name

    @property
    def framework_type(self):
        """Gets the framework_type of this AlgorithmFramework.  # noqa: E501

        The type of value this algorithm framework masks.  # noqa: E501

        :return: The framework_type of this AlgorithmFramework.  # noqa: E501
        :rtype: str
        """
        return self._framework_type

    @framework_type.setter
    def framework_type(self, framework_type):
        """Sets the framework_type of this AlgorithmFramework.

        The type of value this algorithm framework masks.  # noqa: E501

        :param framework_type: The framework_type of this AlgorithmFramework.  # noqa: E501
        :type: str
        """
        allowed_values = ["BIG_DECIMAL", "DATE", "STRING", "BYTE_BUFFER"]  # noqa: E501
        if framework_type not in allowed_values:
            raise ValueError(
                "Invalid value for `framework_type` ({0}), must be one of {1}"  # noqa: E501
                .format(framework_type, allowed_values)
            )

        self._framework_type = framework_type

    @property
    def plugin(self):
        """Gets the plugin of this AlgorithmFramework.  # noqa: E501


        :return: The plugin of this AlgorithmFramework.  # noqa: E501
        :rtype: PluginBase
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        """Sets the plugin of this AlgorithmFramework.


        :param plugin: The plugin of this AlgorithmFramework.  # noqa: E501
        :type: PluginBase
        """

        self._plugin = plugin

    @property
    def extension_schema(self):
        """Gets the extension_schema of this AlgorithmFramework.  # noqa: E501

        The JSON schema of algorithmExtension used by this framework  # noqa: E501

        :return: The extension_schema of this AlgorithmFramework.  # noqa: E501
        :rtype: object
        """
        return self._extension_schema

    @extension_schema.setter
    def extension_schema(self, extension_schema):
        """Sets the extension_schema of this AlgorithmFramework.

        The JSON schema of algorithmExtension used by this framework  # noqa: E501

        :param extension_schema: The extension_schema of this AlgorithmFramework.  # noqa: E501
        :type: object
        """

        self._extension_schema = extension_schema

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
        if issubclass(AlgorithmFramework, dict):
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
        if not isinstance(other, AlgorithmFramework):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
