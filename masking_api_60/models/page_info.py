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


class PageInfo(object):
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
        'number_on_page': 'int',
        'total': 'int'
    }

    attribute_map = {
        'number_on_page': 'numberOnPage',
        'total': 'total'
    }

    def __init__(self, number_on_page=None, total=None):  # noqa: E501
        """PageInfo - a model defined in Swagger"""  # noqa: E501

        self._number_on_page = None
        self._total = None
        self.discriminator = None

        if number_on_page is not None:
            self.number_on_page = number_on_page
        if total is not None:
            self.total = total

    @property
    def number_on_page(self):
        """Gets the number_on_page of this PageInfo.  # noqa: E501

        The number of items on this page. This should always match the page size unless it is the last page.  # noqa: E501

        :return: The number_on_page of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_on_page

    @number_on_page.setter
    def number_on_page(self, number_on_page):
        """Sets the number_on_page of this PageInfo.

        The number of items on this page. This should always match the page size unless it is the last page.  # noqa: E501

        :param number_on_page: The number_on_page of this PageInfo.  # noqa: E501
        :type: int
        """

        self._number_on_page = number_on_page

    @property
    def total(self):
        """Gets the total of this PageInfo.  # noqa: E501

        The total number of items  # noqa: E501

        :return: The total of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PageInfo.

        The total number of items  # noqa: E501

        :param total: The total of this PageInfo.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(PageInfo, dict):
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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
