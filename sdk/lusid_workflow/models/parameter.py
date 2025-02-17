# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.546
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


class Parameter(object):
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
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'required': 'bool',
        'default_value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'required': 'required',
        'default_value': 'defaultValue'
    }

    required_map = {
        'type': 'required',
        'name': 'required',
        'display_name': 'optional',
        'description': 'optional',
        'required': 'required',
        'default_value': 'optional'
    }

    def __init__(self, type=None, name=None, display_name=None, description=None, required=None, default_value=None, local_vars_configuration=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI"
        
        :param type:  The type of this Parameter (required)
        :type type: str
        :param name:  Name (required)
        :type name: str
        :param display_name:  DisplayName
        :type display_name: str
        :param description:  Description
        :type description: str
        :param required:  Required or not (required)
        :type required: bool
        :param default_value:  DefaultValue
        :type default_value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._display_name = None
        self._description = None
        self._required = None
        self._default_value = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.display_name = display_name
        self.description = description
        self.required = required
        self.default_value = default_value

    @property
    def type(self):
        """Gets the type of this Parameter.  # noqa: E501

        The type of this Parameter  # noqa: E501

        :return: The type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.

        The type of this Parameter  # noqa: E501

        :param type: The type of this Parameter.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this Parameter.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        Name  # noqa: E501

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Parameter.  # noqa: E501

        DisplayName  # noqa: E501

        :return: The display_name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Parameter.

        DisplayName  # noqa: E501

        :param display_name: The display_name of this Parameter.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Parameter.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.

        Description  # noqa: E501

        :param description: The description of this Parameter.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this Parameter.  # noqa: E501

        Required or not  # noqa: E501

        :return: The required of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Parameter.

        Required or not  # noqa: E501

        :param required: The required of this Parameter.  # noqa: E501
        :type required: bool
        """
        if self.local_vars_configuration.client_side_validation and required is None:  # noqa: E501
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def default_value(self):
        """Gets the default_value of this Parameter.  # noqa: E501

        DefaultValue  # noqa: E501

        :return: The default_value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Parameter.

        DefaultValue  # noqa: E501

        :param default_value: The default_value of this Parameter.  # noqa: E501
        :type default_value: str
        """

        self._default_value = default_value

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
        if not isinstance(other, Parameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Parameter):
            return True

        return self.to_dict() != other.to_dict()
