# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.129
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


class TriggerSchema(object):
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
        'type': 'str',
        'time_in_state': 'int',
        'response_codes': 'dict(str, list[int])'
    }

    attribute_map = {
        'type': 'type',
        'time_in_state': 'timeInState',
        'response_codes': 'responseCodes'
    }

    required_map = {
        'type': 'optional',
        'time_in_state': 'optional',
        'response_codes': 'optional'
    }

    def __init__(self, type=None, time_in_state=None, response_codes=None, local_vars_configuration=None):  # noqa: E501
        """TriggerSchema - a model defined in OpenAPI"
        
        :param type:  The type of Trigger: Manual, Timeout or WebHook
        :type type: str
        :param time_in_state:  The amount of time to wait in seconds (Timeout only)
        :type time_in_state: int
        :param response_codes:  Defines a set of HTTP response codes that correspond to an outcome. eg: 'OK =>  ['200', '204'] (WebHook only)
        :type response_codes: dict(str, list[int])

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._time_in_state = None
        self._response_codes = None
        self.discriminator = None

        self.type = type
        if time_in_state is not None:
            self.time_in_state = time_in_state
        self.response_codes = response_codes

    @property
    def type(self):
        """Gets the type of this TriggerSchema.  # noqa: E501

        The type of Trigger: Manual, Timeout or WebHook  # noqa: E501

        :return: The type of this TriggerSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TriggerSchema.

        The type of Trigger: Manual, Timeout or WebHook  # noqa: E501

        :param type: The type of this TriggerSchema.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def time_in_state(self):
        """Gets the time_in_state of this TriggerSchema.  # noqa: E501

        The amount of time to wait in seconds (Timeout only)  # noqa: E501

        :return: The time_in_state of this TriggerSchema.  # noqa: E501
        :rtype: int
        """
        return self._time_in_state

    @time_in_state.setter
    def time_in_state(self, time_in_state):
        """Sets the time_in_state of this TriggerSchema.

        The amount of time to wait in seconds (Timeout only)  # noqa: E501

        :param time_in_state: The time_in_state of this TriggerSchema.  # noqa: E501
        :type time_in_state: int
        """

        self._time_in_state = time_in_state

    @property
    def response_codes(self):
        """Gets the response_codes of this TriggerSchema.  # noqa: E501

        Defines a set of HTTP response codes that correspond to an outcome. eg: 'OK =>  ['200', '204'] (WebHook only)  # noqa: E501

        :return: The response_codes of this TriggerSchema.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._response_codes

    @response_codes.setter
    def response_codes(self, response_codes):
        """Sets the response_codes of this TriggerSchema.

        Defines a set of HTTP response codes that correspond to an outcome. eg: 'OK =>  ['200', '204'] (WebHook only)  # noqa: E501

        :param response_codes: The response_codes of this TriggerSchema.  # noqa: E501
        :type response_codes: dict(str, list[int])
        """

        self._response_codes = response_codes

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
        if not isinstance(other, TriggerSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TriggerSchema):
            return True

        return self.to_dict() != other.to_dict()
