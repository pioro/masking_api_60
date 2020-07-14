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


class Privilege(object):
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
        'copy': 'bool',
        'create': 'bool',
        'delete': 'bool',
        'export': 'bool',
        '_import': 'bool',
        'run': 'bool',
        'update': 'bool',
        'view': 'bool'
    }

    attribute_map = {
        'copy': 'copy',
        'create': 'create',
        'delete': 'delete',
        'export': 'export',
        '_import': 'import',
        'run': 'run',
        'update': 'update',
        'view': 'view'
    }

    def __init__(self, copy=False, create=False, delete=False, export=False, _import=False, run=False, update=False, view=False):  # noqa: E501
        """Privilege - a model defined in Swagger"""  # noqa: E501

        self._copy = None
        self._create = None
        self._delete = None
        self._export = None
        self.__import = None
        self._run = None
        self._update = None
        self._view = None
        self.discriminator = None

        if copy is not None:
            self.copy = copy
        if create is not None:
            self.create = create
        if delete is not None:
            self.delete = delete
        if export is not None:
            self.export = export
        if _import is not None:
            self._import = _import
        if run is not None:
            self.run = run
        if update is not None:
            self.update = update
        if view is not None:
            self.view = view

    @property
    def copy(self):
        """Gets the copy of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to copy the object it is applied to.  # noqa: E501

        :return: The copy of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """Sets the copy of this Privilege.

        This field indicates whether or not this privilege has the ability to copy the object it is applied to.  # noqa: E501

        :param copy: The copy of this Privilege.  # noqa: E501
        :type: bool
        """

        self._copy = copy

    @property
    def create(self):
        """Gets the create of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to create the object it is applied to.  # noqa: E501

        :return: The create of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this Privilege.

        This field indicates whether or not this privilege has the ability to create the object it is applied to.  # noqa: E501

        :param create: The create of this Privilege.  # noqa: E501
        :type: bool
        """

        self._create = create

    @property
    def delete(self):
        """Gets the delete of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to delete the object it is applied to.  # noqa: E501

        :return: The delete of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this Privilege.

        This field indicates whether or not this privilege has the ability to delete the object it is applied to.  # noqa: E501

        :param delete: The delete of this Privilege.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def export(self):
        """Gets the export of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to export the object it is applied to.  # noqa: E501

        :return: The export of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._export

    @export.setter
    def export(self, export):
        """Sets the export of this Privilege.

        This field indicates whether or not this privilege has the ability to export the object it is applied to.  # noqa: E501

        :param export: The export of this Privilege.  # noqa: E501
        :type: bool
        """

        self._export = export

    @property
    def _import(self):
        """Gets the _import of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to import the object it is applied to.  # noqa: E501

        :return: The _import of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self.__import

    @_import.setter
    def _import(self, _import):
        """Sets the _import of this Privilege.

        This field indicates whether or not this privilege has the ability to import the object it is applied to.  # noqa: E501

        :param _import: The _import of this Privilege.  # noqa: E501
        :type: bool
        """

        self.__import = _import

    @property
    def run(self):
        """Gets the run of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to run the object it is applied to.  # noqa: E501

        :return: The run of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this Privilege.

        This field indicates whether or not this privilege has the ability to run the object it is applied to.  # noqa: E501

        :param run: The run of this Privilege.  # noqa: E501
        :type: bool
        """

        self._run = run

    @property
    def update(self):
        """Gets the update of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to update the object it is applied to.  # noqa: E501

        :return: The update of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this Privilege.

        This field indicates whether or not this privilege has the ability to update the object it is applied to.  # noqa: E501

        :param update: The update of this Privilege.  # noqa: E501
        :type: bool
        """

        self._update = update

    @property
    def view(self):
        """Gets the view of this Privilege.  # noqa: E501

        This field indicates whether or not this privilege has the ability to view the object it is applied to.  # noqa: E501

        :return: The view of this Privilege.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this Privilege.

        This field indicates whether or not this privilege has the ability to view the object it is applied to.  # noqa: E501

        :param view: The view of this Privilege.  # noqa: E501
        :type: bool
        """

        self._view = view

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
        if issubclass(Privilege, dict):
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
        if not isinstance(other, Privilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other