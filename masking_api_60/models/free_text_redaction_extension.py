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


class FreeTextRedactionExtension(object):
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
        'deny_list_redaction': 'bool',
        'lookup_file_reference_id': 'str',
        'lookup_redaction_value': 'str',
        'profile_set_id': 'int',
        'profile_set_redaction_value': 'str'
    }

    attribute_map = {
        'deny_list_redaction': 'denyListRedaction',
        'lookup_file_reference_id': 'lookupFileReferenceId',
        'lookup_redaction_value': 'lookupRedactionValue',
        'profile_set_id': 'profileSetId',
        'profile_set_redaction_value': 'profileSetRedactionValue'
    }

    def __init__(self, deny_list_redaction=True, lookup_file_reference_id=None, lookup_redaction_value=None, profile_set_id=None, profile_set_redaction_value=None):  # noqa: E501
        """FreeTextRedactionExtension - a model defined in Swagger"""  # noqa: E501

        self._deny_list_redaction = None
        self._lookup_file_reference_id = None
        self._lookup_redaction_value = None
        self._profile_set_id = None
        self._profile_set_redaction_value = None
        self.discriminator = None

        if deny_list_redaction is not None:
            self.deny_list_redaction = deny_list_redaction
        if lookup_file_reference_id is not None:
            self.lookup_file_reference_id = lookup_file_reference_id
        if lookup_redaction_value is not None:
            self.lookup_redaction_value = lookup_redaction_value
        if profile_set_id is not None:
            self.profile_set_id = profile_set_id
        if profile_set_redaction_value is not None:
            self.profile_set_redaction_value = profile_set_redaction_value

    @property
    def deny_list_redaction(self):
        """Gets the deny_list_redaction of this FreeTextRedactionExtension.  # noqa: E501

        Deny list redaction if true, allow list redaction if false.  # noqa: E501

        :return: The deny_list_redaction of this FreeTextRedactionExtension.  # noqa: E501
        :rtype: bool
        """
        return self._deny_list_redaction

    @deny_list_redaction.setter
    def deny_list_redaction(self, deny_list_redaction):
        """Sets the deny_list_redaction of this FreeTextRedactionExtension.

        Deny list redaction if true, allow list redaction if false.  # noqa: E501

        :param deny_list_redaction: The deny_list_redaction of this FreeTextRedactionExtension.  # noqa: E501
        :type: bool
        """

        self._deny_list_redaction = deny_list_redaction

    @property
    def lookup_file_reference_id(self):
        """Gets the lookup_file_reference_id of this FreeTextRedactionExtension.  # noqa: E501

        The reference URI value returned from the endpoint for uploading the lookup file to the Masking Engine.  # noqa: E501

        :return: The lookup_file_reference_id of this FreeTextRedactionExtension.  # noqa: E501
        :rtype: str
        """
        return self._lookup_file_reference_id

    @lookup_file_reference_id.setter
    def lookup_file_reference_id(self, lookup_file_reference_id):
        """Sets the lookup_file_reference_id of this FreeTextRedactionExtension.

        The reference URI value returned from the endpoint for uploading the lookup file to the Masking Engine.  # noqa: E501

        :param lookup_file_reference_id: The lookup_file_reference_id of this FreeTextRedactionExtension.  # noqa: E501
        :type: str
        """

        self._lookup_file_reference_id = lookup_file_reference_id

    @property
    def lookup_redaction_value(self):
        """Gets the lookup_redaction_value of this FreeTextRedactionExtension.  # noqa: E501

        The value to use to redact items matching entries specified in the lookup file.  # noqa: E501

        :return: The lookup_redaction_value of this FreeTextRedactionExtension.  # noqa: E501
        :rtype: str
        """
        return self._lookup_redaction_value

    @lookup_redaction_value.setter
    def lookup_redaction_value(self, lookup_redaction_value):
        """Sets the lookup_redaction_value of this FreeTextRedactionExtension.

        The value to use to redact items matching entries specified in the lookup file.  # noqa: E501

        :param lookup_redaction_value: The lookup_redaction_value of this FreeTextRedactionExtension.  # noqa: E501
        :type: str
        """
        if lookup_redaction_value is not None and len(lookup_redaction_value) > 255:
            raise ValueError("Invalid value for `lookup_redaction_value`, length must be less than or equal to `255`")  # noqa: E501

        self._lookup_redaction_value = lookup_redaction_value

    @property
    def profile_set_id(self):
        """Gets the profile_set_id of this FreeTextRedactionExtension.  # noqa: E501

        The ID number of the profile set for defining the pattern matching to use for identifying values for redaction.  # noqa: E501

        :return: The profile_set_id of this FreeTextRedactionExtension.  # noqa: E501
        :rtype: int
        """
        return self._profile_set_id

    @profile_set_id.setter
    def profile_set_id(self, profile_set_id):
        """Sets the profile_set_id of this FreeTextRedactionExtension.

        The ID number of the profile set for defining the pattern matching to use for identifying values for redaction.  # noqa: E501

        :param profile_set_id: The profile_set_id of this FreeTextRedactionExtension.  # noqa: E501
        :type: int
        """

        self._profile_set_id = profile_set_id

    @property
    def profile_set_redaction_value(self):
        """Gets the profile_set_redaction_value of this FreeTextRedactionExtension.  # noqa: E501

        The value to use to redact items matching patterns defined by the profile set.  # noqa: E501

        :return: The profile_set_redaction_value of this FreeTextRedactionExtension.  # noqa: E501
        :rtype: str
        """
        return self._profile_set_redaction_value

    @profile_set_redaction_value.setter
    def profile_set_redaction_value(self, profile_set_redaction_value):
        """Sets the profile_set_redaction_value of this FreeTextRedactionExtension.

        The value to use to redact items matching patterns defined by the profile set.  # noqa: E501

        :param profile_set_redaction_value: The profile_set_redaction_value of this FreeTextRedactionExtension.  # noqa: E501
        :type: str
        """
        if profile_set_redaction_value is not None and len(profile_set_redaction_value) > 255:
            raise ValueError("Invalid value for `profile_set_redaction_value`, length must be less than or equal to `255`")  # noqa: E501

        self._profile_set_redaction_value = profile_set_redaction_value

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
        if issubclass(FreeTextRedactionExtension, dict):
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
        if not isinstance(other, FreeTextRedactionExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
