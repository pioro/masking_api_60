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


class FileMetadata(object):
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
        'file_metadata_id': 'int',
        'file_name': 'str',
        'ruleset_id': 'int',
        'file_format_id': 'int',
        'file_type': 'str',
        'delimiter': 'str',
        'enclosure': 'str',
        'end_of_record': 'str',
        'name_is_regular_expression': 'bool'
    }

    attribute_map = {
        'file_metadata_id': 'fileMetadataId',
        'file_name': 'fileName',
        'ruleset_id': 'rulesetId',
        'file_format_id': 'fileFormatId',
        'file_type': 'fileType',
        'delimiter': 'delimiter',
        'enclosure': 'enclosure',
        'end_of_record': 'endOfRecord',
        'name_is_regular_expression': 'nameIsRegularExpression'
    }

    def __init__(self, file_metadata_id=None, file_name=None, ruleset_id=None, file_format_id=None, file_type=None, delimiter=None, enclosure=None, end_of_record=None, name_is_regular_expression=False):  # noqa: E501
        """FileMetadata - a model defined in Swagger"""  # noqa: E501

        self._file_metadata_id = None
        self._file_name = None
        self._ruleset_id = None
        self._file_format_id = None
        self._file_type = None
        self._delimiter = None
        self._enclosure = None
        self._end_of_record = None
        self._name_is_regular_expression = None
        self.discriminator = None

        if file_metadata_id is not None:
            self.file_metadata_id = file_metadata_id
        self.file_name = file_name
        self.ruleset_id = ruleset_id
        if file_format_id is not None:
            self.file_format_id = file_format_id
        if file_type is not None:
            self.file_type = file_type
        if delimiter is not None:
            self.delimiter = delimiter
        if enclosure is not None:
            self.enclosure = enclosure
        if end_of_record is not None:
            self.end_of_record = end_of_record
        if name_is_regular_expression is not None:
            self.name_is_regular_expression = name_is_regular_expression

    @property
    def file_metadata_id(self):
        """Gets the file_metadata_id of this FileMetadata.  # noqa: E501

        The ID of the file metadata. This field is set by the Masking Engine.  # noqa: E501

        :return: The file_metadata_id of this FileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._file_metadata_id

    @file_metadata_id.setter
    def file_metadata_id(self, file_metadata_id):
        """Sets the file_metadata_id of this FileMetadata.

        The ID of the file metadata. This field is set by the Masking Engine.  # noqa: E501

        :param file_metadata_id: The file_metadata_id of this FileMetadata.  # noqa: E501
        :type: int
        """

        self._file_metadata_id = file_metadata_id

    @property
    def file_name(self):
        """Gets the file_name of this FileMetadata.  # noqa: E501

        The name of the file metadata. This name must match the name of a file in the ruleset it is created on. This name must be unique for the given ruleset; in other words, the same file cannot be added to a ruleset more than once.  # noqa: E501

        :return: The file_name of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileMetadata.

        The name of the file metadata. This name must match the name of a file in the ruleset it is created on. This name must be unique for the given ruleset; in other words, the same file cannot be added to a ruleset more than once.  # noqa: E501

        :param file_name: The file_name of this FileMetadata.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501
        if file_name is not None and len(file_name) > 255:
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `255`")  # noqa: E501

        self._file_name = file_name

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this FileMetadata.  # noqa: E501

        The ID of the ruleset to create the file metadata on.  # noqa: E501

        :return: The ruleset_id of this FileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this FileMetadata.

        The ID of the ruleset to create the file metadata on.  # noqa: E501

        :param ruleset_id: The ruleset_id of this FileMetadata.  # noqa: E501
        :type: int
        """
        if ruleset_id is None:
            raise ValueError("Invalid value for `ruleset_id`, must not be `None`")  # noqa: E501

        self._ruleset_id = ruleset_id

    @property
    def file_format_id(self):
        """Gets the file_format_id of this FileMetadata.  # noqa: E501

        The ID of the file format corresponding to this file. It is used to determine the fields for this file. This field is required.  # noqa: E501

        :return: The file_format_id of this FileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._file_format_id

    @file_format_id.setter
    def file_format_id(self, file_format_id):
        """Sets the file_format_id of this FileMetadata.

        The ID of the file format corresponding to this file. It is used to determine the fields for this file. This field is required.  # noqa: E501

        :param file_format_id: The file_format_id of this FileMetadata.  # noqa: E501
        :type: int
        """

        self._file_format_id = file_format_id

    @property
    def file_type(self):
        """Gets the file_type of this FileMetadata.  # noqa: E501

        The type of file this is. This field will match the file connector file type.  # noqa: E501

        :return: The file_type of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileMetadata.

        The type of file this is. This field will match the file connector file type.  # noqa: E501

        :param file_type: The file_type of this FileMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELIMITED", "FIXED_WIDTH", "XML"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def delimiter(self):
        """Gets the delimiter of this FileMetadata.  # noqa: E501

        The delimiter for a delimited file. This field should be left blank for other file types.  # noqa: E501

        :return: The delimiter of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this FileMetadata.

        The delimiter for a delimited file. This field should be left blank for other file types.  # noqa: E501

        :param delimiter: The delimiter of this FileMetadata.  # noqa: E501
        :type: str
        """
        if delimiter is not None and len(delimiter) > 50:
            raise ValueError("Invalid value for `delimiter`, length must be less than or equal to `50`")  # noqa: E501

        self._delimiter = delimiter

    @property
    def enclosure(self):
        """Gets the enclosure of this FileMetadata.  # noqa: E501

        The text enclosure for the file.  # noqa: E501

        :return: The enclosure of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._enclosure

    @enclosure.setter
    def enclosure(self, enclosure):
        """Sets the enclosure of this FileMetadata.

        The text enclosure for the file.  # noqa: E501

        :param enclosure: The enclosure of this FileMetadata.  # noqa: E501
        :type: str
        """
        if enclosure is not None and len(enclosure) > 5:
            raise ValueError("Invalid value for `enclosure`, length must be less than or equal to `5`")  # noqa: E501

        self._enclosure = enclosure

    @property
    def end_of_record(self):
        """Gets the end_of_record of this FileMetadata.  # noqa: E501

        The string of characters that delineates the end-of-record for a file. Note that, for linux this is '\\n', and for windows it is '\\r\\n'.  # noqa: E501

        :return: The end_of_record of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._end_of_record

    @end_of_record.setter
    def end_of_record(self, end_of_record):
        """Sets the end_of_record of this FileMetadata.

        The string of characters that delineates the end-of-record for a file. Note that, for linux this is '\\n', and for windows it is '\\r\\n'.  # noqa: E501

        :param end_of_record: The end_of_record of this FileMetadata.  # noqa: E501
        :type: str
        """
        if end_of_record is not None and len(end_of_record) > 25:
            raise ValueError("Invalid value for `end_of_record`, length must be less than or equal to `25`")  # noqa: E501

        self._end_of_record = end_of_record

    @property
    def name_is_regular_expression(self):
        """Gets the name_is_regular_expression of this FileMetadata.  # noqa: E501

        Whether or not this file name represents a regular expression.  # noqa: E501

        :return: The name_is_regular_expression of this FileMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._name_is_regular_expression

    @name_is_regular_expression.setter
    def name_is_regular_expression(self, name_is_regular_expression):
        """Sets the name_is_regular_expression of this FileMetadata.

        Whether or not this file name represents a regular expression.  # noqa: E501

        :param name_is_regular_expression: The name_is_regular_expression of this FileMetadata.  # noqa: E501
        :type: bool
        """

        self._name_is_regular_expression = name_is_regular_expression

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
        if issubclass(FileMetadata, dict):
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
        if not isinstance(other, FileMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
