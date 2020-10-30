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


class ReidentificationJob(object):
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
        'reidentification_job_id': 'int',
        'job_name': 'str',
        'ruleset_id': 'int',
        'ruleset_type': 'str',
        'created_by': 'str',
        'created_time': 'datetime',
        'email': 'str',
        'feedback_size': 'int',
        'job_description': 'str',
        'max_memory': 'int',
        'min_memory': 'int',
        'multi_tenant': 'bool',
        'num_input_streams': 'int',
        'on_the_fly_masking': 'bool',
        'database_masking_options': 'DatabaseMaskingOptions',
        'on_the_fly_masking_source': 'OnTheFlyMaskingSource',
        'fail_immediately': 'bool',
        'stream_row_limit': 'int'
    }

    attribute_map = {
        'reidentification_job_id': 'reidentificationJobId',
        'job_name': 'jobName',
        'ruleset_id': 'rulesetId',
        'ruleset_type': 'rulesetType',
        'created_by': 'createdBy',
        'created_time': 'createdTime',
        'email': 'email',
        'feedback_size': 'feedbackSize',
        'job_description': 'jobDescription',
        'max_memory': 'maxMemory',
        'min_memory': 'minMemory',
        'multi_tenant': 'multiTenant',
        'num_input_streams': 'numInputStreams',
        'on_the_fly_masking': 'onTheFlyMasking',
        'database_masking_options': 'databaseMaskingOptions',
        'on_the_fly_masking_source': 'onTheFlyMaskingSource',
        'fail_immediately': 'failImmediately',
        'stream_row_limit': 'streamRowLimit'
    }

    def __init__(self, reidentification_job_id=None, job_name=None, ruleset_id=None, ruleset_type=None, created_by=None, created_time=None, email=None, feedback_size=None, job_description=None, max_memory=None, min_memory=None, multi_tenant=False, num_input_streams=1, on_the_fly_masking=False, database_masking_options=None, on_the_fly_masking_source=None, fail_immediately=False, stream_row_limit=None):  # noqa: E501
        """ReidentificationJob - a model defined in Swagger"""  # noqa: E501

        self._reidentification_job_id = None
        self._job_name = None
        self._ruleset_id = None
        self._ruleset_type = None
        self._created_by = None
        self._created_time = None
        self._email = None
        self._feedback_size = None
        self._job_description = None
        self._max_memory = None
        self._min_memory = None
        self._multi_tenant = None
        self._num_input_streams = None
        self._on_the_fly_masking = None
        self._database_masking_options = None
        self._on_the_fly_masking_source = None
        self._fail_immediately = None
        self._stream_row_limit = None
        self.discriminator = None

        if reidentification_job_id is not None:
            self.reidentification_job_id = reidentification_job_id
        self.job_name = job_name
        self.ruleset_id = ruleset_id
        if ruleset_type is not None:
            self.ruleset_type = ruleset_type
        if created_by is not None:
            self.created_by = created_by
        if created_time is not None:
            self.created_time = created_time
        if email is not None:
            self.email = email
        if feedback_size is not None:
            self.feedback_size = feedback_size
        if job_description is not None:
            self.job_description = job_description
        if max_memory is not None:
            self.max_memory = max_memory
        if min_memory is not None:
            self.min_memory = min_memory
        if multi_tenant is not None:
            self.multi_tenant = multi_tenant
        if num_input_streams is not None:
            self.num_input_streams = num_input_streams
        if on_the_fly_masking is not None:
            self.on_the_fly_masking = on_the_fly_masking
        if database_masking_options is not None:
            self.database_masking_options = database_masking_options
        if on_the_fly_masking_source is not None:
            self.on_the_fly_masking_source = on_the_fly_masking_source
        if fail_immediately is not None:
            self.fail_immediately = fail_immediately
        if stream_row_limit is not None:
            self.stream_row_limit = stream_row_limit

    @property
    def reidentification_job_id(self):
        """Gets the reidentification_job_id of this ReidentificationJob.  # noqa: E501

        The ID number of the re-identification job. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The reidentification_job_id of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._reidentification_job_id

    @reidentification_job_id.setter
    def reidentification_job_id(self, reidentification_job_id):
        """Sets the reidentification_job_id of this ReidentificationJob.

        The ID number of the re-identification job. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param reidentification_job_id: The reidentification_job_id of this ReidentificationJob.  # noqa: E501
        :type: int
        """

        self._reidentification_job_id = reidentification_job_id

    @property
    def job_name(self):
        """Gets the job_name of this ReidentificationJob.  # noqa: E501

        The name of the re-identification job. Once the re-identification job is created, this field cannot be changed.  # noqa: E501

        :return: The job_name of this ReidentificationJob.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ReidentificationJob.

        The name of the re-identification job. Once the re-identification job is created, this field cannot be changed.  # noqa: E501

        :param job_name: The job_name of this ReidentificationJob.  # noqa: E501
        :type: str
        """
        if job_name is None:
            raise ValueError("Invalid value for `job_name`, must not be `None`")  # noqa: E501
        if job_name is not None and len(job_name) > 50:
            raise ValueError("Invalid value for `job_name`, length must be less than or equal to `50`")  # noqa: E501

        self._job_name = job_name

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this ReidentificationJob.  # noqa: E501

        The ID of the ruleset that this re-identification job is based on. Once the re-identification job is created, the underlying environment that is inferred from the ruleset will be unchangeable. That is, the job can only be updated to reference a ruleset that is in the same environment as the environment of the original ruleset.  # noqa: E501

        :return: The ruleset_id of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this ReidentificationJob.

        The ID of the ruleset that this re-identification job is based on. Once the re-identification job is created, the underlying environment that is inferred from the ruleset will be unchangeable. That is, the job can only be updated to reference a ruleset that is in the same environment as the environment of the original ruleset.  # noqa: E501

        :param ruleset_id: The ruleset_id of this ReidentificationJob.  # noqa: E501
        :type: int
        """
        if ruleset_id is None:
            raise ValueError("Invalid value for `ruleset_id`, must not be `None`")  # noqa: E501

        self._ruleset_id = ruleset_id

    @property
    def ruleset_type(self):
        """Gets the ruleset_type of this ReidentificationJob.  # noqa: E501

        The type of the ruleset that this re-identification job is assigned to.  # noqa: E501

        :return: The ruleset_type of this ReidentificationJob.  # noqa: E501
        :rtype: str
        """
        return self._ruleset_type

    @ruleset_type.setter
    def ruleset_type(self, ruleset_type):
        """Sets the ruleset_type of this ReidentificationJob.

        The type of the ruleset that this re-identification job is assigned to.  # noqa: E501

        :param ruleset_type: The ruleset_type of this ReidentificationJob.  # noqa: E501
        :type: str
        """

        self._ruleset_type = ruleset_type

    @property
    def created_by(self):
        """Gets the created_by of this ReidentificationJob.  # noqa: E501

        The user that created the re-identification job. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The created_by of this ReidentificationJob.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ReidentificationJob.

        The user that created the re-identification job. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param created_by: The created_by of this ReidentificationJob.  # noqa: E501
        :type: str
        """
        if created_by is not None and len(created_by) > 255:
            raise ValueError("Invalid value for `created_by`, length must be less than or equal to `255`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_time(self):
        """Gets the created_time of this ReidentificationJob.  # noqa: E501

        The time when the re-identification job was created. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The created_time of this ReidentificationJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ReidentificationJob.

        The time when the re-identification job was created. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param created_time: The created_time of this ReidentificationJob.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def email(self):
        """Gets the email of this ReidentificationJob.  # noqa: E501

        The email address to send job status notifications to; note that the SMTP settings must be configured first to receive notifications.  # noqa: E501

        :return: The email of this ReidentificationJob.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ReidentificationJob.

        The email address to send job status notifications to; note that the SMTP settings must be configured first to receive notifications.  # noqa: E501

        :param email: The email of this ReidentificationJob.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def feedback_size(self):
        """Gets the feedback_size of this ReidentificationJob.  # noqa: E501

        The granularity with which the Masking Engine provides updates on the progress of the re-identification job. For instance, a feedbackSize of 50000 results in log updates whenever 50000 rows are processed during the masking phase.  # noqa: E501

        :return: The feedback_size of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._feedback_size

    @feedback_size.setter
    def feedback_size(self, feedback_size):
        """Sets the feedback_size of this ReidentificationJob.

        The granularity with which the Masking Engine provides updates on the progress of the re-identification job. For instance, a feedbackSize of 50000 results in log updates whenever 50000 rows are processed during the masking phase.  # noqa: E501

        :param feedback_size: The feedback_size of this ReidentificationJob.  # noqa: E501
        :type: int
        """
        if feedback_size is not None and feedback_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `feedback_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._feedback_size = feedback_size

    @property
    def job_description(self):
        """Gets the job_description of this ReidentificationJob.  # noqa: E501

        A description of the job.  # noqa: E501

        :return: The job_description of this ReidentificationJob.  # noqa: E501
        :rtype: str
        """
        return self._job_description

    @job_description.setter
    def job_description(self, job_description):
        """Sets the job_description of this ReidentificationJob.

        A description of the job.  # noqa: E501

        :param job_description: The job_description of this ReidentificationJob.  # noqa: E501
        :type: str
        """
        if job_description is not None and len(job_description) > 255:
            raise ValueError("Invalid value for `job_description`, length must be less than or equal to `255`")  # noqa: E501

        self._job_description = job_description

    @property
    def max_memory(self):
        """Gets the max_memory of this ReidentificationJob.  # noqa: E501

        The maximum amount of memory, in MB, that the re-identification job can consume during execution.  # noqa: E501

        :return: The max_memory of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this ReidentificationJob.

        The maximum amount of memory, in MB, that the re-identification job can consume during execution.  # noqa: E501

        :param max_memory: The max_memory of this ReidentificationJob.  # noqa: E501
        :type: int
        """

        self._max_memory = max_memory

    @property
    def min_memory(self):
        """Gets the min_memory of this ReidentificationJob.  # noqa: E501

        The minimum amount of memory, in MB, that the re-identification job can consume during execution.  # noqa: E501

        :return: The min_memory of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._min_memory

    @min_memory.setter
    def min_memory(self, min_memory):
        """Sets the min_memory of this ReidentificationJob.

        The minimum amount of memory, in MB, that the re-identification job can consume during execution.  # noqa: E501

        :param min_memory: The min_memory of this ReidentificationJob.  # noqa: E501
        :type: int
        """

        self._min_memory = min_memory

    @property
    def multi_tenant(self):
        """Gets the multi_tenant of this ReidentificationJob.  # noqa: E501

        This field determines whether the re-identification job, after creation, can be executed using a connector that is different from the underlying connector associated with the ruleset that this re-identification job is based on.  # noqa: E501

        :return: The multi_tenant of this ReidentificationJob.  # noqa: E501
        :rtype: bool
        """
        return self._multi_tenant

    @multi_tenant.setter
    def multi_tenant(self, multi_tenant):
        """Sets the multi_tenant of this ReidentificationJob.

        This field determines whether the re-identification job, after creation, can be executed using a connector that is different from the underlying connector associated with the ruleset that this re-identification job is based on.  # noqa: E501

        :param multi_tenant: The multi_tenant of this ReidentificationJob.  # noqa: E501
        :type: bool
        """

        self._multi_tenant = multi_tenant

    @property
    def num_input_streams(self):
        """Gets the num_input_streams of this ReidentificationJob.  # noqa: E501

        This field controls the amount of parallelism that the re-identification job uses to extract out the data to be masked. For instance, when masking a database, specifying 5 input streams results in the re-identification job reading up to 5 database tables in parallel and then masking those 5 streams of data in parallel. The higher the value of this field, the more potential parallelism there will be in the job, but the re-identification job will consume more memory. If the number of input streams exceeds the number of units being masked (e.g. tables or files), then the excess streams will do nothing.  # noqa: E501

        :return: The num_input_streams of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._num_input_streams

    @num_input_streams.setter
    def num_input_streams(self, num_input_streams):
        """Sets the num_input_streams of this ReidentificationJob.

        This field controls the amount of parallelism that the re-identification job uses to extract out the data to be masked. For instance, when masking a database, specifying 5 input streams results in the re-identification job reading up to 5 database tables in parallel and then masking those 5 streams of data in parallel. The higher the value of this field, the more potential parallelism there will be in the job, but the re-identification job will consume more memory. If the number of input streams exceeds the number of units being masked (e.g. tables or files), then the excess streams will do nothing.  # noqa: E501

        :param num_input_streams: The num_input_streams of this ReidentificationJob.  # noqa: E501
        :type: int
        """
        if num_input_streams is not None and num_input_streams < 1:  # noqa: E501
            raise ValueError("Invalid value for `num_input_streams`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_input_streams = num_input_streams

    @property
    def on_the_fly_masking(self):
        """Gets the on_the_fly_masking of this ReidentificationJob.  # noqa: E501

        This field determines whether the re-identification job will be performed InPlace or OnTheFly. The process for InPlace masking is to read out the data to be masked, mask the data, and then load the masked data back into the original data source. The process for OnTheFly masking is to read out the data to be masked, mask the data, and then load the masked data back into a different data source. When masking OnTheFly, the field 'onTheFlyMaskingSource' must be provided.  # noqa: E501

        :return: The on_the_fly_masking of this ReidentificationJob.  # noqa: E501
        :rtype: bool
        """
        return self._on_the_fly_masking

    @on_the_fly_masking.setter
    def on_the_fly_masking(self, on_the_fly_masking):
        """Sets the on_the_fly_masking of this ReidentificationJob.

        This field determines whether the re-identification job will be performed InPlace or OnTheFly. The process for InPlace masking is to read out the data to be masked, mask the data, and then load the masked data back into the original data source. The process for OnTheFly masking is to read out the data to be masked, mask the data, and then load the masked data back into a different data source. When masking OnTheFly, the field 'onTheFlyMaskingSource' must be provided.  # noqa: E501

        :param on_the_fly_masking: The on_the_fly_masking of this ReidentificationJob.  # noqa: E501
        :type: bool
        """

        self._on_the_fly_masking = on_the_fly_masking

    @property
    def database_masking_options(self):
        """Gets the database_masking_options of this ReidentificationJob.  # noqa: E501

        This field only applies when masking a database, and it can be used to specify various database options to optimize the masking job. Not all database options are supported for all database types.  # noqa: E501

        :return: The database_masking_options of this ReidentificationJob.  # noqa: E501
        :rtype: DatabaseMaskingOptions
        """
        return self._database_masking_options

    @database_masking_options.setter
    def database_masking_options(self, database_masking_options):
        """Sets the database_masking_options of this ReidentificationJob.

        This field only applies when masking a database, and it can be used to specify various database options to optimize the masking job. Not all database options are supported for all database types.  # noqa: E501

        :param database_masking_options: The database_masking_options of this ReidentificationJob.  # noqa: E501
        :type: DatabaseMaskingOptions
        """

        self._database_masking_options = database_masking_options

    @property
    def on_the_fly_masking_source(self):
        """Gets the on_the_fly_masking_source of this ReidentificationJob.  # noqa: E501

        This field is required when the re-identification job is performed OnTheFly; it describes the source connection from where the data to be masked will be extracted.  # noqa: E501

        :return: The on_the_fly_masking_source of this ReidentificationJob.  # noqa: E501
        :rtype: OnTheFlyMaskingSource
        """
        return self._on_the_fly_masking_source

    @on_the_fly_masking_source.setter
    def on_the_fly_masking_source(self, on_the_fly_masking_source):
        """Sets the on_the_fly_masking_source of this ReidentificationJob.

        This field is required when the re-identification job is performed OnTheFly; it describes the source connection from where the data to be masked will be extracted.  # noqa: E501

        :param on_the_fly_masking_source: The on_the_fly_masking_source of this ReidentificationJob.  # noqa: E501
        :type: OnTheFlyMaskingSource
        """

        self._on_the_fly_masking_source = on_the_fly_masking_source

    @property
    def fail_immediately(self):
        """Gets the fail_immediately of this ReidentificationJob.  # noqa: E501

        This field determines whether the masking job will fail immediately or delay failure until job completion when a masking algorithm fails to mask its data. Setting this value to 'false' provides a means for a user to see all cumulative masking errors before the job is marked as failed.  # noqa: E501

        :return: The fail_immediately of this ReidentificationJob.  # noqa: E501
        :rtype: bool
        """
        return self._fail_immediately

    @fail_immediately.setter
    def fail_immediately(self, fail_immediately):
        """Sets the fail_immediately of this ReidentificationJob.

        This field determines whether the masking job will fail immediately or delay failure until job completion when a masking algorithm fails to mask its data. Setting this value to 'false' provides a means for a user to see all cumulative masking errors before the job is marked as failed.  # noqa: E501

        :param fail_immediately: The fail_immediately of this ReidentificationJob.  # noqa: E501
        :type: bool
        """

        self._fail_immediately = fail_immediately

    @property
    def stream_row_limit(self):
        """Gets the stream_row_limit of this ReidentificationJob.  # noqa: E501

        This value constrains the total number of rows that may enter the job for each masking stream. A setting of 0 means unlimited. A value of -1 selects the default value. The default value for this setting varies by job type. The minimum explicit value allowed is 20  # noqa: E501

        :return: The stream_row_limit of this ReidentificationJob.  # noqa: E501
        :rtype: int
        """
        return self._stream_row_limit

    @stream_row_limit.setter
    def stream_row_limit(self, stream_row_limit):
        """Sets the stream_row_limit of this ReidentificationJob.

        This value constrains the total number of rows that may enter the job for each masking stream. A setting of 0 means unlimited. A value of -1 selects the default value. The default value for this setting varies by job type. The minimum explicit value allowed is 20  # noqa: E501

        :param stream_row_limit: The stream_row_limit of this ReidentificationJob.  # noqa: E501
        :type: int
        """
        if stream_row_limit is not None and stream_row_limit < -1:  # noqa: E501
            raise ValueError("Invalid value for `stream_row_limit`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._stream_row_limit = stream_row_limit

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
        if issubclass(ReidentificationJob, dict):
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
        if not isinstance(other, ReidentificationJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
