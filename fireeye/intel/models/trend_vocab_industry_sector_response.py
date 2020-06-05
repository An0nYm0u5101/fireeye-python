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


class TrendVocabIndustrySectorResponse(object):
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
        'message': 'TrendVocabIndustrySector',
        'success': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'success': 'success'
    }

    def __init__(self, message=None, success=None, local_vars_configuration=None):  # noqa: E501
        """TrendVocabIndustrySectorResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._success = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if success is not None:
            self.success = success

    @property
    def message(self):
        """Gets the message of this TrendVocabIndustrySectorResponse.  # noqa: E501


        :return: The message of this TrendVocabIndustrySectorResponse.  # noqa: E501
        :rtype: TrendVocabIndustrySector
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TrendVocabIndustrySectorResponse.


        :param message: The message of this TrendVocabIndustrySectorResponse.  # noqa: E501
        :type: TrendVocabIndustrySector
        """

        self._message = message

    @property
    def success(self):
        """Gets the success of this TrendVocabIndustrySectorResponse.  # noqa: E501


        :return: The success of this TrendVocabIndustrySectorResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TrendVocabIndustrySectorResponse.


        :param success: The success of this TrendVocabIndustrySectorResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, TrendVocabIndustrySectorResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrendVocabIndustrySectorResponse):
            return True

        return self.to_dict() != other.to_dict()
