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


class PostEntitiesLocationSpecificProperties(object):
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
        'motivation': 'list[str]',
        'name': 'str',
        'keyword': 'str',
        'associated_actors': 'list[object]',
        'type': 'str',
        'description': 'str',
        'location_id': 'str',
        'report_id': 'str'
    }

    attribute_map = {
        'motivation': 'motivation',
        'name': 'name',
        'keyword': 'keyword',
        'associated_actors': 'associated_actors',
        'type': 'type',
        'description': 'description',
        'location_id': 'location_id',
        'report_id': 'report_id'
    }

    def __init__(self, motivation=None, name=None, keyword=None, associated_actors=None, type=None, description=None, location_id=None, report_id=None, local_vars_configuration=None):  # noqa: E501
        """PostEntitiesLocationSpecificProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._motivation = None
        self._name = None
        self._keyword = None
        self._associated_actors = None
        self._type = None
        self._description = None
        self._location_id = None
        self._report_id = None
        self.discriminator = None

        if motivation is not None:
            self.motivation = motivation
        if name is not None:
            self.name = name
        if keyword is not None:
            self.keyword = keyword
        if associated_actors is not None:
            self.associated_actors = associated_actors
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if location_id is not None:
            self.location_id = location_id
        if report_id is not None:
            self.report_id = report_id

    @property
    def motivation(self):
        """Gets the motivation of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The motivation of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this PostEntitiesLocationSpecificProperties.


        :param motivation: The motivation of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: list[str]
        """

        self._motivation = motivation

    @property
    def name(self):
        """Gets the name of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The name of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostEntitiesLocationSpecificProperties.


        :param name: The name of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def keyword(self):
        """Gets the keyword of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The keyword of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this PostEntitiesLocationSpecificProperties.


        :param keyword: The keyword of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def associated_actors(self):
        """Gets the associated_actors of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The associated_actors of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: list[object]
        """
        return self._associated_actors

    @associated_actors.setter
    def associated_actors(self, associated_actors):
        """Sets the associated_actors of this PostEntitiesLocationSpecificProperties.


        :param associated_actors: The associated_actors of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: list[object]
        """

        self._associated_actors = associated_actors

    @property
    def type(self):
        """Gets the type of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The type of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostEntitiesLocationSpecificProperties.


        :param type: The type of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The description of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostEntitiesLocationSpecificProperties.


        :param description: The description of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def location_id(self):
        """Gets the location_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The location_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this PostEntitiesLocationSpecificProperties.


        :param location_id: The location_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

    @property
    def report_id(self):
        """Gets the report_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501


        :return: The report_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this PostEntitiesLocationSpecificProperties.


        :param report_id: The report_id of this PostEntitiesLocationSpecificProperties.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

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
        if not isinstance(other, PostEntitiesLocationSpecificProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostEntitiesLocationSpecificProperties):
            return True

        return self.to_dict() != other.to_dict()
