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


class KnowledgeBaseInfo(object):
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
        'knowledge_base_info_id': 'int',
        'title': 'str',
        'link': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'knowledge_base_info_id': 'knowledgeBaseInfoId',
        'title': 'title',
        'link': 'link',
        'tag': 'tag'
    }

    def __init__(self, knowledge_base_info_id=None, title=None, link=None, tag=None):  # noqa: E501
        """KnowledgeBaseInfo - a model defined in Swagger"""  # noqa: E501

        self._knowledge_base_info_id = None
        self._title = None
        self._link = None
        self._tag = None
        self.discriminator = None

        if knowledge_base_info_id is not None:
            self.knowledge_base_info_id = knowledge_base_info_id
        if title is not None:
            self.title = title
        if link is not None:
            self.link = link
        if tag is not None:
            self.tag = tag

    @property
    def knowledge_base_info_id(self):
        """Gets the knowledge_base_info_id of this KnowledgeBaseInfo.  # noqa: E501

        The ID of the knowledge base entry.  # noqa: E501

        :return: The knowledge_base_info_id of this KnowledgeBaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._knowledge_base_info_id

    @knowledge_base_info_id.setter
    def knowledge_base_info_id(self, knowledge_base_info_id):
        """Sets the knowledge_base_info_id of this KnowledgeBaseInfo.

        The ID of the knowledge base entry.  # noqa: E501

        :param knowledge_base_info_id: The knowledge_base_info_id of this KnowledgeBaseInfo.  # noqa: E501
        :type: int
        """

        self._knowledge_base_info_id = knowledge_base_info_id

    @property
    def title(self):
        """Gets the title of this KnowledgeBaseInfo.  # noqa: E501

        The title for the knowledge base entry.  # noqa: E501

        :return: The title of this KnowledgeBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this KnowledgeBaseInfo.

        The title for the knowledge base entry.  # noqa: E501

        :param title: The title of this KnowledgeBaseInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def link(self):
        """Gets the link of this KnowledgeBaseInfo.  # noqa: E501

        The link to the information in the knowledge base.  # noqa: E501

        :return: The link of this KnowledgeBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this KnowledgeBaseInfo.

        The link to the information in the knowledge base.  # noqa: E501

        :param link: The link of this KnowledgeBaseInfo.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def tag(self):
        """Gets the tag of this KnowledgeBaseInfo.  # noqa: E501

        The lookup tag associated with the information in the knowledge base.  # noqa: E501

        :return: The tag of this KnowledgeBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this KnowledgeBaseInfo.

        The lookup tag associated with the information in the knowledge base.  # noqa: E501

        :param tag: The tag of this KnowledgeBaseInfo.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if issubclass(KnowledgeBaseInfo, dict):
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
        if not isinstance(other, KnowledgeBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other