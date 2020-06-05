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


class TrendActorRegionTargetRelatedResponseMessageActor(object):
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
        'region_target': 'list[TrendActorObjectCommonProperties]',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'region_target': 'region_target',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, region_target=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TrendActorRegionTargetRelatedResponseMessageActor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._region_target = None
        self._name = None
        self._id = None
        self.discriminator = None

        if region_target is not None:
            self.region_target = region_target
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def region_target(self):
        """Gets the region_target of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501


        :return: The region_target of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :rtype: list[TrendActorObjectCommonProperties]
        """
        return self._region_target

    @region_target.setter
    def region_target(self, region_target):
        """Sets the region_target of this TrendActorRegionTargetRelatedResponseMessageActor.


        :param region_target: The region_target of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :type: list[TrendActorObjectCommonProperties]
        """

        self._region_target = region_target

    @property
    def name(self):
        """Gets the name of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501


        :return: The name of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrendActorRegionTargetRelatedResponseMessageActor.


        :param name: The name of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501


        :return: The id of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrendActorRegionTargetRelatedResponseMessageActor.


        :param id: The id of this TrendActorRegionTargetRelatedResponseMessageActor.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, TrendActorRegionTargetRelatedResponseMessageActor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrendActorRegionTargetRelatedResponseMessageActor):
            return True

        return self.to_dict() != other.to_dict()
