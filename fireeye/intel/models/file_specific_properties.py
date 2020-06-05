# coding: utf-8

"""
    Intel API v3 - Simplified Intel API

    FireEye Intel API - Simplified Intelligence  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@fireeye.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fireeye.intel.configuration import Configuration


class FileSpecificProperties(object):
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
        'hashes': 'FileSpecificPropertiesHashes',
        'full_path': 'str',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'hashes': 'hashes',
        'full_path': 'full_path',
        'size': 'size'
    }

    def __init__(self, name=None, hashes=None, full_path=None, size=None, local_vars_configuration=None):  # noqa: E501
        """FileSpecificProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._hashes = None
        self._full_path = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if hashes is not None:
            self.hashes = hashes
        if full_path is not None:
            self.full_path = full_path
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this FileSpecificProperties.  # noqa: E501


        :return: The name of this FileSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSpecificProperties.


        :param name: The name of this FileSpecificProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hashes(self):
        """Gets the hashes of this FileSpecificProperties.  # noqa: E501


        :return: The hashes of this FileSpecificProperties.  # noqa: E501
        :rtype: FileSpecificPropertiesHashes
        """
        return self._hashes

    @hashes.setter
    def hashes(self, hashes):
        """Sets the hashes of this FileSpecificProperties.


        :param hashes: The hashes of this FileSpecificProperties.  # noqa: E501
        :type: FileSpecificPropertiesHashes
        """

        self._hashes = hashes

    @property
    def full_path(self):
        """Gets the full_path of this FileSpecificProperties.  # noqa: E501


        :return: The full_path of this FileSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this FileSpecificProperties.


        :param full_path: The full_path of this FileSpecificProperties.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def size(self):
        """Gets the size of this FileSpecificProperties.  # noqa: E501


        :return: The size of this FileSpecificProperties.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileSpecificProperties.


        :param size: The size of this FileSpecificProperties.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, FileSpecificProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSpecificProperties):
            return True

        return self.to_dict() != other.to_dict()
