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


class NonConformantDataSample(object):
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
        'data_sample_id': 'int',
        'execution_event_id': 'int',
        'data_sample': 'str',
        'count': 'int'
    }

    attribute_map = {
        'data_sample_id': 'dataSampleId',
        'execution_event_id': 'executionEventId',
        'data_sample': 'dataSample',
        'count': 'count'
    }

    def __init__(self, data_sample_id=None, execution_event_id=None, data_sample=None, count=None):  # noqa: E501
        """NonConformantDataSample - a model defined in Swagger"""  # noqa: E501

        self._data_sample_id = None
        self._execution_event_id = None
        self._data_sample = None
        self._count = None
        self.discriminator = None

        if data_sample_id is not None:
            self.data_sample_id = data_sample_id
        if execution_event_id is not None:
            self.execution_event_id = execution_event_id
        if data_sample is not None:
            self.data_sample = data_sample
        if count is not None:
            self.count = count

    @property
    def data_sample_id(self):
        """Gets the data_sample_id of this NonConformantDataSample.  # noqa: E501

        The ID of the non-conformant data sample.  # noqa: E501

        :return: The data_sample_id of this NonConformantDataSample.  # noqa: E501
        :rtype: int
        """
        return self._data_sample_id

    @data_sample_id.setter
    def data_sample_id(self, data_sample_id):
        """Sets the data_sample_id of this NonConformantDataSample.

        The ID of the non-conformant data sample.  # noqa: E501

        :param data_sample_id: The data_sample_id of this NonConformantDataSample.  # noqa: E501
        :type: int
        """

        self._data_sample_id = data_sample_id

    @property
    def execution_event_id(self):
        """Gets the execution_event_id of this NonConformantDataSample.  # noqa: E501

        The ID of the execution event this sample is associated with.  # noqa: E501

        :return: The execution_event_id of this NonConformantDataSample.  # noqa: E501
        :rtype: int
        """
        return self._execution_event_id

    @execution_event_id.setter
    def execution_event_id(self, execution_event_id):
        """Sets the execution_event_id of this NonConformantDataSample.

        The ID of the execution event this sample is associated with.  # noqa: E501

        :param execution_event_id: The execution_event_id of this NonConformantDataSample.  # noqa: E501
        :type: int
        """

        self._execution_event_id = execution_event_id

    @property
    def data_sample(self):
        """Gets the data_sample of this NonConformantDataSample.  # noqa: E501

        The redacted value of the non-conformant field data that could not be masked by the assigned algorithm.  # noqa: E501

        :return: The data_sample of this NonConformantDataSample.  # noqa: E501
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample):
        """Sets the data_sample of this NonConformantDataSample.

        The redacted value of the non-conformant field data that could not be masked by the assigned algorithm.  # noqa: E501

        :param data_sample: The data_sample of this NonConformantDataSample.  # noqa: E501
        :type: str
        """

        self._data_sample = data_sample

    @property
    def count(self):
        """Gets the count of this NonConformantDataSample.  # noqa: E501

        The approximate number of times this data pattern was encountered.  # noqa: E501

        :return: The count of this NonConformantDataSample.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NonConformantDataSample.

        The approximate number of times this data pattern was encountered.  # noqa: E501

        :param count: The count of this NonConformantDataSample.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(NonConformantDataSample, dict):
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
        if not isinstance(other, NonConformantDataSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
