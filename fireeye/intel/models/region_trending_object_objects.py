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


class RegionTrendingObjectObjects(object):
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
        'metrics': 'list[Metric]',
        'name': 'str',
        'iso_country_code_2': 'str',
        'id': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'name': 'name',
        'iso_country_code_2': 'iso_country_code_2',
        'id': 'id'
    }

    def __init__(self, metrics=None, name=None, iso_country_code_2=None, id=None, local_vars_configuration=None):  # noqa: E501
        """RegionTrendingObjectObjects - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metrics = None
        self._name = None
        self._iso_country_code_2 = None
        self._id = None
        self.discriminator = None

        if metrics is not None:
            self.metrics = metrics
        if name is not None:
            self.name = name
        if iso_country_code_2 is not None:
            self.iso_country_code_2 = iso_country_code_2
        if id is not None:
            self.id = id

    @property
    def metrics(self):
        """Gets the metrics of this RegionTrendingObjectObjects.  # noqa: E501


        :return: The metrics of this RegionTrendingObjectObjects.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this RegionTrendingObjectObjects.


        :param metrics: The metrics of this RegionTrendingObjectObjects.  # noqa: E501
        :type: list[Metric]
        """

        self._metrics = metrics

    @property
    def name(self):
        """Gets the name of this RegionTrendingObjectObjects.  # noqa: E501


        :return: The name of this RegionTrendingObjectObjects.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegionTrendingObjectObjects.


        :param name: The name of this RegionTrendingObjectObjects.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def iso_country_code_2(self):
        """Gets the iso_country_code_2 of this RegionTrendingObjectObjects.  # noqa: E501


        :return: The iso_country_code_2 of this RegionTrendingObjectObjects.  # noqa: E501
        :rtype: str
        """
        return self._iso_country_code_2

    @iso_country_code_2.setter
    def iso_country_code_2(self, iso_country_code_2):
        """Sets the iso_country_code_2 of this RegionTrendingObjectObjects.


        :param iso_country_code_2: The iso_country_code_2 of this RegionTrendingObjectObjects.  # noqa: E501
        :type: str
        """

        self._iso_country_code_2 = iso_country_code_2

    @property
    def id(self):
        """Gets the id of this RegionTrendingObjectObjects.  # noqa: E501


        :return: The id of this RegionTrendingObjectObjects.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegionTrendingObjectObjects.


        :param id: The id of this RegionTrendingObjectObjects.  # noqa: E501
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
        if not isinstance(other, RegionTrendingObjectObjects):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegionTrendingObjectObjects):
            return True

        return self.to_dict() != other.to_dict()
