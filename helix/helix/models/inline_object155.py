# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from helix.configuration import Configuration


class InlineObject155(object):
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
    """
    openapi_types = {
        'list': 'str',
        'notes': 'str',
        'type': 'str',
        'risk': 'str',
        'value': 'str'
    }

    attribute_map = {
        'list': 'list',
        'notes': 'notes',
        'type': 'type',
        'risk': 'risk',
        'value': 'value'
    }

    def __init__(self, list=None, notes=None, type=None, risk=None, value=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject155 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list = None
        self._notes = None
        self._type = None
        self._risk = None
        self._value = None
        self.discriminator = None

        self.list = list
        if notes is not None:
            self.notes = notes
        self.type = type
        if risk is not None:
            self.risk = risk
        self.value = value

    @property
    def list(self):
        """Gets the list of this InlineObject155.  # noqa: E501

          # noqa: E501

        :return: The list of this InlineObject155.  # noqa: E501
        :rtype: str
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InlineObject155.

          # noqa: E501

        :param list: The list of this InlineObject155.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and list is None:  # noqa: E501
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

    @property
    def notes(self):
        """Gets the notes of this InlineObject155.  # noqa: E501

          # noqa: E501

        :return: The notes of this InlineObject155.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InlineObject155.

          # noqa: E501

        :param notes: The notes of this InlineObject155.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def type(self):
        """Gets the type of this InlineObject155.  # noqa: E501

          # noqa: E501

        :return: The type of this InlineObject155.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject155.

          # noqa: E501

        :param type: The type of this InlineObject155.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def risk(self):
        """Gets the risk of this InlineObject155.  # noqa: E501

          # noqa: E501

        :return: The risk of this InlineObject155.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this InlineObject155.

          # noqa: E501

        :param risk: The risk of this InlineObject155.  # noqa: E501
        :type: str
        """

        self._risk = risk

    @property
    def value(self):
        """Gets the value of this InlineObject155.  # noqa: E501

          # noqa: E501

        :return: The value of this InlineObject155.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineObject155.

          # noqa: E501

        :param value: The value of this InlineObject155.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject155):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject155):
            return True

        return self.to_dict() != other.to_dict()
