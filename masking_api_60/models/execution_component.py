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


class ExecutionComponent(object):
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
        'execution_component_id': 'int',
        'component_name': 'str',
        'execution_id': 'int',
        'status': 'str',
        'rows_masked': 'int',
        'rows_total': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'execution_component_id': 'executionComponentId',
        'component_name': 'componentName',
        'execution_id': 'executionId',
        'status': 'status',
        'rows_masked': 'rowsMasked',
        'rows_total': 'rowsTotal',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, execution_component_id=None, component_name=None, execution_id=None, status=None, rows_masked=None, rows_total=None, start_time=None, end_time=None):  # noqa: E501
        """ExecutionComponent - a model defined in Swagger"""  # noqa: E501

        self._execution_component_id = None
        self._component_name = None
        self._execution_id = None
        self._status = None
        self._rows_masked = None
        self._rows_total = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if execution_component_id is not None:
            self.execution_component_id = execution_component_id
        if component_name is not None:
            self.component_name = component_name
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if rows_masked is not None:
            self.rows_masked = rows_masked
        if rows_total is not None:
            self.rows_total = rows_total
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def execution_component_id(self):
        """Gets the execution_component_id of this ExecutionComponent.  # noqa: E501

        The ID of the execution component.  # noqa: E501

        :return: The execution_component_id of this ExecutionComponent.  # noqa: E501
        :rtype: int
        """
        return self._execution_component_id

    @execution_component_id.setter
    def execution_component_id(self, execution_component_id):
        """Sets the execution_component_id of this ExecutionComponent.

        The ID of the execution component.  # noqa: E501

        :param execution_component_id: The execution_component_id of this ExecutionComponent.  # noqa: E501
        :type: int
        """

        self._execution_component_id = execution_component_id

    @property
    def component_name(self):
        """Gets the component_name of this ExecutionComponent.  # noqa: E501

        The name of the component source e.g. the name of the file, table, or Mainframe Dataset file.  # noqa: E501

        :return: The component_name of this ExecutionComponent.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ExecutionComponent.

        The name of the component source e.g. the name of the file, table, or Mainframe Dataset file.  # noqa: E501

        :param component_name: The component_name of this ExecutionComponent.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

    @property
    def execution_id(self):
        """Gets the execution_id of this ExecutionComponent.  # noqa: E501

        The ID of the execution.  # noqa: E501

        :return: The execution_id of this ExecutionComponent.  # noqa: E501
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExecutionComponent.

        The ID of the execution.  # noqa: E501

        :param execution_id: The execution_id of this ExecutionComponent.  # noqa: E501
        :type: int
        """

        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this ExecutionComponent.  # noqa: E501

        The status of the execution of a component.  # noqa: E501

        :return: The status of this ExecutionComponent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionComponent.

        The status of the execution of a component.  # noqa: E501

        :param status: The status of this ExecutionComponent.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANCELLED", "FAILED", "RUNNING", "SUCCEEDED", "WAITING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def rows_masked(self):
        """Gets the rows_masked of this ExecutionComponent.  # noqa: E501

        The number of rows masked so far in the component.  # noqa: E501

        :return: The rows_masked of this ExecutionComponent.  # noqa: E501
        :rtype: int
        """
        return self._rows_masked

    @rows_masked.setter
    def rows_masked(self, rows_masked):
        """Sets the rows_masked of this ExecutionComponent.

        The number of rows masked so far in the component.  # noqa: E501

        :param rows_masked: The rows_masked of this ExecutionComponent.  # noqa: E501
        :type: int
        """

        self._rows_masked = rows_masked

    @property
    def rows_total(self):
        """Gets the rows_total of this ExecutionComponent.  # noqa: E501

        The total number of rows that should be masked in the component. This value is set to -1 while the total row count is being calculated.  # noqa: E501

        :return: The rows_total of this ExecutionComponent.  # noqa: E501
        :rtype: int
        """
        return self._rows_total

    @rows_total.setter
    def rows_total(self, rows_total):
        """Sets the rows_total of this ExecutionComponent.

        The total number of rows that should be masked in the component. This value is set to -1 while the total row count is being calculated.  # noqa: E501

        :param rows_total: The rows_total of this ExecutionComponent.  # noqa: E501
        :type: int
        """

        self._rows_total = rows_total

    @property
    def start_time(self):
        """Gets the start_time of this ExecutionComponent.  # noqa: E501

        The date and time that the masking engine starts operating on the component. This will be null for column level profiling and for components that the engine has not started masking.  # noqa: E501

        :return: The start_time of this ExecutionComponent.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ExecutionComponent.

        The date and time that the masking engine starts operating on the component. This will be null for column level profiling and for components that the engine has not started masking.  # noqa: E501

        :param start_time: The start_time of this ExecutionComponent.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ExecutionComponent.  # noqa: E501

        The date and time that the component is placed in a final state i.e. FAILED or SUCCEEDED.  # noqa: E501

        :return: The end_time of this ExecutionComponent.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ExecutionComponent.

        The date and time that the component is placed in a final state i.e. FAILED or SUCCEEDED.  # noqa: E501

        :param end_time: The end_time of this ExecutionComponent.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

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
        if issubclass(ExecutionComponent, dict):
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
        if not isinstance(other, ExecutionComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
