# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.362
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class Task(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'id': 'str',
        'correlation_ids': 'list[str]',
        'task_definition_id': 'ResourceId',
        'task_definition_version': 'TaskDefinitionVersion',
        'version': 'VersionInfo',
        'state': 'str',
        'terminal_state': 'bool',
        'as_at_last_transition': 'datetime',
        'fields': 'list[TaskInstanceField]'
    }

    attribute_map = {
        'id': 'id',
        'correlation_ids': 'correlationIds',
        'task_definition_id': 'taskDefinitionId',
        'task_definition_version': 'taskDefinitionVersion',
        'version': 'version',
        'state': 'state',
        'terminal_state': 'terminalState',
        'as_at_last_transition': 'asAtLastTransition',
        'fields': 'fields'
    }

    required_map = {
        'id': 'required',
        'correlation_ids': 'optional',
        'task_definition_id': 'required',
        'task_definition_version': 'required',
        'version': 'optional',
        'state': 'required',
        'terminal_state': 'required',
        'as_at_last_transition': 'optional',
        'fields': 'optional'
    }

    def __init__(self, id=None, correlation_ids=None, task_definition_id=None, task_definition_version=None, version=None, state=None, terminal_state=None, as_at_last_transition=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """Task - a model defined in OpenAPI"
        
        :param id:  The unique id for this Task (required)
        :type id: str
        :param correlation_ids:  User-provided ID used to link entities and tasks
        :type correlation_ids: list[str]
        :param task_definition_id:  (required)
        :type task_definition_id: lusid_workflow.ResourceId
        :param task_definition_version:  (required)
        :type task_definition_version: lusid_workflow.TaskDefinitionVersion
        :param version: 
        :type version: lusid_workflow.VersionInfo
        :param state:  Current State (required)
        :type state: str
        :param terminal_state:  True if no onward transitions are possible (required)
        :type terminal_state: bool
        :param as_at_last_transition:  Last Transition timestamp
        :type as_at_last_transition: datetime
        :param fields:  Fields and their latest values - should correspond with the Task Definition field schema
        :type fields: list[lusid_workflow.TaskInstanceField]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._correlation_ids = None
        self._task_definition_id = None
        self._task_definition_version = None
        self._version = None
        self._state = None
        self._terminal_state = None
        self._as_at_last_transition = None
        self._fields = None
        self.discriminator = None

        self.id = id
        self.correlation_ids = correlation_ids
        self.task_definition_id = task_definition_id
        self.task_definition_version = task_definition_version
        if version is not None:
            self.version = version
        self.state = state
        self.terminal_state = terminal_state
        self.as_at_last_transition = as_at_last_transition
        self.fields = fields

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501

        The unique id for this Task  # noqa: E501

        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        The unique id for this Task  # noqa: E501

        :param id: The id of this Task.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def correlation_ids(self):
        """Gets the correlation_ids of this Task.  # noqa: E501

        User-provided ID used to link entities and tasks  # noqa: E501

        :return: The correlation_ids of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._correlation_ids

    @correlation_ids.setter
    def correlation_ids(self, correlation_ids):
        """Sets the correlation_ids of this Task.

        User-provided ID used to link entities and tasks  # noqa: E501

        :param correlation_ids: The correlation_ids of this Task.  # noqa: E501
        :type correlation_ids: list[str]
        """

        self._correlation_ids = correlation_ids

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this Task.  # noqa: E501


        :return: The task_definition_id of this Task.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this Task.


        :param task_definition_id: The task_definition_id of this Task.  # noqa: E501
        :type task_definition_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and task_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_id`, must not be `None`")  # noqa: E501

        self._task_definition_id = task_definition_id

    @property
    def task_definition_version(self):
        """Gets the task_definition_version of this Task.  # noqa: E501


        :return: The task_definition_version of this Task.  # noqa: E501
        :rtype: lusid_workflow.TaskDefinitionVersion
        """
        return self._task_definition_version

    @task_definition_version.setter
    def task_definition_version(self, task_definition_version):
        """Sets the task_definition_version of this Task.


        :param task_definition_version: The task_definition_version of this Task.  # noqa: E501
        :type task_definition_version: lusid_workflow.TaskDefinitionVersion
        """
        if self.local_vars_configuration.client_side_validation and task_definition_version is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_version`, must not be `None`")  # noqa: E501

        self._task_definition_version = task_definition_version

    @property
    def version(self):
        """Gets the version of this Task.  # noqa: E501


        :return: The version of this Task.  # noqa: E501
        :rtype: lusid_workflow.VersionInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Task.


        :param version: The version of this Task.  # noqa: E501
        :type version: lusid_workflow.VersionInfo
        """

        self._version = version

    @property
    def state(self):
        """Gets the state of this Task.  # noqa: E501

        Current State  # noqa: E501

        :return: The state of this Task.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Task.

        Current State  # noqa: E501

        :param state: The state of this Task.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 1):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

    @property
    def terminal_state(self):
        """Gets the terminal_state of this Task.  # noqa: E501

        True if no onward transitions are possible  # noqa: E501

        :return: The terminal_state of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._terminal_state

    @terminal_state.setter
    def terminal_state(self, terminal_state):
        """Sets the terminal_state of this Task.

        True if no onward transitions are possible  # noqa: E501

        :param terminal_state: The terminal_state of this Task.  # noqa: E501
        :type terminal_state: bool
        """
        if self.local_vars_configuration.client_side_validation and terminal_state is None:  # noqa: E501
            raise ValueError("Invalid value for `terminal_state`, must not be `None`")  # noqa: E501

        self._terminal_state = terminal_state

    @property
    def as_at_last_transition(self):
        """Gets the as_at_last_transition of this Task.  # noqa: E501

        Last Transition timestamp  # noqa: E501

        :return: The as_at_last_transition of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_last_transition

    @as_at_last_transition.setter
    def as_at_last_transition(self, as_at_last_transition):
        """Sets the as_at_last_transition of this Task.

        Last Transition timestamp  # noqa: E501

        :param as_at_last_transition: The as_at_last_transition of this Task.  # noqa: E501
        :type as_at_last_transition: datetime
        """

        self._as_at_last_transition = as_at_last_transition

    @property
    def fields(self):
        """Gets the fields of this Task.  # noqa: E501

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :return: The fields of this Task.  # noqa: E501
        :rtype: list[lusid_workflow.TaskInstanceField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Task.

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :param fields: The fields of this Task.  # noqa: E501
        :type fields: list[lusid_workflow.TaskInstanceField]
        """

        self._fields = fields

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Task):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Task):
            return True

        return self.to_dict() != other.to_dict()
