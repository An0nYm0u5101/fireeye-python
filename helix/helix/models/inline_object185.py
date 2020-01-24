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


class InlineObject185(object):
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
        'status': 'str',
        'interval': 'str',
        'packet_loss': 'str',
        'hostname': 'str',
        'metrics': 'str',
        'meta_cbid': 'str'
    }

    attribute_map = {
        'status': 'status',
        'interval': 'interval',
        'packet_loss': 'packet_loss',
        'hostname': 'hostname',
        'metrics': 'metrics',
        'meta_cbid': 'meta_cbid'
    }

    def __init__(self, status=None, interval=None, packet_loss=None, hostname=None, metrics=None, meta_cbid=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject185 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._interval = None
        self._packet_loss = None
        self._hostname = None
        self._metrics = None
        self._meta_cbid = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if interval is not None:
            self.interval = interval
        if packet_loss is not None:
            self.packet_loss = packet_loss
        if hostname is not None:
            self.hostname = hostname
        if metrics is not None:
            self.metrics = metrics
        self.meta_cbid = meta_cbid

    @property
    def status(self):
        """Gets the status of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The status of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineObject185.

          # noqa: E501

        :param status: The status of this InlineObject185.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def interval(self):
        """Gets the interval of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The interval of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this InlineObject185.

          # noqa: E501

        :param interval: The interval of this InlineObject185.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def packet_loss(self):
        """Gets the packet_loss of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The packet_loss of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._packet_loss

    @packet_loss.setter
    def packet_loss(self, packet_loss):
        """Sets the packet_loss of this InlineObject185.

          # noqa: E501

        :param packet_loss: The packet_loss of this InlineObject185.  # noqa: E501
        :type: str
        """

        self._packet_loss = packet_loss

    @property
    def hostname(self):
        """Gets the hostname of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The hostname of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this InlineObject185.

          # noqa: E501

        :param hostname: The hostname of this InlineObject185.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def metrics(self):
        """Gets the metrics of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The metrics of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this InlineObject185.

          # noqa: E501

        :param metrics: The metrics of this InlineObject185.  # noqa: E501
        :type: str
        """

        self._metrics = metrics

    @property
    def meta_cbid(self):
        """Gets the meta_cbid of this InlineObject185.  # noqa: E501

          # noqa: E501

        :return: The meta_cbid of this InlineObject185.  # noqa: E501
        :rtype: str
        """
        return self._meta_cbid

    @meta_cbid.setter
    def meta_cbid(self, meta_cbid):
        """Sets the meta_cbid of this InlineObject185.

          # noqa: E501

        :param meta_cbid: The meta_cbid of this InlineObject185.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and meta_cbid is None:  # noqa: E501
            raise ValueError("Invalid value for `meta_cbid`, must not be `None`")  # noqa: E501

        self._meta_cbid = meta_cbid

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
        if not isinstance(other, InlineObject185):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject185):
            return True

        return self.to_dict() != other.to_dict()
