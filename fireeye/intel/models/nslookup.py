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


class Nslookup(object):
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
        'type': 'str',
        'id': 'str',
        'current_asn': 'str',
        'location': 'ContextLocation'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'current_asn': 'current_asn',
        'location': 'location'
    }

    def __init__(self, type=None, id=None, current_asn=None, location=None, local_vars_configuration=None):  # noqa: E501
        """Nslookup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._current_asn = None
        self._location = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if current_asn is not None:
            self.current_asn = current_asn
        if location is not None:
            self.location = location

    @property
    def type(self):
        """Gets the type of this Nslookup.  # noqa: E501


        :return: The type of this Nslookup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Nslookup.


        :param type: The type of this Nslookup.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Nslookup.  # noqa: E501


        :return: The id of this Nslookup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Nslookup.


        :param id: The id of this Nslookup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def current_asn(self):
        """Gets the current_asn of this Nslookup.  # noqa: E501


        :return: The current_asn of this Nslookup.  # noqa: E501
        :rtype: str
        """
        return self._current_asn

    @current_asn.setter
    def current_asn(self, current_asn):
        """Sets the current_asn of this Nslookup.


        :param current_asn: The current_asn of this Nslookup.  # noqa: E501
        :type: str
        """

        self._current_asn = current_asn

    @property
    def location(self):
        """Gets the location of this Nslookup.  # noqa: E501


        :return: The location of this Nslookup.  # noqa: E501
        :rtype: ContextLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Nslookup.


        :param location: The location of this Nslookup.  # noqa: E501
        :type: ContextLocation
        """

        self._location = location

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
        if not isinstance(other, Nslookup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Nslookup):
            return True

        return self.to_dict() != other.to_dict()
