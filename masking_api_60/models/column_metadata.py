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


class ColumnMetadata(object):
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
        'column_metadata_id': 'int',
        'column_name': 'str',
        'table_metadata_id': 'int',
        'algorithm_name': 'str',
        'domain_name': 'str',
        'data_type': 'str',
        'date_format': 'str',
        'column_length': 'int',
        'is_masked': 'bool',
        'is_profiler_writable': 'bool',
        'is_primary_key': 'bool',
        'is_index': 'bool',
        'is_foreign_key': 'bool',
        'notes': 'str'
    }

    attribute_map = {
        'column_metadata_id': 'columnMetadataId',
        'column_name': 'columnName',
        'table_metadata_id': 'tableMetadataId',
        'algorithm_name': 'algorithmName',
        'domain_name': 'domainName',
        'data_type': 'dataType',
        'date_format': 'dateFormat',
        'column_length': 'columnLength',
        'is_masked': 'isMasked',
        'is_profiler_writable': 'isProfilerWritable',
        'is_primary_key': 'isPrimaryKey',
        'is_index': 'isIndex',
        'is_foreign_key': 'isForeignKey',
        'notes': 'notes'
    }

    def __init__(self, column_metadata_id=None, column_name=None, table_metadata_id=None, algorithm_name=None, domain_name=None, data_type=None, date_format=None, column_length=None, is_masked=None, is_profiler_writable=None, is_primary_key=None, is_index=None, is_foreign_key=None, notes=None):  # noqa: E501
        """ColumnMetadata - a model defined in Swagger"""  # noqa: E501

        self._column_metadata_id = None
        self._column_name = None
        self._table_metadata_id = None
        self._algorithm_name = None
        self._domain_name = None
        self._data_type = None
        self._date_format = None
        self._column_length = None
        self._is_masked = None
        self._is_profiler_writable = None
        self._is_primary_key = None
        self._is_index = None
        self._is_foreign_key = None
        self._notes = None
        self.discriminator = None

        if column_metadata_id is not None:
            self.column_metadata_id = column_metadata_id
        if column_name is not None:
            self.column_name = column_name
        if table_metadata_id is not None:
            self.table_metadata_id = table_metadata_id
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if domain_name is not None:
            self.domain_name = domain_name
        if data_type is not None:
            self.data_type = data_type
        if date_format is not None:
            self.date_format = date_format
        if column_length is not None:
            self.column_length = column_length
        if is_masked is not None:
            self.is_masked = is_masked
        self.is_profiler_writable = is_profiler_writable
        if is_primary_key is not None:
            self.is_primary_key = is_primary_key
        if is_index is not None:
            self.is_index = is_index
        if is_foreign_key is not None:
            self.is_foreign_key = is_foreign_key
        if notes is not None:
            self.notes = notes

    @property
    def column_metadata_id(self):
        """Gets the column_metadata_id of this ColumnMetadata.  # noqa: E501

        The ID number of the column metadata. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The column_metadata_id of this ColumnMetadata.  # noqa: E501
        :rtype: int
        """
        return self._column_metadata_id

    @column_metadata_id.setter
    def column_metadata_id(self, column_metadata_id):
        """Sets the column_metadata_id of this ColumnMetadata.

        The ID number of the column metadata. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param column_metadata_id: The column_metadata_id of this ColumnMetadata.  # noqa: E501
        :type: int
        """

        self._column_metadata_id = column_metadata_id

    @property
    def column_name(self):
        """Gets the column_name of this ColumnMetadata.  # noqa: E501

        The name of the column, as determined by the underlying table.  # noqa: E501

        :return: The column_name of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnMetadata.

        The name of the column, as determined by the underlying table.  # noqa: E501

        :param column_name: The column_name of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if column_name is not None and len(column_name) > 255:
            raise ValueError("Invalid value for `column_name`, length must be less than or equal to `255`")  # noqa: E501

        self._column_name = column_name

    @property
    def table_metadata_id(self):
        """Gets the table_metadata_id of this ColumnMetadata.  # noqa: E501

        The ID number of the table metadata that this column is a part of. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The table_metadata_id of this ColumnMetadata.  # noqa: E501
        :rtype: int
        """
        return self._table_metadata_id

    @table_metadata_id.setter
    def table_metadata_id(self, table_metadata_id):
        """Sets the table_metadata_id of this ColumnMetadata.

        The ID number of the table metadata that this column is a part of. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param table_metadata_id: The table_metadata_id of this ColumnMetadata.  # noqa: E501
        :type: int
        """

        self._table_metadata_id = table_metadata_id

    @property
    def algorithm_name(self):
        """Gets the algorithm_name of this ColumnMetadata.  # noqa: E501

        The name of the algorithm assigned to this column. Columns that are unmasked should have this property unset, in addition to having 'domainName' unset. If this field is set, then the 'domainName' must also be specified.  # noqa: E501

        :return: The algorithm_name of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        """Sets the algorithm_name of this ColumnMetadata.

        The name of the algorithm assigned to this column. Columns that are unmasked should have this property unset, in addition to having 'domainName' unset. If this field is set, then the 'domainName' must also be specified.  # noqa: E501

        :param algorithm_name: The algorithm_name of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if algorithm_name is not None and len(algorithm_name) > 500:
            raise ValueError("Invalid value for `algorithm_name`, length must be less than or equal to `500`")  # noqa: E501

        self._algorithm_name = algorithm_name

    @property
    def domain_name(self):
        """Gets the domain_name of this ColumnMetadata.  # noqa: E501

        The name of the domain assigned to this column. Columns that are left unmasked should have this property unset. If the 'domainName' is set, but the 'algorithmName' is unset, then the default algorithm corresponding to the 'domainName' will be used.  # noqa: E501

        :return: The domain_name of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ColumnMetadata.

        The name of the domain assigned to this column. Columns that are left unmasked should have this property unset. If the 'domainName' is set, but the 'algorithmName' is unset, then the default algorithm corresponding to the 'domainName' will be used.  # noqa: E501

        :param domain_name: The domain_name of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if domain_name is not None and len(domain_name) > 20:
            raise ValueError("Invalid value for `domain_name`, length must be less than or equal to `20`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def data_type(self):
        """Gets the data_type of this ColumnMetadata.  # noqa: E501

        The data type of this column.  # noqa: E501

        :return: The data_type of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ColumnMetadata.

        The data type of this column.  # noqa: E501

        :param data_type: The data_type of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if data_type is not None and len(data_type) > 50:
            raise ValueError("Invalid value for `data_type`, length must be less than or equal to `50`")  # noqa: E501

        self._data_type = data_type

    @property
    def date_format(self):
        """Gets the date_format of this ColumnMetadata.  # noqa: E501

        The date format of the date assigned to this column.  # noqa: E501

        :return: The date_format of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ColumnMetadata.

        The date format of the date assigned to this column.  # noqa: E501

        :param date_format: The date_format of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if date_format is not None and len(date_format) > 50:
            raise ValueError("Invalid value for `date_format`, length must be less than or equal to `50`")  # noqa: E501

        self._date_format = date_format

    @property
    def column_length(self):
        """Gets the column_length of this ColumnMetadata.  # noqa: E501

        The length of the column, in number of characters, as determined by the underlying table.  # noqa: E501

        :return: The column_length of this ColumnMetadata.  # noqa: E501
        :rtype: int
        """
        return self._column_length

    @column_length.setter
    def column_length(self, column_length):
        """Sets the column_length of this ColumnMetadata.

        The length of the column, in number of characters, as determined by the underlying table.  # noqa: E501

        :param column_length: The column_length of this ColumnMetadata.  # noqa: E501
        :type: int
        """

        self._column_length = column_length

    @property
    def is_masked(self):
        """Gets the is_masked of this ColumnMetadata.  # noqa: E501

        This field indicates whether or not a column is being masked. This field is assigned by the Masking Engine to true or false based on whether the column is assigned an algorithm and domain.  # noqa: E501

        :return: The is_masked of this ColumnMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_masked

    @is_masked.setter
    def is_masked(self, is_masked):
        """Sets the is_masked of this ColumnMetadata.

        This field indicates whether or not a column is being masked. This field is assigned by the Masking Engine to true or false based on whether the column is assigned an algorithm and domain.  # noqa: E501

        :param is_masked: The is_masked of this ColumnMetadata.  # noqa: E501
        :type: bool
        """

        self._is_masked = is_masked

    @property
    def is_profiler_writable(self):
        """Gets the is_profiler_writable of this ColumnMetadata.  # noqa: E501

        This field indicates whether or not a column's fields (e.g. algorithm or domain assignment) may be modified during the execution of a profile job when there is a profiling match.  # noqa: E501

        :return: The is_profiler_writable of this ColumnMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_profiler_writable

    @is_profiler_writable.setter
    def is_profiler_writable(self, is_profiler_writable):
        """Sets the is_profiler_writable of this ColumnMetadata.

        This field indicates whether or not a column's fields (e.g. algorithm or domain assignment) may be modified during the execution of a profile job when there is a profiling match.  # noqa: E501

        :param is_profiler_writable: The is_profiler_writable of this ColumnMetadata.  # noqa: E501
        :type: bool
        """
        if is_profiler_writable is None:
            raise ValueError("Invalid value for `is_profiler_writable`, must not be `None`")  # noqa: E501

        self._is_profiler_writable = is_profiler_writable

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this ColumnMetadata.  # noqa: E501

        This field indicates whether or not a column is a primary key. This field is determined by the Masking Engine.  # noqa: E501

        :return: The is_primary_key of this ColumnMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this ColumnMetadata.

        This field indicates whether or not a column is a primary key. This field is determined by the Masking Engine.  # noqa: E501

        :param is_primary_key: The is_primary_key of this ColumnMetadata.  # noqa: E501
        :type: bool
        """

        self._is_primary_key = is_primary_key

    @property
    def is_index(self):
        """Gets the is_index of this ColumnMetadata.  # noqa: E501

        This field indicates whether or not a column is an index. This field is determined by the Masking Engine.  # noqa: E501

        :return: The is_index of this ColumnMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_index

    @is_index.setter
    def is_index(self, is_index):
        """Sets the is_index of this ColumnMetadata.

        This field indicates whether or not a column is an index. This field is determined by the Masking Engine.  # noqa: E501

        :param is_index: The is_index of this ColumnMetadata.  # noqa: E501
        :type: bool
        """

        self._is_index = is_index

    @property
    def is_foreign_key(self):
        """Gets the is_foreign_key of this ColumnMetadata.  # noqa: E501

        This field indicates whether or not a column is a foreign key. This field is determined by the Masking Engine.  # noqa: E501

        :return: The is_foreign_key of this ColumnMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_foreign_key

    @is_foreign_key.setter
    def is_foreign_key(self, is_foreign_key):
        """Sets the is_foreign_key of this ColumnMetadata.

        This field indicates whether or not a column is a foreign key. This field is determined by the Masking Engine.  # noqa: E501

        :param is_foreign_key: The is_foreign_key of this ColumnMetadata.  # noqa: E501
        :type: bool
        """

        self._is_foreign_key = is_foreign_key

    @property
    def notes(self):
        """Gets the notes of this ColumnMetadata.  # noqa: E501

        This field is used to store additional information about the column.  # noqa: E501

        :return: The notes of this ColumnMetadata.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ColumnMetadata.

        This field is used to store additional information about the column.  # noqa: E501

        :param notes: The notes of this ColumnMetadata.  # noqa: E501
        :type: str
        """
        if notes is not None and len(notes) > 500:
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `500`")  # noqa: E501

        self._notes = notes

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
        if issubclass(ColumnMetadata, dict):
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
        if not isinstance(other, ColumnMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
