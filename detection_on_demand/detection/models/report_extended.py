# coding: utf-8

"""
    Detection On Demand

    FireEye offers a best-in-class virtual execution engine in many of its core products, including our Network Security, Email Security, and File Analysis solutions. Now our customers can interact with and consume those capabilities directly via a scalable and performant web service. Use the new RESTful API to submit files for malware analysis, search hash values for past analysis results, get full reports for your file submissions, and integrate into your existing toolsets and workflows.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: developers@fireeye.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from detection.configuration import Configuration


class ReportExtended(object):
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
        'report_id': 'str',
        'overall_status': 'str',
        'is_malicious': 'bool',
        'started_at': 'str',
        'completed_at': 'str',
        'duration': 'float',
        'file_extension': 'str',
        'file_name': 'str',
        'file_size': 'int',
        'md5': 'str',
        'sha256': 'str',
        'signature_name': 'list[str]',
        'engine_results': 'ReportExtendedEngineResults'
    }

    attribute_map = {
        'report_id': 'report_id',
        'overall_status': 'overall_status',
        'is_malicious': 'is_malicious',
        'started_at': 'started_at',
        'completed_at': 'completed_at',
        'duration': 'duration',
        'file_extension': 'file_extension',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'md5': 'md5',
        'sha256': 'sha256',
        'signature_name': 'signature_name',
        'engine_results': 'engine_results'
    }

    def __init__(self, report_id=None, overall_status=None, is_malicious=None, started_at=None, completed_at=None, duration=None, file_extension=None, file_name=None, file_size=None, md5=None, sha256=None, signature_name=None, engine_results=None, local_vars_configuration=None):  # noqa: E501
        """ReportExtended - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._report_id = None
        self._overall_status = None
        self._is_malicious = None
        self._started_at = None
        self._completed_at = None
        self._duration = None
        self._file_extension = None
        self._file_name = None
        self._file_size = None
        self._md5 = None
        self._sha256 = None
        self._signature_name = None
        self._engine_results = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if overall_status is not None:
            self.overall_status = overall_status
        if is_malicious is not None:
            self.is_malicious = is_malicious
        if started_at is not None:
            self.started_at = started_at
        if completed_at is not None:
            self.completed_at = completed_at
        if duration is not None:
            self.duration = duration
        if file_extension is not None:
            self.file_extension = file_extension
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if md5 is not None:
            self.md5 = md5
        if sha256 is not None:
            self.sha256 = sha256
        if signature_name is not None:
            self.signature_name = signature_name
        if engine_results is not None:
            self.engine_results = engine_results

    @property
    def report_id(self):
        """Gets the report_id of this ReportExtended.  # noqa: E501


        :return: The report_id of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportExtended.


        :param report_id: The report_id of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def overall_status(self):
        """Gets the overall_status of this ReportExtended.  # noqa: E501

        Indicates whether processing of the submitted file is complete.  # noqa: E501

        :return: The overall_status of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this ReportExtended.

        Indicates whether processing of the submitted file is complete.  # noqa: E501

        :param overall_status: The overall_status of this ReportExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["DONE", "RUNNING", "FAILED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overall_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overall_status` ({0}), must be one of {1}"  # noqa: E501
                .format(overall_status, allowed_values)
            )

        self._overall_status = overall_status

    @property
    def is_malicious(self):
        """Gets the is_malicious of this ReportExtended.  # noqa: E501

        FireEye's final determination if the file is malicious or not.  # noqa: E501

        :return: The is_malicious of this ReportExtended.  # noqa: E501
        :rtype: bool
        """
        return self._is_malicious

    @is_malicious.setter
    def is_malicious(self, is_malicious):
        """Sets the is_malicious of this ReportExtended.

        FireEye's final determination if the file is malicious or not.  # noqa: E501

        :param is_malicious: The is_malicious of this ReportExtended.  # noqa: E501
        :type: bool
        """
        allowed_values = [true, false]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and is_malicious not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `is_malicious` ({0}), must be one of {1}"  # noqa: E501
                .format(is_malicious, allowed_values)
            )

        self._is_malicious = is_malicious

    @property
    def started_at(self):
        """Gets the started_at of this ReportExtended.  # noqa: E501

        The time processing was started.  # noqa: E501

        :return: The started_at of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this ReportExtended.

        The time processing was started.  # noqa: E501

        :param started_at: The started_at of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def completed_at(self):
        """Gets the completed_at of this ReportExtended.  # noqa: E501

        The time processing was completed.  # noqa: E501

        :return: The completed_at of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this ReportExtended.

        The time processing was completed.  # noqa: E501

        :param completed_at: The completed_at of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._completed_at = completed_at

    @property
    def duration(self):
        """Gets the duration of this ReportExtended.  # noqa: E501

        The processing time in seconds.  # noqa: E501

        :return: The duration of this ReportExtended.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ReportExtended.

        The processing time in seconds.  # noqa: E501

        :param duration: The duration of this ReportExtended.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def file_extension(self):
        """Gets the file_extension of this ReportExtended.  # noqa: E501

        The file extension of the submitted file.  # noqa: E501

        :return: The file_extension of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this ReportExtended.

        The file extension of the submitted file.  # noqa: E501

        :param file_extension: The file_extension of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def file_name(self):
        """Gets the file_name of this ReportExtended.  # noqa: E501

        The name of the submitted file.  # noqa: E501

        :return: The file_name of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ReportExtended.

        The name of the submitted file.  # noqa: E501

        :param file_name: The file_name of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this ReportExtended.  # noqa: E501

        The size of the submitted file in KB.  # noqa: E501

        :return: The file_size of this ReportExtended.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ReportExtended.

        The size of the submitted file in KB.  # noqa: E501

        :param file_size: The file_size of this ReportExtended.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def md5(self):
        """Gets the md5 of this ReportExtended.  # noqa: E501

        MD5 hash.  # noqa: E501

        :return: The md5 of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this ReportExtended.

        MD5 hash.  # noqa: E501

        :param md5: The md5 of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def sha256(self):
        """Gets the sha256 of this ReportExtended.  # noqa: E501

        SHA256 hash.  # noqa: E501

        :return: The sha256 of this ReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this ReportExtended.

        SHA256 hash.  # noqa: E501

        :param sha256: The sha256 of this ReportExtended.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def signature_name(self):
        """Gets the signature_name of this ReportExtended.  # noqa: E501


        :return: The signature_name of this ReportExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this ReportExtended.


        :param signature_name: The signature_name of this ReportExtended.  # noqa: E501
        :type: list[str]
        """

        self._signature_name = signature_name

    @property
    def engine_results(self):
        """Gets the engine_results of this ReportExtended.  # noqa: E501


        :return: The engine_results of this ReportExtended.  # noqa: E501
        :rtype: ReportExtendedEngineResults
        """
        return self._engine_results

    @engine_results.setter
    def engine_results(self, engine_results):
        """Sets the engine_results of this ReportExtended.


        :param engine_results: The engine_results of this ReportExtended.  # noqa: E501
        :type: ReportExtendedEngineResults
        """

        self._engine_results = engine_results

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
        if not isinstance(other, ReportExtended):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportExtended):
            return True

        return self.to_dict() != other.to_dict()
