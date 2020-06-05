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


class TrendRegionRegionTargetRelatedResponseMessage(object):
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
        'region': 'list[TrendRegionRegionTargetRelatedResponseMessageRegion]'
    }

    attribute_map = {
        'region': 'region'
    }

    def __init__(self, region=None, local_vars_configuration=None):  # noqa: E501
        """TrendRegionRegionTargetRelatedResponseMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._region = None
        self.discriminator = None

        if region is not None:
            self.region = region

    @property
    def region(self):
        """Gets the region of this TrendRegionRegionTargetRelatedResponseMessage.  # noqa: E501


        :return: The region of this TrendRegionRegionTargetRelatedResponseMessage.  # noqa: E501
        :rtype: list[TrendRegionRegionTargetRelatedResponseMessageRegion]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TrendRegionRegionTargetRelatedResponseMessage.


        :param region: The region of this TrendRegionRegionTargetRelatedResponseMessage.  # noqa: E501
        :type: list[TrendRegionRegionTargetRelatedResponseMessageRegion]
        """

        self._region = region

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
        if not isinstance(other, TrendRegionRegionTargetRelatedResponseMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrendRegionRegionTargetRelatedResponseMessage):
            return True

        return self.to_dict() != other.to_dict()
