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


class InlineObject153(object):
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
        'name': 'str',
        'short_name': 'str',
        'is_internal': 'bool',
        'is_active': 'bool',
        'is_protected': 'bool',
        'usage': 'list[str]',
        'is_hidden': 'bool',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'short_name': 'short_name',
        'is_internal': 'is_internal',
        'is_active': 'is_active',
        'is_protected': 'is_protected',
        'usage': 'usage',
        'is_hidden': 'is_hidden',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, short_name=None, is_internal=None, is_active=None, is_protected=None, usage=None, is_hidden=None, type=None, description=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject153 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._short_name = None
        self._is_internal = None
        self._is_active = None
        self._is_protected = None
        self._usage = None
        self._is_hidden = None
        self._type = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if is_internal is not None:
            self.is_internal = is_internal
        if is_active is not None:
            self.is_active = is_active
        if is_protected is not None:
            self.is_protected = is_protected
        if usage is not None:
            self.usage = usage
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject153.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject153.

          # noqa: E501

        :param name: The name of this InlineObject153.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The short_name of this InlineObject153.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this InlineObject153.

          # noqa: E501

        :param short_name: The short_name of this InlineObject153.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def is_internal(self):
        """Gets the is_internal of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The is_internal of this InlineObject153.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this InlineObject153.

          # noqa: E501

        :param is_internal: The is_internal of this InlineObject153.  # noqa: E501
        :type: bool
        """

        self._is_internal = is_internal

    @property
    def is_active(self):
        """Gets the is_active of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The is_active of this InlineObject153.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this InlineObject153.

          # noqa: E501

        :param is_active: The is_active of this InlineObject153.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_protected(self):
        """Gets the is_protected of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The is_protected of this InlineObject153.  # noqa: E501
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """Sets the is_protected of this InlineObject153.

          # noqa: E501

        :param is_protected: The is_protected of this InlineObject153.  # noqa: E501
        :type: bool
        """

        self._is_protected = is_protected

    @property
    def usage(self):
        """Gets the usage of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The usage of this InlineObject153.  # noqa: E501
        :rtype: list[str]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this InlineObject153.

          # noqa: E501

        :param usage: The usage of this InlineObject153.  # noqa: E501
        :type: list[str]
        """

        self._usage = usage

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject153.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject153.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject153.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def type(self):
        """Gets the type of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The type of this InlineObject153.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject153.

          # noqa: E501

        :param type: The type of this InlineObject153.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this InlineObject153.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject153.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject153.

          # noqa: E501

        :param description: The description of this InlineObject153.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, InlineObject153):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject153):
            return True

        return self.to_dict() != other.to_dict()
