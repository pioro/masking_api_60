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


class BreakpointStartData(object):
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
        'breakpoint_type': 'str',
        'enabled': 'bool',
        'timeout': 'int',
        'initial_skip_count': 'int'
    }

    attribute_map = {
        'breakpoint_type': 'breakpointType',
        'enabled': 'enabled',
        'timeout': 'timeout',
        'initial_skip_count': 'initialSkipCount'
    }

    def __init__(self, breakpoint_type=None, enabled=None, timeout=None, initial_skip_count=None):  # noqa: E501
        """BreakpointStartData - a model defined in Swagger"""  # noqa: E501

        self._breakpoint_type = None
        self._enabled = None
        self._timeout = None
        self._initial_skip_count = None
        self.discriminator = None

        if breakpoint_type is not None:
            self.breakpoint_type = breakpoint_type
        if enabled is not None:
            self.enabled = enabled
        if timeout is not None:
            self.timeout = timeout
        if initial_skip_count is not None:
            self.initial_skip_count = initial_skip_count

    @property
    def breakpoint_type(self):
        """Gets the breakpoint_type of this BreakpointStartData.  # noqa: E501

        The breakpoint type that identifies this breakpoint start data.  # noqa: E501

        :return: The breakpoint_type of this BreakpointStartData.  # noqa: E501
        :rtype: str
        """
        return self._breakpoint_type

    @breakpoint_type.setter
    def breakpoint_type(self, breakpoint_type):
        """Sets the breakpoint_type of this BreakpointStartData.

        The breakpoint type that identifies this breakpoint start data.  # noqa: E501

        :param breakpoint_type: The breakpoint_type of this BreakpointStartData.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXECUTION_MASK_END", "EXECUTION_MASK_PRE_KETTLE", "EXECUTION_PROFILE_COLUMN_PRE", "EXECUTION_PROFILE_DATA_PRE_KETTLE", "EXECUTION_PROFILE_END", "PROGRESS_REPORTER_POST_UPDATE", "PROGRESS_REPORTER_REMOVE_POST_LOCK", "PROGRESS_REPORTER_REMOVE_PRE_LOCK", "PROGRESS_REPORTER_UPDATE_POST_LOCK", "PROGRESS_REPORTER_UPDATE_PRE_LOCK", "RULESET_BULK_UPDATE_POST_TABLE_SAVE", "RULESET_BULK_UPDATE_POST_TABLE_UPDATE", "RULESET_BULK_UPDATE_START"]  # noqa: E501
        if breakpoint_type not in allowed_values:
            raise ValueError(
                "Invalid value for `breakpoint_type` ({0}), must be one of {1}"  # noqa: E501
                .format(breakpoint_type, allowed_values)
            )

        self._breakpoint_type = breakpoint_type

    @property
    def enabled(self):
        """Gets the enabled of this BreakpointStartData.  # noqa: E501

        True if the breakpoint is enabled, false otherwise.  # noqa: E501

        :return: The enabled of this BreakpointStartData.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BreakpointStartData.

        True if the breakpoint is enabled, false otherwise.  # noqa: E501

        :param enabled: The enabled of this BreakpointStartData.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def timeout(self):
        """Gets the timeout of this BreakpointStartData.  # noqa: E501

        The number of seconds to wait at the breakpoint before timing out.  # noqa: E501

        :return: The timeout of this BreakpointStartData.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this BreakpointStartData.

        The number of seconds to wait at the breakpoint before timing out.  # noqa: E501

        :param timeout: The timeout of this BreakpointStartData.  # noqa: E501
        :type: int
        """
        if timeout is not None and timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout = timeout

    @property
    def initial_skip_count(self):
        """Gets the initial_skip_count of this BreakpointStartData.  # noqa: E501

        The number of times to pass this breakpoint before waiting on it.  # noqa: E501

        :return: The initial_skip_count of this BreakpointStartData.  # noqa: E501
        :rtype: int
        """
        return self._initial_skip_count

    @initial_skip_count.setter
    def initial_skip_count(self, initial_skip_count):
        """Sets the initial_skip_count of this BreakpointStartData.

        The number of times to pass this breakpoint before waiting on it.  # noqa: E501

        :param initial_skip_count: The initial_skip_count of this BreakpointStartData.  # noqa: E501
        :type: int
        """
        if initial_skip_count is not None and initial_skip_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `initial_skip_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._initial_skip_count = initial_skip_count

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
        if issubclass(BreakpointStartData, dict):
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
        if not isinstance(other, BreakpointStartData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
