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


class Role(object):
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
        'role_id': 'int',
        'role_name': 'str',
        'environment': 'Privilege',
        'connector': 'Privilege',
        'ruleset': 'Privilege',
        'inventory': 'Privilege',
        'profile_job': 'Privilege',
        'masking_job': 'Privilege',
        'tokenize_job': 'Privilege',
        'reidentify_job': 'Privilege',
        'scheduler': 'Privilege',
        'domain': 'Privilege',
        'algorithm': 'Privilege',
        'profile_expression': 'Privilege',
        'profile_set': 'Privilege',
        'file_format': 'Privilege',
        'user': 'Privilege'
    }

    attribute_map = {
        'role_id': 'roleId',
        'role_name': 'roleName',
        'environment': 'environment',
        'connector': 'connector',
        'ruleset': 'ruleset',
        'inventory': 'inventory',
        'profile_job': 'profileJob',
        'masking_job': 'maskingJob',
        'tokenize_job': 'tokenizeJob',
        'reidentify_job': 'reidentifyJob',
        'scheduler': 'scheduler',
        'domain': 'domain',
        'algorithm': 'algorithm',
        'profile_expression': 'profileExpression',
        'profile_set': 'profileSet',
        'file_format': 'fileFormat',
        'user': 'user'
    }

    def __init__(self, role_id=None, role_name=None, environment=None, connector=None, ruleset=None, inventory=None, profile_job=None, masking_job=None, tokenize_job=None, reidentify_job=None, scheduler=None, domain=None, algorithm=None, profile_expression=None, profile_set=None, file_format=None, user=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501

        self._role_id = None
        self._role_name = None
        self._environment = None
        self._connector = None
        self._ruleset = None
        self._inventory = None
        self._profile_job = None
        self._masking_job = None
        self._tokenize_job = None
        self._reidentify_job = None
        self._scheduler = None
        self._domain = None
        self._algorithm = None
        self._profile_expression = None
        self._profile_set = None
        self._file_format = None
        self._user = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        self.role_name = role_name
        if environment is not None:
            self.environment = environment
        if connector is not None:
            self.connector = connector
        if ruleset is not None:
            self.ruleset = ruleset
        if inventory is not None:
            self.inventory = inventory
        if profile_job is not None:
            self.profile_job = profile_job
        if masking_job is not None:
            self.masking_job = masking_job
        if tokenize_job is not None:
            self.tokenize_job = tokenize_job
        if reidentify_job is not None:
            self.reidentify_job = reidentify_job
        if scheduler is not None:
            self.scheduler = scheduler
        if domain is not None:
            self.domain = domain
        if algorithm is not None:
            self.algorithm = algorithm
        if profile_expression is not None:
            self.profile_expression = profile_expression
        if profile_set is not None:
            self.profile_set = profile_set
        if file_format is not None:
            self.file_format = file_format
        if user is not None:
            self.user = user

    @property
    def role_id(self):
        """Gets the role_id of this Role.  # noqa: E501

        The ID of the Role. This field will be generated by the Masking Engine.  # noqa: E501

        :return: The role_id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Role.

        The ID of the Role. This field will be generated by the Masking Engine.  # noqa: E501

        :param role_id: The role_id of this Role.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def role_name(self):
        """Gets the role_name of this Role.  # noqa: E501

        The name for this Role. Note that it must be unique.  # noqa: E501

        :return: The role_name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this Role.

        The name for this Role. Note that it must be unique.  # noqa: E501

        :param role_name: The role_name of this Role.  # noqa: E501
        :type: str
        """
        if role_name is None:
            raise ValueError("Invalid value for `role_name`, must not be `None`")  # noqa: E501
        if role_name is not None and len(role_name) > 255:
            raise ValueError("Invalid value for `role_name`, length must be less than or equal to `255`")  # noqa: E501

        self._role_name = role_name

    @property
    def environment(self):
        """Gets the environment of this Role.  # noqa: E501

        Privileges for environments.  # noqa: E501

        :return: The environment of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Role.

        Privileges for environments.  # noqa: E501

        :param environment: The environment of this Role.  # noqa: E501
        :type: Privilege
        """

        self._environment = environment

    @property
    def connector(self):
        """Gets the connector of this Role.  # noqa: E501

        Privileges for connectors.  # noqa: E501

        :return: The connector of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this Role.

        Privileges for connectors.  # noqa: E501

        :param connector: The connector of this Role.  # noqa: E501
        :type: Privilege
        """

        self._connector = connector

    @property
    def ruleset(self):
        """Gets the ruleset of this Role.  # noqa: E501

        Privileges for rulesets.  # noqa: E501

        :return: The ruleset of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._ruleset

    @ruleset.setter
    def ruleset(self, ruleset):
        """Sets the ruleset of this Role.

        Privileges for rulesets.  # noqa: E501

        :param ruleset: The ruleset of this Role.  # noqa: E501
        :type: Privilege
        """

        self._ruleset = ruleset

    @property
    def inventory(self):
        """Gets the inventory of this Role.  # noqa: E501

        Privileges for inventories.  # noqa: E501

        :return: The inventory of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this Role.

        Privileges for inventories.  # noqa: E501

        :param inventory: The inventory of this Role.  # noqa: E501
        :type: Privilege
        """

        self._inventory = inventory

    @property
    def profile_job(self):
        """Gets the profile_job of this Role.  # noqa: E501

        Privileges for profile jobs.  # noqa: E501

        :return: The profile_job of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._profile_job

    @profile_job.setter
    def profile_job(self, profile_job):
        """Sets the profile_job of this Role.

        Privileges for profile jobs.  # noqa: E501

        :param profile_job: The profile_job of this Role.  # noqa: E501
        :type: Privilege
        """

        self._profile_job = profile_job

    @property
    def masking_job(self):
        """Gets the masking_job of this Role.  # noqa: E501

        Privileges for masking jobs.  # noqa: E501

        :return: The masking_job of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._masking_job

    @masking_job.setter
    def masking_job(self, masking_job):
        """Sets the masking_job of this Role.

        Privileges for masking jobs.  # noqa: E501

        :param masking_job: The masking_job of this Role.  # noqa: E501
        :type: Privilege
        """

        self._masking_job = masking_job

    @property
    def tokenize_job(self):
        """Gets the tokenize_job of this Role.  # noqa: E501

        Privileges for tokenize jobs.  # noqa: E501

        :return: The tokenize_job of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._tokenize_job

    @tokenize_job.setter
    def tokenize_job(self, tokenize_job):
        """Sets the tokenize_job of this Role.

        Privileges for tokenize jobs.  # noqa: E501

        :param tokenize_job: The tokenize_job of this Role.  # noqa: E501
        :type: Privilege
        """

        self._tokenize_job = tokenize_job

    @property
    def reidentify_job(self):
        """Gets the reidentify_job of this Role.  # noqa: E501

        Privileges for re-identify jobs.  # noqa: E501

        :return: The reidentify_job of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._reidentify_job

    @reidentify_job.setter
    def reidentify_job(self, reidentify_job):
        """Sets the reidentify_job of this Role.

        Privileges for re-identify jobs.  # noqa: E501

        :param reidentify_job: The reidentify_job of this Role.  # noqa: E501
        :type: Privilege
        """

        self._reidentify_job = reidentify_job

    @property
    def scheduler(self):
        """Gets the scheduler of this Role.  # noqa: E501

        Privileges for the job scheduler.  # noqa: E501

        :return: The scheduler of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this Role.

        Privileges for the job scheduler.  # noqa: E501

        :param scheduler: The scheduler of this Role.  # noqa: E501
        :type: Privilege
        """

        self._scheduler = scheduler

    @property
    def domain(self):
        """Gets the domain of this Role.  # noqa: E501

        Privileges for domains.  # noqa: E501

        :return: The domain of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Role.

        Privileges for domains.  # noqa: E501

        :param domain: The domain of this Role.  # noqa: E501
        :type: Privilege
        """

        self._domain = domain

    @property
    def algorithm(self):
        """Gets the algorithm of this Role.  # noqa: E501

        Privileges for algorithms.  # noqa: E501

        :return: The algorithm of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this Role.

        Privileges for algorithms.  # noqa: E501

        :param algorithm: The algorithm of this Role.  # noqa: E501
        :type: Privilege
        """

        self._algorithm = algorithm

    @property
    def profile_expression(self):
        """Gets the profile_expression of this Role.  # noqa: E501

        Privileges for profile expressions.  # noqa: E501

        :return: The profile_expression of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._profile_expression

    @profile_expression.setter
    def profile_expression(self, profile_expression):
        """Sets the profile_expression of this Role.

        Privileges for profile expressions.  # noqa: E501

        :param profile_expression: The profile_expression of this Role.  # noqa: E501
        :type: Privilege
        """

        self._profile_expression = profile_expression

    @property
    def profile_set(self):
        """Gets the profile_set of this Role.  # noqa: E501

        Privileges for profile sets.  # noqa: E501

        :return: The profile_set of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._profile_set

    @profile_set.setter
    def profile_set(self, profile_set):
        """Sets the profile_set of this Role.

        Privileges for profile sets.  # noqa: E501

        :param profile_set: The profile_set of this Role.  # noqa: E501
        :type: Privilege
        """

        self._profile_set = profile_set

    @property
    def file_format(self):
        """Gets the file_format of this Role.  # noqa: E501

        Privileges for file formats.  # noqa: E501

        :return: The file_format of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this Role.

        Privileges for file formats.  # noqa: E501

        :param file_format: The file_format of this Role.  # noqa: E501
        :type: Privilege
        """

        self._file_format = file_format

    @property
    def user(self):
        """Gets the user of this Role.  # noqa: E501

        Privileges for users and roles.  # noqa: E501

        :return: The user of this Role.  # noqa: E501
        :rtype: Privilege
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Role.

        Privileges for users and roles.  # noqa: E501

        :param user: The user of this Role.  # noqa: E501
        :type: Privilege
        """

        self._user = user

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
