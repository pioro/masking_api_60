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


class AsyncTask(object):
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
        'async_task_id': 'int',
        'operation': 'str',
        'reference': 'str',
        'status': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'cancellable': 'bool'
    }

    attribute_map = {
        'async_task_id': 'asyncTaskId',
        'operation': 'operation',
        'reference': 'reference',
        'status': 'status',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'cancellable': 'cancellable'
    }

    def __init__(self, async_task_id=None, operation=None, reference=None, status=None, start_time=None, end_time=None, cancellable=None):  # noqa: E501
        """AsyncTask - a model defined in Swagger"""  # noqa: E501

        self._async_task_id = None
        self._operation = None
        self._reference = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._cancellable = None
        self.discriminator = None

        if async_task_id is not None:
            self.async_task_id = async_task_id
        if operation is not None:
            self.operation = operation
        if reference is not None:
            self.reference = reference
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cancellable is not None:
            self.cancellable = cancellable

    @property
    def async_task_id(self):
        """Gets the async_task_id of this AsyncTask.  # noqa: E501

        The ID of the AsyncTask. This field will be generated by the Masking Engine.  # noqa: E501

        :return: The async_task_id of this AsyncTask.  # noqa: E501
        :rtype: int
        """
        return self._async_task_id

    @async_task_id.setter
    def async_task_id(self, async_task_id):
        """Sets the async_task_id of this AsyncTask.

        The ID of the AsyncTask. This field will be generated by the Masking Engine.  # noqa: E501

        :param async_task_id: The async_task_id of this AsyncTask.  # noqa: E501
        :type: int
        """

        self._async_task_id = async_task_id

    @property
    def operation(self):
        """Gets the operation of this AsyncTask.  # noqa: E501

        The type of operation that the AsyncTask is performing.  # noqa: E501

        :return: The operation of this AsyncTask.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AsyncTask.

        The type of operation that the AsyncTask is performing.  # noqa: E501

        :param operation: The operation of this AsyncTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALGORITHM_CREATE", "ALGORITHM_UPDATE", "DATAFILE_BULK_UPDATE", "ENCRYPTION_KEY_CREATE", "EXPORT", "IMPORT", "RULESET_REFRESH", "TABLE_BULK_UPDATE", "MAINFRAME_DATASET_BULK_UPDATE"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def reference(self):
        """Gets the reference of this AsyncTask.  # noqa: E501

        The reference for the AsyncTask. An example of a reference is the ruleset ID for a RULESET_REFRESH operation.  # noqa: E501

        :return: The reference of this AsyncTask.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this AsyncTask.

        The reference for the AsyncTask. An example of a reference is the ruleset ID for a RULESET_REFRESH operation.  # noqa: E501

        :param reference: The reference of this AsyncTask.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 255:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `255`")  # noqa: E501

        self._reference = reference

    @property
    def status(self):
        """Gets the status of this AsyncTask.  # noqa: E501

        The status of the AsyncTask in regard to its completion.  # noqa: E501

        :return: The status of this AsyncTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AsyncTask.

        The status of the AsyncTask in regard to its completion.  # noqa: E501

        :param status: The status of this AsyncTask.  # noqa: E501
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
    def start_time(self):
        """Gets the start_time of this AsyncTask.  # noqa: E501

        The date and time that this AsyncTask was started.  # noqa: E501

        :return: The start_time of this AsyncTask.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AsyncTask.

        The date and time that this AsyncTask was started.  # noqa: E501

        :param start_time: The start_time of this AsyncTask.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AsyncTask.  # noqa: E501

        The date and time that this AsyncTask completed.  # noqa: E501

        :return: The end_time of this AsyncTask.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AsyncTask.

        The date and time that this AsyncTask completed.  # noqa: E501

        :param end_time: The end_time of this AsyncTask.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def cancellable(self):
        """Gets the cancellable of this AsyncTask.  # noqa: E501

        True if the AsyncTask can be cancelled, false otherwise.  # noqa: E501

        :return: The cancellable of this AsyncTask.  # noqa: E501
        :rtype: bool
        """
        return self._cancellable

    @cancellable.setter
    def cancellable(self, cancellable):
        """Sets the cancellable of this AsyncTask.

        True if the AsyncTask can be cancelled, false otherwise.  # noqa: E501

        :param cancellable: The cancellable of this AsyncTask.  # noqa: E501
        :type: bool
        """

        self._cancellable = cancellable

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
        if issubclass(AsyncTask, dict):
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
        if not isinstance(other, AsyncTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
