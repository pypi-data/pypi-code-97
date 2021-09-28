# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DistributionCenter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'code': 'str',
        'country_code': 'str',
        'default_center': 'bool',
        'default_handles_all_items': 'bool',
        'distribution_center_oid': 'int',
        'duns': 'str',
        'estimate_from_distribution_center_oid': 'int',
        'ftp_password': 'str',
        'hold_before_shipment_minutes': 'int',
        'hold_before_transmission': 'bool',
        'hold_auto_order_before_shipment_minutes': 'int',
        'latitude': 'float',
        'longitude': 'float',
        'name': 'str',
        'no_customer_direct_shipments': 'bool',
        'no_split_shipment': 'bool',
        'postal_code': 'str',
        'process_days': 'int',
        'process_inventory_start_time': 'str',
        'process_inventory_stop_time': 'str',
        'require_asn': 'bool',
        'send_kit_instead_of_components': 'bool',
        'shipment_cutoff_time_friday': 'str',
        'shipment_cutoff_time_monday': 'str',
        'shipment_cutoff_time_saturday': 'str',
        'shipment_cutoff_time_sunday': 'str',
        'shipment_cutoff_time_thursday': 'str',
        'shipment_cutoff_time_tuesday': 'str',
        'shipment_cutoff_time_wednesday': 'str',
        'state': 'str',
        'transport': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'code': 'code',
        'country_code': 'country_code',
        'default_center': 'default_center',
        'default_handles_all_items': 'default_handles_all_items',
        'distribution_center_oid': 'distribution_center_oid',
        'duns': 'duns',
        'estimate_from_distribution_center_oid': 'estimate_from_distribution_center_oid',
        'ftp_password': 'ftp_password',
        'hold_before_shipment_minutes': 'hold_before_shipment_minutes',
        'hold_before_transmission': 'hold_before_transmission',
        'hold_auto_order_before_shipment_minutes': 'holdAutoOrderBeforeShipmentMinutes',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'name': 'name',
        'no_customer_direct_shipments': 'no_customer_direct_shipments',
        'no_split_shipment': 'no_split_shipment',
        'postal_code': 'postal_code',
        'process_days': 'process_days',
        'process_inventory_start_time': 'process_inventory_start_time',
        'process_inventory_stop_time': 'process_inventory_stop_time',
        'require_asn': 'require_asn',
        'send_kit_instead_of_components': 'send_kit_instead_of_components',
        'shipment_cutoff_time_friday': 'shipment_cutoff_time_friday',
        'shipment_cutoff_time_monday': 'shipment_cutoff_time_monday',
        'shipment_cutoff_time_saturday': 'shipment_cutoff_time_saturday',
        'shipment_cutoff_time_sunday': 'shipment_cutoff_time_sunday',
        'shipment_cutoff_time_thursday': 'shipment_cutoff_time_thursday',
        'shipment_cutoff_time_tuesday': 'shipment_cutoff_time_tuesday',
        'shipment_cutoff_time_wednesday': 'shipment_cutoff_time_wednesday',
        'state': 'state',
        'transport': 'transport'
    }

    def __init__(self, address1=None, address2=None, city=None, code=None, country_code=None, default_center=None, default_handles_all_items=None, distribution_center_oid=None, duns=None, estimate_from_distribution_center_oid=None, ftp_password=None, hold_before_shipment_minutes=None, hold_before_transmission=None, hold_auto_order_before_shipment_minutes=None, latitude=None, longitude=None, name=None, no_customer_direct_shipments=None, no_split_shipment=None, postal_code=None, process_days=None, process_inventory_start_time=None, process_inventory_stop_time=None, require_asn=None, send_kit_instead_of_components=None, shipment_cutoff_time_friday=None, shipment_cutoff_time_monday=None, shipment_cutoff_time_saturday=None, shipment_cutoff_time_sunday=None, shipment_cutoff_time_thursday=None, shipment_cutoff_time_tuesday=None, shipment_cutoff_time_wednesday=None, state=None, transport=None):  # noqa: E501
        """DistributionCenter - a model defined in Swagger"""  # noqa: E501

        self._address1 = None
        self._address2 = None
        self._city = None
        self._code = None
        self._country_code = None
        self._default_center = None
        self._default_handles_all_items = None
        self._distribution_center_oid = None
        self._duns = None
        self._estimate_from_distribution_center_oid = None
        self._ftp_password = None
        self._hold_before_shipment_minutes = None
        self._hold_before_transmission = None
        self._hold_auto_order_before_shipment_minutes = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._no_customer_direct_shipments = None
        self._no_split_shipment = None
        self._postal_code = None
        self._process_days = None
        self._process_inventory_start_time = None
        self._process_inventory_stop_time = None
        self._require_asn = None
        self._send_kit_instead_of_components = None
        self._shipment_cutoff_time_friday = None
        self._shipment_cutoff_time_monday = None
        self._shipment_cutoff_time_saturday = None
        self._shipment_cutoff_time_sunday = None
        self._shipment_cutoff_time_thursday = None
        self._shipment_cutoff_time_tuesday = None
        self._shipment_cutoff_time_wednesday = None
        self._state = None
        self._transport = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if code is not None:
            self.code = code
        if country_code is not None:
            self.country_code = country_code
        if default_center is not None:
            self.default_center = default_center
        if default_handles_all_items is not None:
            self.default_handles_all_items = default_handles_all_items
        if distribution_center_oid is not None:
            self.distribution_center_oid = distribution_center_oid
        if duns is not None:
            self.duns = duns
        if estimate_from_distribution_center_oid is not None:
            self.estimate_from_distribution_center_oid = estimate_from_distribution_center_oid
        if ftp_password is not None:
            self.ftp_password = ftp_password
        if hold_before_shipment_minutes is not None:
            self.hold_before_shipment_minutes = hold_before_shipment_minutes
        if hold_before_transmission is not None:
            self.hold_before_transmission = hold_before_transmission
        if hold_auto_order_before_shipment_minutes is not None:
            self.hold_auto_order_before_shipment_minutes = hold_auto_order_before_shipment_minutes
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if name is not None:
            self.name = name
        if no_customer_direct_shipments is not None:
            self.no_customer_direct_shipments = no_customer_direct_shipments
        if no_split_shipment is not None:
            self.no_split_shipment = no_split_shipment
        if postal_code is not None:
            self.postal_code = postal_code
        if process_days is not None:
            self.process_days = process_days
        if process_inventory_start_time is not None:
            self.process_inventory_start_time = process_inventory_start_time
        if process_inventory_stop_time is not None:
            self.process_inventory_stop_time = process_inventory_stop_time
        if require_asn is not None:
            self.require_asn = require_asn
        if send_kit_instead_of_components is not None:
            self.send_kit_instead_of_components = send_kit_instead_of_components
        if shipment_cutoff_time_friday is not None:
            self.shipment_cutoff_time_friday = shipment_cutoff_time_friday
        if shipment_cutoff_time_monday is not None:
            self.shipment_cutoff_time_monday = shipment_cutoff_time_monday
        if shipment_cutoff_time_saturday is not None:
            self.shipment_cutoff_time_saturday = shipment_cutoff_time_saturday
        if shipment_cutoff_time_sunday is not None:
            self.shipment_cutoff_time_sunday = shipment_cutoff_time_sunday
        if shipment_cutoff_time_thursday is not None:
            self.shipment_cutoff_time_thursday = shipment_cutoff_time_thursday
        if shipment_cutoff_time_tuesday is not None:
            self.shipment_cutoff_time_tuesday = shipment_cutoff_time_tuesday
        if shipment_cutoff_time_wednesday is not None:
            self.shipment_cutoff_time_wednesday = shipment_cutoff_time_wednesday
        if state is not None:
            self.state = state
        if transport is not None:
            self.transport = transport

    @property
    def address1(self):
        """Gets the address1 of this DistributionCenter.  # noqa: E501

        Address line 1 of the distribution center  # noqa: E501

        :return: The address1 of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this DistributionCenter.

        Address line 1 of the distribution center  # noqa: E501

        :param address1: The address1 of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this DistributionCenter.  # noqa: E501

        Address line 2 of the distribution center  # noqa: E501

        :return: The address2 of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this DistributionCenter.

        Address line 2 of the distribution center  # noqa: E501

        :param address2: The address2 of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this DistributionCenter.  # noqa: E501

        City of the distribution center  # noqa: E501

        :return: The city of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this DistributionCenter.

        City of the distribution center  # noqa: E501

        :param city: The city of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def code(self):
        """Gets the code of this DistributionCenter.  # noqa: E501

        Unique code for this distribution center  # noqa: E501

        :return: The code of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DistributionCenter.

        Unique code for this distribution center  # noqa: E501

        :param code: The code of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def country_code(self):
        """Gets the country_code of this DistributionCenter.  # noqa: E501

        Country code of the distribution center  # noqa: E501

        :return: The country_code of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this DistributionCenter.

        Country code of the distribution center  # noqa: E501

        :param country_code: The country_code of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def default_center(self):
        """Gets the default_center of this DistributionCenter.  # noqa: E501

        True if this is the default distribution center on the account  # noqa: E501

        :return: The default_center of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._default_center

    @default_center.setter
    def default_center(self, default_center):
        """Sets the default_center of this DistributionCenter.

        True if this is the default distribution center on the account  # noqa: E501

        :param default_center: The default_center of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._default_center = default_center

    @property
    def default_handles_all_items(self):
        """Gets the default_handles_all_items of this DistributionCenter.  # noqa: E501

        True if this distribution center handles all new items by default  # noqa: E501

        :return: The default_handles_all_items of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._default_handles_all_items

    @default_handles_all_items.setter
    def default_handles_all_items(self, default_handles_all_items):
        """Sets the default_handles_all_items of this DistributionCenter.

        True if this distribution center handles all new items by default  # noqa: E501

        :param default_handles_all_items: The default_handles_all_items of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._default_handles_all_items = default_handles_all_items

    @property
    def distribution_center_oid(self):
        """Gets the distribution_center_oid of this DistributionCenter.  # noqa: E501

        Distribution center object identifier  # noqa: E501

        :return: The distribution_center_oid of this DistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._distribution_center_oid

    @distribution_center_oid.setter
    def distribution_center_oid(self, distribution_center_oid):
        """Sets the distribution_center_oid of this DistributionCenter.

        Distribution center object identifier  # noqa: E501

        :param distribution_center_oid: The distribution_center_oid of this DistributionCenter.  # noqa: E501
        :type: int
        """

        self._distribution_center_oid = distribution_center_oid

    @property
    def duns(self):
        """Gets the duns of this DistributionCenter.  # noqa: E501

        DUNS number assigned to this distribution center (EDI)  # noqa: E501

        :return: The duns of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._duns

    @duns.setter
    def duns(self, duns):
        """Sets the duns of this DistributionCenter.

        DUNS number assigned to this distribution center (EDI)  # noqa: E501

        :param duns: The duns of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._duns = duns

    @property
    def estimate_from_distribution_center_oid(self):
        """Gets the estimate_from_distribution_center_oid of this DistributionCenter.  # noqa: E501

        Estimate shipments for this distribution center as if they came from the other distribution center  # noqa: E501

        :return: The estimate_from_distribution_center_oid of this DistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._estimate_from_distribution_center_oid

    @estimate_from_distribution_center_oid.setter
    def estimate_from_distribution_center_oid(self, estimate_from_distribution_center_oid):
        """Sets the estimate_from_distribution_center_oid of this DistributionCenter.

        Estimate shipments for this distribution center as if they came from the other distribution center  # noqa: E501

        :param estimate_from_distribution_center_oid: The estimate_from_distribution_center_oid of this DistributionCenter.  # noqa: E501
        :type: int
        """

        self._estimate_from_distribution_center_oid = estimate_from_distribution_center_oid

    @property
    def ftp_password(self):
        """Gets the ftp_password of this DistributionCenter.  # noqa: E501

        Password associated with the virtual FTP  # noqa: E501

        :return: The ftp_password of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._ftp_password

    @ftp_password.setter
    def ftp_password(self, ftp_password):
        """Sets the ftp_password of this DistributionCenter.

        Password associated with the virtual FTP  # noqa: E501

        :param ftp_password: The ftp_password of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._ftp_password = ftp_password

    @property
    def hold_before_shipment_minutes(self):
        """Gets the hold_before_shipment_minutes of this DistributionCenter.  # noqa: E501

        The number of minutes to hold a shipment  # noqa: E501

        :return: The hold_before_shipment_minutes of this DistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._hold_before_shipment_minutes

    @hold_before_shipment_minutes.setter
    def hold_before_shipment_minutes(self, hold_before_shipment_minutes):
        """Sets the hold_before_shipment_minutes of this DistributionCenter.

        The number of minutes to hold a shipment  # noqa: E501

        :param hold_before_shipment_minutes: The hold_before_shipment_minutes of this DistributionCenter.  # noqa: E501
        :type: int
        """

        self._hold_before_shipment_minutes = hold_before_shipment_minutes

    @property
    def hold_before_transmission(self):
        """Gets the hold_before_transmission of this DistributionCenter.  # noqa: E501

        True if the shipment should be held before transmission and require a manual release  # noqa: E501

        :return: The hold_before_transmission of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._hold_before_transmission

    @hold_before_transmission.setter
    def hold_before_transmission(self, hold_before_transmission):
        """Sets the hold_before_transmission of this DistributionCenter.

        True if the shipment should be held before transmission and require a manual release  # noqa: E501

        :param hold_before_transmission: The hold_before_transmission of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._hold_before_transmission = hold_before_transmission

    @property
    def hold_auto_order_before_shipment_minutes(self):
        """Gets the hold_auto_order_before_shipment_minutes of this DistributionCenter.  # noqa: E501


        :return: The hold_auto_order_before_shipment_minutes of this DistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._hold_auto_order_before_shipment_minutes

    @hold_auto_order_before_shipment_minutes.setter
    def hold_auto_order_before_shipment_minutes(self, hold_auto_order_before_shipment_minutes):
        """Sets the hold_auto_order_before_shipment_minutes of this DistributionCenter.


        :param hold_auto_order_before_shipment_minutes: The hold_auto_order_before_shipment_minutes of this DistributionCenter.  # noqa: E501
        :type: int
        """

        self._hold_auto_order_before_shipment_minutes = hold_auto_order_before_shipment_minutes

    @property
    def latitude(self):
        """Gets the latitude of this DistributionCenter.  # noqa: E501

        Latitude where the distribution center is located  # noqa: E501

        :return: The latitude of this DistributionCenter.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this DistributionCenter.

        Latitude where the distribution center is located  # noqa: E501

        :param latitude: The latitude of this DistributionCenter.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this DistributionCenter.  # noqa: E501

        Longitude where the distribution center is located  # noqa: E501

        :return: The longitude of this DistributionCenter.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this DistributionCenter.

        Longitude where the distribution center is located  # noqa: E501

        :param longitude: The longitude of this DistributionCenter.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def name(self):
        """Gets the name of this DistributionCenter.  # noqa: E501

        Name of this distribution center  # noqa: E501

        :return: The name of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionCenter.

        Name of this distribution center  # noqa: E501

        :param name: The name of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no_customer_direct_shipments(self):
        """Gets the no_customer_direct_shipments of this DistributionCenter.  # noqa: E501

        True if this distribution center does not handle customer direct shipments  # noqa: E501

        :return: The no_customer_direct_shipments of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._no_customer_direct_shipments

    @no_customer_direct_shipments.setter
    def no_customer_direct_shipments(self, no_customer_direct_shipments):
        """Sets the no_customer_direct_shipments of this DistributionCenter.

        True if this distribution center does not handle customer direct shipments  # noqa: E501

        :param no_customer_direct_shipments: The no_customer_direct_shipments of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._no_customer_direct_shipments = no_customer_direct_shipments

    @property
    def no_split_shipment(self):
        """Gets the no_split_shipment of this DistributionCenter.  # noqa: E501

        True if this distribution center is not allowed to participate in a split shipment.  # noqa: E501

        :return: The no_split_shipment of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._no_split_shipment

    @no_split_shipment.setter
    def no_split_shipment(self, no_split_shipment):
        """Sets the no_split_shipment of this DistributionCenter.

        True if this distribution center is not allowed to participate in a split shipment.  # noqa: E501

        :param no_split_shipment: The no_split_shipment of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._no_split_shipment = no_split_shipment

    @property
    def postal_code(self):
        """Gets the postal_code of this DistributionCenter.  # noqa: E501

        Postal code of the distribution center  # noqa: E501

        :return: The postal_code of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this DistributionCenter.

        Postal code of the distribution center  # noqa: E501

        :param postal_code: The postal_code of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def process_days(self):
        """Gets the process_days of this DistributionCenter.  # noqa: E501

        The number of processing days required before an order ships  # noqa: E501

        :return: The process_days of this DistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._process_days

    @process_days.setter
    def process_days(self, process_days):
        """Sets the process_days of this DistributionCenter.

        The number of processing days required before an order ships  # noqa: E501

        :param process_days: The process_days of this DistributionCenter.  # noqa: E501
        :type: int
        """

        self._process_days = process_days

    @property
    def process_inventory_start_time(self):
        """Gets the process_inventory_start_time of this DistributionCenter.  # noqa: E501

        The time (EST) after which inventory updates will be processed  # noqa: E501

        :return: The process_inventory_start_time of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._process_inventory_start_time

    @process_inventory_start_time.setter
    def process_inventory_start_time(self, process_inventory_start_time):
        """Sets the process_inventory_start_time of this DistributionCenter.

        The time (EST) after which inventory updates will be processed  # noqa: E501

        :param process_inventory_start_time: The process_inventory_start_time of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._process_inventory_start_time = process_inventory_start_time

    @property
    def process_inventory_stop_time(self):
        """Gets the process_inventory_stop_time of this DistributionCenter.  # noqa: E501

        The time (EST) before which inventory updates will be processed  # noqa: E501

        :return: The process_inventory_stop_time of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._process_inventory_stop_time

    @process_inventory_stop_time.setter
    def process_inventory_stop_time(self, process_inventory_stop_time):
        """Sets the process_inventory_stop_time of this DistributionCenter.

        The time (EST) before which inventory updates will be processed  # noqa: E501

        :param process_inventory_stop_time: The process_inventory_stop_time of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._process_inventory_stop_time = process_inventory_stop_time

    @property
    def require_asn(self):
        """Gets the require_asn of this DistributionCenter.  # noqa: E501

        True if ASNs are required for this distribution center (EDI)  # noqa: E501

        :return: The require_asn of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._require_asn

    @require_asn.setter
    def require_asn(self, require_asn):
        """Sets the require_asn of this DistributionCenter.

        True if ASNs are required for this distribution center (EDI)  # noqa: E501

        :param require_asn: The require_asn of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._require_asn = require_asn

    @property
    def send_kit_instead_of_components(self):
        """Gets the send_kit_instead_of_components of this DistributionCenter.  # noqa: E501

        True if we should send the kit instead of the components  # noqa: E501

        :return: The send_kit_instead_of_components of this DistributionCenter.  # noqa: E501
        :rtype: bool
        """
        return self._send_kit_instead_of_components

    @send_kit_instead_of_components.setter
    def send_kit_instead_of_components(self, send_kit_instead_of_components):
        """Sets the send_kit_instead_of_components of this DistributionCenter.

        True if we should send the kit instead of the components  # noqa: E501

        :param send_kit_instead_of_components: The send_kit_instead_of_components of this DistributionCenter.  # noqa: E501
        :type: bool
        """

        self._send_kit_instead_of_components = send_kit_instead_of_components

    @property
    def shipment_cutoff_time_friday(self):
        """Gets the shipment_cutoff_time_friday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Friday  # noqa: E501

        :return: The shipment_cutoff_time_friday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_friday

    @shipment_cutoff_time_friday.setter
    def shipment_cutoff_time_friday(self, shipment_cutoff_time_friday):
        """Sets the shipment_cutoff_time_friday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Friday  # noqa: E501

        :param shipment_cutoff_time_friday: The shipment_cutoff_time_friday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_friday = shipment_cutoff_time_friday

    @property
    def shipment_cutoff_time_monday(self):
        """Gets the shipment_cutoff_time_monday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Monday  # noqa: E501

        :return: The shipment_cutoff_time_monday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_monday

    @shipment_cutoff_time_monday.setter
    def shipment_cutoff_time_monday(self, shipment_cutoff_time_monday):
        """Sets the shipment_cutoff_time_monday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Monday  # noqa: E501

        :param shipment_cutoff_time_monday: The shipment_cutoff_time_monday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_monday = shipment_cutoff_time_monday

    @property
    def shipment_cutoff_time_saturday(self):
        """Gets the shipment_cutoff_time_saturday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Saturday  # noqa: E501

        :return: The shipment_cutoff_time_saturday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_saturday

    @shipment_cutoff_time_saturday.setter
    def shipment_cutoff_time_saturday(self, shipment_cutoff_time_saturday):
        """Sets the shipment_cutoff_time_saturday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Saturday  # noqa: E501

        :param shipment_cutoff_time_saturday: The shipment_cutoff_time_saturday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_saturday = shipment_cutoff_time_saturday

    @property
    def shipment_cutoff_time_sunday(self):
        """Gets the shipment_cutoff_time_sunday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Sunday  # noqa: E501

        :return: The shipment_cutoff_time_sunday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_sunday

    @shipment_cutoff_time_sunday.setter
    def shipment_cutoff_time_sunday(self, shipment_cutoff_time_sunday):
        """Sets the shipment_cutoff_time_sunday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Sunday  # noqa: E501

        :param shipment_cutoff_time_sunday: The shipment_cutoff_time_sunday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_sunday = shipment_cutoff_time_sunday

    @property
    def shipment_cutoff_time_thursday(self):
        """Gets the shipment_cutoff_time_thursday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Thursday  # noqa: E501

        :return: The shipment_cutoff_time_thursday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_thursday

    @shipment_cutoff_time_thursday.setter
    def shipment_cutoff_time_thursday(self, shipment_cutoff_time_thursday):
        """Sets the shipment_cutoff_time_thursday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Thursday  # noqa: E501

        :param shipment_cutoff_time_thursday: The shipment_cutoff_time_thursday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_thursday = shipment_cutoff_time_thursday

    @property
    def shipment_cutoff_time_tuesday(self):
        """Gets the shipment_cutoff_time_tuesday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Tuesday  # noqa: E501

        :return: The shipment_cutoff_time_tuesday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_tuesday

    @shipment_cutoff_time_tuesday.setter
    def shipment_cutoff_time_tuesday(self, shipment_cutoff_time_tuesday):
        """Sets the shipment_cutoff_time_tuesday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Tuesday  # noqa: E501

        :param shipment_cutoff_time_tuesday: The shipment_cutoff_time_tuesday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_tuesday = shipment_cutoff_time_tuesday

    @property
    def shipment_cutoff_time_wednesday(self):
        """Gets the shipment_cutoff_time_wednesday of this DistributionCenter.  # noqa: E501

        The time (EST) after which shipments will not be processed on Wednesday  # noqa: E501

        :return: The shipment_cutoff_time_wednesday of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._shipment_cutoff_time_wednesday

    @shipment_cutoff_time_wednesday.setter
    def shipment_cutoff_time_wednesday(self, shipment_cutoff_time_wednesday):
        """Sets the shipment_cutoff_time_wednesday of this DistributionCenter.

        The time (EST) after which shipments will not be processed on Wednesday  # noqa: E501

        :param shipment_cutoff_time_wednesday: The shipment_cutoff_time_wednesday of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._shipment_cutoff_time_wednesday = shipment_cutoff_time_wednesday

    @property
    def state(self):
        """Gets the state of this DistributionCenter.  # noqa: E501

        State of the distribution center  # noqa: E501

        :return: The state of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DistributionCenter.

        State of the distribution center  # noqa: E501

        :param state: The state of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def transport(self):
        """Gets the transport of this DistributionCenter.  # noqa: E501

        Transport mechanism for this distribution center  # noqa: E501

        :return: The transport of this DistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this DistributionCenter.

        Transport mechanism for this distribution center  # noqa: E501

        :param transport: The transport of this DistributionCenter.  # noqa: E501
        :type: str
        """

        self._transport = transport

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DistributionCenter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DistributionCenter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
