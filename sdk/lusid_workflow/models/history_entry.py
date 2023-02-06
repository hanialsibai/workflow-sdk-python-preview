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


class HistoryEntry(object):
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
        'time_stamp': 'datetime',
        'entry': 'str'
    }

    attribute_map = {
        'time_stamp': 'timeStamp',
        'entry': 'entry'
    }

    required_map = {
        'time_stamp': 'optional',
        'entry': 'optional'
    }

    def __init__(self, time_stamp=None, entry=None, local_vars_configuration=None):  # noqa: E501
        """HistoryEntry - a model defined in OpenAPI"
        
        :param time_stamp:  The timestamp for the entry
        :type time_stamp: datetime
        :param entry:  The information itself
        :type entry: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._time_stamp = None
        self._entry = None
        self.discriminator = None

        if time_stamp is not None:
            self.time_stamp = time_stamp
        self.entry = entry

    @property
    def time_stamp(self):
        """Gets the time_stamp of this HistoryEntry.  # noqa: E501

        The timestamp for the entry  # noqa: E501

        :return: The time_stamp of this HistoryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this HistoryEntry.

        The timestamp for the entry  # noqa: E501

        :param time_stamp: The time_stamp of this HistoryEntry.  # noqa: E501
        :type time_stamp: datetime
        """

        self._time_stamp = time_stamp

    @property
    def entry(self):
        """Gets the entry of this HistoryEntry.  # noqa: E501

        The information itself  # noqa: E501

        :return: The entry of this HistoryEntry.  # noqa: E501
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this HistoryEntry.

        The information itself  # noqa: E501

        :param entry: The entry of this HistoryEntry.  # noqa: E501
        :type entry: str
        """

        self._entry = entry

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
        if not isinstance(other, HistoryEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoryEntry):
            return True

        return self.to_dict() != other.to_dict()
