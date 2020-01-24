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


class InlineObject120(object):
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
        'content_length': 'int',
        'tags': 'list[str]',
        'filename': 'str',
        'content': 'str',
        'content_type': 'str',
        'play_execution': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'content_length': 'content_length',
        'tags': 'tags',
        'filename': 'filename',
        'content': 'content',
        'content_type': 'content_type',
        'play_execution': 'play_execution',
        'metadata': 'metadata'
    }

    def __init__(self, content_length=None, tags=None, filename=None, content=None, content_type=None, play_execution=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject120 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_length = None
        self._tags = None
        self._filename = None
        self._content = None
        self._content_type = None
        self._play_execution = None
        self._metadata = None
        self.discriminator = None

        if content_length is not None:
            self.content_length = content_length
        if tags is not None:
            self.tags = tags
        if filename is not None:
            self.filename = filename
        if content is not None:
            self.content = content
        if content_type is not None:
            self.content_type = content_type
        if play_execution is not None:
            self.play_execution = play_execution
        if metadata is not None:
            self.metadata = metadata

    @property
    def content_length(self):
        """Gets the content_length of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The content_length of this InlineObject120.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this InlineObject120.

          # noqa: E501

        :param content_length: The content_length of this InlineObject120.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def tags(self):
        """Gets the tags of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject120.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject120.

          # noqa: E501

        :param tags: The tags of this InlineObject120.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def filename(self):
        """Gets the filename of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The filename of this InlineObject120.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this InlineObject120.

          # noqa: E501

        :param filename: The filename of this InlineObject120.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def content(self):
        """Gets the content of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The content of this InlineObject120.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineObject120.

          # noqa: E501

        :param content: The content of this InlineObject120.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_type(self):
        """Gets the content_type of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The content_type of this InlineObject120.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this InlineObject120.

          # noqa: E501

        :param content_type: The content_type of this InlineObject120.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def play_execution(self):
        """Gets the play_execution of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The play_execution of this InlineObject120.  # noqa: E501
        :rtype: str
        """
        return self._play_execution

    @play_execution.setter
    def play_execution(self, play_execution):
        """Sets the play_execution of this InlineObject120.

          # noqa: E501

        :param play_execution: The play_execution of this InlineObject120.  # noqa: E501
        :type: str
        """

        self._play_execution = play_execution

    @property
    def metadata(self):
        """Gets the metadata of this InlineObject120.  # noqa: E501

          # noqa: E501

        :return: The metadata of this InlineObject120.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineObject120.

          # noqa: E501

        :param metadata: The metadata of this InlineObject120.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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
        if not isinstance(other, InlineObject120):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject120):
            return True

        return self.to_dict() != other.to_dict()
