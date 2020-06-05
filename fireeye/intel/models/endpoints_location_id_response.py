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


class EndpointsLocationIdResponse(object):
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
        'id': 'str',
        'created': 'str',
        'modified': 'str',
        'name': 'str',
        'city': 'str',
        'iso_country_code_2': 'str',
        'iso_country_code_3': 'list[str]',
        'iocs': 'Indicators',
        'malwares': 'list[Malware]',
        'locations': 'LocationsLocations',
        'industries': 'list[Identity]',
        'campaigns': 'list[Campaign]',
        'attack_patterns': 'AttackPatternsAttackPatterns',
        'actors': 'list[Actor]',
        'tools': 'list[Tool]',
        'softwares': 'list[Software]',
        'infrastructures': 'list[Infrastructure]',
        'cve': 'list[Vulnerability]',
        'intrusion_sets': 'list[IntrusionSet]',
        'socket_addrs': 'list[SocketAddr]',
        'network_traffics': 'list[NetworkTraffic]',
        'windows_registry_keys': 'list[WindowsRegistryKey]',
        'course_of_actions': 'list[CourseOfAction]',
        'reports': 'list[Report]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'name': 'name',
        'city': 'city',
        'iso_country_code_2': 'iso_country_code_2',
        'iso_country_code_3': 'iso_country_code_3',
        'iocs': 'iocs',
        'malwares': 'malwares',
        'locations': 'locations',
        'industries': 'industries',
        'campaigns': 'campaigns',
        'attack_patterns': 'attack-patterns',
        'actors': 'actors',
        'tools': 'tools',
        'softwares': 'softwares',
        'infrastructures': 'infrastructures',
        'cve': 'cve',
        'intrusion_sets': 'intrusion-sets',
        'socket_addrs': 'socket-addrs',
        'network_traffics': 'network-traffics',
        'windows_registry_keys': 'windows-registry-keys',
        'course_of_actions': 'course-of-actions',
        'reports': 'reports'
    }

    def __init__(self, id=None, created=None, modified=None, name=None, city=None, iso_country_code_2=None, iso_country_code_3=None, iocs=None, malwares=None, locations=None, industries=None, campaigns=None, attack_patterns=None, actors=None, tools=None, softwares=None, infrastructures=None, cve=None, intrusion_sets=None, socket_addrs=None, network_traffics=None, windows_registry_keys=None, course_of_actions=None, reports=None, local_vars_configuration=None):  # noqa: E501
        """EndpointsLocationIdResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._modified = None
        self._name = None
        self._city = None
        self._iso_country_code_2 = None
        self._iso_country_code_3 = None
        self._iocs = None
        self._malwares = None
        self._locations = None
        self._industries = None
        self._campaigns = None
        self._attack_patterns = None
        self._actors = None
        self._tools = None
        self._softwares = None
        self._infrastructures = None
        self._cve = None
        self._intrusion_sets = None
        self._socket_addrs = None
        self._network_traffics = None
        self._windows_registry_keys = None
        self._course_of_actions = None
        self._reports = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if iso_country_code_2 is not None:
            self.iso_country_code_2 = iso_country_code_2
        if iso_country_code_3 is not None:
            self.iso_country_code_3 = iso_country_code_3
        if iocs is not None:
            self.iocs = iocs
        if malwares is not None:
            self.malwares = malwares
        if locations is not None:
            self.locations = locations
        if industries is not None:
            self.industries = industries
        if campaigns is not None:
            self.campaigns = campaigns
        if attack_patterns is not None:
            self.attack_patterns = attack_patterns
        if actors is not None:
            self.actors = actors
        if tools is not None:
            self.tools = tools
        if softwares is not None:
            self.softwares = softwares
        if infrastructures is not None:
            self.infrastructures = infrastructures
        if cve is not None:
            self.cve = cve
        if intrusion_sets is not None:
            self.intrusion_sets = intrusion_sets
        if socket_addrs is not None:
            self.socket_addrs = socket_addrs
        if network_traffics is not None:
            self.network_traffics = network_traffics
        if windows_registry_keys is not None:
            self.windows_registry_keys = windows_registry_keys
        if course_of_actions is not None:
            self.course_of_actions = course_of_actions
        if reports is not None:
            self.reports = reports

    @property
    def id(self):
        """Gets the id of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The id of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointsLocationIdResponse.


        :param id: The id of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The created of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EndpointsLocationIdResponse.


        :param created: The created of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The modified of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this EndpointsLocationIdResponse.


        :param modified: The modified of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The name of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointsLocationIdResponse.


        :param name: The name of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """Gets the city of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The city of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EndpointsLocationIdResponse.


        :param city: The city of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def iso_country_code_2(self):
        """Gets the iso_country_code_2 of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The iso_country_code_2 of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._iso_country_code_2

    @iso_country_code_2.setter
    def iso_country_code_2(self, iso_country_code_2):
        """Sets the iso_country_code_2 of this EndpointsLocationIdResponse.


        :param iso_country_code_2: The iso_country_code_2 of this EndpointsLocationIdResponse.  # noqa: E501
        :type: str
        """

        self._iso_country_code_2 = iso_country_code_2

    @property
    def iso_country_code_3(self):
        """Gets the iso_country_code_3 of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The iso_country_code_3 of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._iso_country_code_3

    @iso_country_code_3.setter
    def iso_country_code_3(self, iso_country_code_3):
        """Sets the iso_country_code_3 of this EndpointsLocationIdResponse.


        :param iso_country_code_3: The iso_country_code_3 of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[str]
        """

        self._iso_country_code_3 = iso_country_code_3

    @property
    def iocs(self):
        """Gets the iocs of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The iocs of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: Indicators
        """
        return self._iocs

    @iocs.setter
    def iocs(self, iocs):
        """Sets the iocs of this EndpointsLocationIdResponse.


        :param iocs: The iocs of this EndpointsLocationIdResponse.  # noqa: E501
        :type: Indicators
        """

        self._iocs = iocs

    @property
    def malwares(self):
        """Gets the malwares of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The malwares of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Malware]
        """
        return self._malwares

    @malwares.setter
    def malwares(self, malwares):
        """Sets the malwares of this EndpointsLocationIdResponse.


        :param malwares: The malwares of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Malware]
        """

        self._malwares = malwares

    @property
    def locations(self):
        """Gets the locations of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The locations of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: LocationsLocations
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this EndpointsLocationIdResponse.


        :param locations: The locations of this EndpointsLocationIdResponse.  # noqa: E501
        :type: LocationsLocations
        """

        self._locations = locations

    @property
    def industries(self):
        """Gets the industries of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The industries of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Identity]
        """
        return self._industries

    @industries.setter
    def industries(self, industries):
        """Sets the industries of this EndpointsLocationIdResponse.


        :param industries: The industries of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Identity]
        """

        self._industries = industries

    @property
    def campaigns(self):
        """Gets the campaigns of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The campaigns of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Campaign]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """Sets the campaigns of this EndpointsLocationIdResponse.


        :param campaigns: The campaigns of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Campaign]
        """

        self._campaigns = campaigns

    @property
    def attack_patterns(self):
        """Gets the attack_patterns of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The attack_patterns of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: AttackPatternsAttackPatterns
        """
        return self._attack_patterns

    @attack_patterns.setter
    def attack_patterns(self, attack_patterns):
        """Sets the attack_patterns of this EndpointsLocationIdResponse.


        :param attack_patterns: The attack_patterns of this EndpointsLocationIdResponse.  # noqa: E501
        :type: AttackPatternsAttackPatterns
        """

        self._attack_patterns = attack_patterns

    @property
    def actors(self):
        """Gets the actors of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The actors of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Actor]
        """
        return self._actors

    @actors.setter
    def actors(self, actors):
        """Sets the actors of this EndpointsLocationIdResponse.


        :param actors: The actors of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Actor]
        """

        self._actors = actors

    @property
    def tools(self):
        """Gets the tools of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The tools of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Tool]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this EndpointsLocationIdResponse.


        :param tools: The tools of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Tool]
        """

        self._tools = tools

    @property
    def softwares(self):
        """Gets the softwares of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The softwares of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Software]
        """
        return self._softwares

    @softwares.setter
    def softwares(self, softwares):
        """Sets the softwares of this EndpointsLocationIdResponse.


        :param softwares: The softwares of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Software]
        """

        self._softwares = softwares

    @property
    def infrastructures(self):
        """Gets the infrastructures of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The infrastructures of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Infrastructure]
        """
        return self._infrastructures

    @infrastructures.setter
    def infrastructures(self, infrastructures):
        """Sets the infrastructures of this EndpointsLocationIdResponse.


        :param infrastructures: The infrastructures of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Infrastructure]
        """

        self._infrastructures = infrastructures

    @property
    def cve(self):
        """Gets the cve of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The cve of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Vulnerability]
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this EndpointsLocationIdResponse.


        :param cve: The cve of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Vulnerability]
        """

        self._cve = cve

    @property
    def intrusion_sets(self):
        """Gets the intrusion_sets of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The intrusion_sets of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[IntrusionSet]
        """
        return self._intrusion_sets

    @intrusion_sets.setter
    def intrusion_sets(self, intrusion_sets):
        """Sets the intrusion_sets of this EndpointsLocationIdResponse.


        :param intrusion_sets: The intrusion_sets of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[IntrusionSet]
        """

        self._intrusion_sets = intrusion_sets

    @property
    def socket_addrs(self):
        """Gets the socket_addrs of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The socket_addrs of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[SocketAddr]
        """
        return self._socket_addrs

    @socket_addrs.setter
    def socket_addrs(self, socket_addrs):
        """Sets the socket_addrs of this EndpointsLocationIdResponse.


        :param socket_addrs: The socket_addrs of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[SocketAddr]
        """

        self._socket_addrs = socket_addrs

    @property
    def network_traffics(self):
        """Gets the network_traffics of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The network_traffics of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[NetworkTraffic]
        """
        return self._network_traffics

    @network_traffics.setter
    def network_traffics(self, network_traffics):
        """Sets the network_traffics of this EndpointsLocationIdResponse.


        :param network_traffics: The network_traffics of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[NetworkTraffic]
        """

        self._network_traffics = network_traffics

    @property
    def windows_registry_keys(self):
        """Gets the windows_registry_keys of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The windows_registry_keys of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[WindowsRegistryKey]
        """
        return self._windows_registry_keys

    @windows_registry_keys.setter
    def windows_registry_keys(self, windows_registry_keys):
        """Sets the windows_registry_keys of this EndpointsLocationIdResponse.


        :param windows_registry_keys: The windows_registry_keys of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[WindowsRegistryKey]
        """

        self._windows_registry_keys = windows_registry_keys

    @property
    def course_of_actions(self):
        """Gets the course_of_actions of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The course_of_actions of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[CourseOfAction]
        """
        return self._course_of_actions

    @course_of_actions.setter
    def course_of_actions(self, course_of_actions):
        """Sets the course_of_actions of this EndpointsLocationIdResponse.


        :param course_of_actions: The course_of_actions of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[CourseOfAction]
        """

        self._course_of_actions = course_of_actions

    @property
    def reports(self):
        """Gets the reports of this EndpointsLocationIdResponse.  # noqa: E501


        :return: The reports of this EndpointsLocationIdResponse.  # noqa: E501
        :rtype: list[Report]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this EndpointsLocationIdResponse.


        :param reports: The reports of this EndpointsLocationIdResponse.  # noqa: E501
        :type: list[Report]
        """

        self._reports = reports

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
        if not isinstance(other, EndpointsLocationIdResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointsLocationIdResponse):
            return True

        return self.to_dict() != other.to_dict()
