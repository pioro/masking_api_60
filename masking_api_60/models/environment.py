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


class Environment(object):
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
        'environment_id': 'int',
        'environment_name': 'str',
        'application_id': 'int',
        'purpose': 'str',
        'is_workflow_enabled': 'bool'
    }

    attribute_map = {
        'environment_id': 'environmentId',
        'environment_name': 'environmentName',
        'application_id': 'applicationId',
        'purpose': 'purpose',
        'is_workflow_enabled': 'isWorkflowEnabled'
    }

    def __init__(self, environment_id=None, environment_name=None, application_id=None, purpose=None, is_workflow_enabled=False):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501

        self._environment_id = None
        self._environment_name = None
        self._application_id = None
        self._purpose = None
        self._is_workflow_enabled = None
        self.discriminator = None

        if environment_id is not None:
            self.environment_id = environment_id
        self.environment_name = environment_name
        self.application_id = application_id
        self.purpose = purpose
        if is_workflow_enabled is not None:
            self.is_workflow_enabled = is_workflow_enabled

    @property
    def environment_id(self):
        """Gets the environment_id of this Environment.  # noqa: E501

        The ID of the Environment. This field will be generated by the Masking Engine.  # noqa: E501

        :return: The environment_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this Environment.

        The ID of the Environment. This field will be generated by the Masking Engine.  # noqa: E501

        :param environment_id: The environment_id of this Environment.  # noqa: E501
        :type: int
        """

        self._environment_id = environment_id

    @property
    def environment_name(self):
        """Gets the environment_name of this Environment.  # noqa: E501

        The name for this Environment. Note that it must be unique among Environments.  # noqa: E501

        :return: The environment_name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this Environment.

        The name for this Environment. Note that it must be unique among Environments.  # noqa: E501

        :param environment_name: The environment_name of this Environment.  # noqa: E501
        :type: str
        """
        if environment_name is None:
            raise ValueError("Invalid value for `environment_name`, must not be `None`")  # noqa: E501
        if environment_name is not None and len(environment_name) > 255:
            raise ValueError("Invalid value for `environment_name`, length must be less than or equal to `255`")  # noqa: E501

        self._environment_name = environment_name

    @property
    def application_id(self):
        """Gets the application_id of this Environment.  # noqa: E501

        The ID of the associated application.  # noqa: E501

        :return: The application_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this Environment.

        The ID of the associated application.  # noqa: E501

        :param application_id: The application_id of this Environment.  # noqa: E501
        :type: int
        """
        if application_id is None:
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def purpose(self):
        """Gets the purpose of this Environment.  # noqa: E501

        The purpose of this Environment. Environments with a 'MASK' purpose will have access to Masking and Profiling jobs, whereas Environments with a 'TOKENIZE' purpose will have access to Tokenization and Re-Identification jobs. Note that any custom purposes created through the UI will be represented as 'MASK' purposes, due to the jobs that they have access to.  # noqa: E501

        :return: The purpose of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Environment.

        The purpose of this Environment. Environments with a 'MASK' purpose will have access to Masking and Profiling jobs, whereas Environments with a 'TOKENIZE' purpose will have access to Tokenization and Re-Identification jobs. Note that any custom purposes created through the UI will be represented as 'MASK' purposes, due to the jobs that they have access to.  # noqa: E501

        :param purpose: The purpose of this Environment.  # noqa: E501
        :type: str
        """
        if purpose is None:
            raise ValueError("Invalid value for `purpose`, must not be `None`")  # noqa: E501
        allowed_values = ["MASK", "TOKENIZE"]  # noqa: E501
        if purpose not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose` ({0}), must be one of {1}"  # noqa: E501
                .format(purpose, allowed_values)
            )

        self._purpose = purpose

    @property
    def is_workflow_enabled(self):
        """Gets the is_workflow_enabled of this Environment.  # noqa: E501

        True to have workflow enabled, false to leave the workflow disabled.  # noqa: E501

        :return: The is_workflow_enabled of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._is_workflow_enabled

    @is_workflow_enabled.setter
    def is_workflow_enabled(self, is_workflow_enabled):
        """Sets the is_workflow_enabled of this Environment.

        True to have workflow enabled, false to leave the workflow disabled.  # noqa: E501

        :param is_workflow_enabled: The is_workflow_enabled of this Environment.  # noqa: E501
        :type: bool
        """

        self._is_workflow_enabled = is_workflow_enabled

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
        if issubclass(Environment, dict):
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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
