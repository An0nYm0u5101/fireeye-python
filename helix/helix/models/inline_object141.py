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


class InlineObject141(object):
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
        'query_end': 'str',
        'pdf_state': 'str',
        'pdf_duration': 'int',
        'finished_at': 'str',
        'query_start': 'str',
        'error_message': 'str',
        'is_mssp': 'bool',
        'state': 'str',
        'dashboard': 'str',
        'pdf_started_at': 'str',
        'duration': 'int',
        'started_at': 'str',
        'pdf_finished_at': 'str'
    }

    attribute_map = {
        'query_end': 'query_end',
        'pdf_state': 'pdf_state',
        'pdf_duration': 'pdf_duration',
        'finished_at': 'finished_at',
        'query_start': 'query_start',
        'error_message': 'error_message',
        'is_mssp': 'is_mssp',
        'state': 'state',
        'dashboard': 'dashboard',
        'pdf_started_at': 'pdf_started_at',
        'duration': 'duration',
        'started_at': 'started_at',
        'pdf_finished_at': 'pdf_finished_at'
    }

    def __init__(self, query_end=None, pdf_state=None, pdf_duration=None, finished_at=None, query_start=None, error_message=None, is_mssp=None, state=None, dashboard=None, pdf_started_at=None, duration=None, started_at=None, pdf_finished_at=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject141 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_end = None
        self._pdf_state = None
        self._pdf_duration = None
        self._finished_at = None
        self._query_start = None
        self._error_message = None
        self._is_mssp = None
        self._state = None
        self._dashboard = None
        self._pdf_started_at = None
        self._duration = None
        self._started_at = None
        self._pdf_finished_at = None
        self.discriminator = None

        if query_end is not None:
            self.query_end = query_end
        if pdf_state is not None:
            self.pdf_state = pdf_state
        if pdf_duration is not None:
            self.pdf_duration = pdf_duration
        if finished_at is not None:
            self.finished_at = finished_at
        if query_start is not None:
            self.query_start = query_start
        if error_message is not None:
            self.error_message = error_message
        if is_mssp is not None:
            self.is_mssp = is_mssp
        if state is not None:
            self.state = state
        self.dashboard = dashboard
        if pdf_started_at is not None:
            self.pdf_started_at = pdf_started_at
        if duration is not None:
            self.duration = duration
        self.started_at = started_at
        if pdf_finished_at is not None:
            self.pdf_finished_at = pdf_finished_at

    @property
    def query_end(self):
        """Gets the query_end of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The query_end of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._query_end

    @query_end.setter
    def query_end(self, query_end):
        """Sets the query_end of this InlineObject141.

          # noqa: E501

        :param query_end: The query_end of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._query_end = query_end

    @property
    def pdf_state(self):
        """Gets the pdf_state of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The pdf_state of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._pdf_state

    @pdf_state.setter
    def pdf_state(self, pdf_state):
        """Sets the pdf_state of this InlineObject141.

          # noqa: E501

        :param pdf_state: The pdf_state of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._pdf_state = pdf_state

    @property
    def pdf_duration(self):
        """Gets the pdf_duration of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The pdf_duration of this InlineObject141.  # noqa: E501
        :rtype: int
        """
        return self._pdf_duration

    @pdf_duration.setter
    def pdf_duration(self, pdf_duration):
        """Sets the pdf_duration of this InlineObject141.

          # noqa: E501

        :param pdf_duration: The pdf_duration of this InlineObject141.  # noqa: E501
        :type: int
        """

        self._pdf_duration = pdf_duration

    @property
    def finished_at(self):
        """Gets the finished_at of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The finished_at of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this InlineObject141.

          # noqa: E501

        :param finished_at: The finished_at of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def query_start(self):
        """Gets the query_start of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The query_start of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        """Sets the query_start of this InlineObject141.

          # noqa: E501

        :param query_start: The query_start of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._query_start = query_start

    @property
    def error_message(self):
        """Gets the error_message of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The error_message of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InlineObject141.

          # noqa: E501

        :param error_message: The error_message of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def is_mssp(self):
        """Gets the is_mssp of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The is_mssp of this InlineObject141.  # noqa: E501
        :rtype: bool
        """
        return self._is_mssp

    @is_mssp.setter
    def is_mssp(self, is_mssp):
        """Sets the is_mssp of this InlineObject141.

          # noqa: E501

        :param is_mssp: The is_mssp of this InlineObject141.  # noqa: E501
        :type: bool
        """

        self._is_mssp = is_mssp

    @property
    def state(self):
        """Gets the state of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject141.

          # noqa: E501

        :param state: The state of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def dashboard(self):
        """Gets the dashboard of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The dashboard of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this InlineObject141.

          # noqa: E501

        :param dashboard: The dashboard of this InlineObject141.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dashboard is None:  # noqa: E501
            raise ValueError("Invalid value for `dashboard`, must not be `None`")  # noqa: E501

        self._dashboard = dashboard

    @property
    def pdf_started_at(self):
        """Gets the pdf_started_at of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The pdf_started_at of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._pdf_started_at

    @pdf_started_at.setter
    def pdf_started_at(self, pdf_started_at):
        """Sets the pdf_started_at of this InlineObject141.

          # noqa: E501

        :param pdf_started_at: The pdf_started_at of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._pdf_started_at = pdf_started_at

    @property
    def duration(self):
        """Gets the duration of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The duration of this InlineObject141.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineObject141.

          # noqa: E501

        :param duration: The duration of this InlineObject141.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def started_at(self):
        """Gets the started_at of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The started_at of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this InlineObject141.

          # noqa: E501

        :param started_at: The started_at of this InlineObject141.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def pdf_finished_at(self):
        """Gets the pdf_finished_at of this InlineObject141.  # noqa: E501

          # noqa: E501

        :return: The pdf_finished_at of this InlineObject141.  # noqa: E501
        :rtype: str
        """
        return self._pdf_finished_at

    @pdf_finished_at.setter
    def pdf_finished_at(self, pdf_finished_at):
        """Sets the pdf_finished_at of this InlineObject141.

          # noqa: E501

        :param pdf_finished_at: The pdf_finished_at of this InlineObject141.  # noqa: E501
        :type: str
        """

        self._pdf_finished_at = pdf_finished_at

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
        if not isinstance(other, InlineObject141):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject141):
            return True

        return self.to_dict() != other.to_dict()
