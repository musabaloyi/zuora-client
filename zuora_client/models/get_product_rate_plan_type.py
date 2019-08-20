# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_product_rate_plan_charge_type import GETProductRatePlanChargeType  # noqa: F401,E501
from zuora_client.models.product_rate_plan_object_custom_fields import ProductRatePlanObjectCustomFields  # noqa: F401,E501
from zuora_client.models.product_rate_plan_object_ns_fields import ProductRatePlanObjectNSFields  # noqa: F401,E501


class GETProductRatePlanType(object):
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
        'billing_period__ns': 'str',
        'class__ns': 'str',
        'department__ns': 'str',
        'include_children__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'item_type__ns': 'str',
        'location__ns': 'str',
        'multi_currency_price__ns': 'str',
        'price__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'description': 'str',
        'effective_end_date': 'date',
        'effective_start_date': 'date',
        'id': 'str',
        'name': 'str',
        'product_rate_plan_charges': 'list[GETProductRatePlanChargeType]',
        'status': 'str'
    }

    attribute_map = {
        'billing_period__ns': 'BillingPeriod__NS',
        'class__ns': 'Class__NS',
        'department__ns': 'Department__NS',
        'include_children__ns': 'IncludeChildren__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'item_type__ns': 'ItemType__NS',
        'location__ns': 'Location__NS',
        'multi_currency_price__ns': 'MultiCurrencyPrice__NS',
        'price__ns': 'Price__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'description': 'description',
        'effective_end_date': 'effectiveEndDate',
        'effective_start_date': 'effectiveStartDate',
        'id': 'id',
        'name': 'name',
        'product_rate_plan_charges': 'productRatePlanCharges',
        'status': 'status'
    }

    def __init__(self, billing_period__ns=None, class__ns=None, department__ns=None, include_children__ns=None, integration_id__ns=None, integration_status__ns=None, item_type__ns=None, location__ns=None, multi_currency_price__ns=None, price__ns=None, subsidiary__ns=None, sync_date__ns=None, description=None, effective_end_date=None, effective_start_date=None, id=None, name=None, product_rate_plan_charges=None, status=None):  # noqa: E501
        """GETProductRatePlanType - a model defined in Swagger"""  # noqa: E501

        self._billing_period__ns = None
        self._class__ns = None
        self._department__ns = None
        self._include_children__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._item_type__ns = None
        self._location__ns = None
        self._multi_currency_price__ns = None
        self._price__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._description = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._id = None
        self._name = None
        self._product_rate_plan_charges = None
        self._status = None
        self.discriminator = None

        if billing_period__ns is not None:
            self.billing_period__ns = billing_period__ns
        if class__ns is not None:
            self.class__ns = class__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if include_children__ns is not None:
            self.include_children__ns = include_children__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if item_type__ns is not None:
            self.item_type__ns = item_type__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if multi_currency_price__ns is not None:
            self.multi_currency_price__ns = multi_currency_price__ns
        if price__ns is not None:
            self.price__ns = price__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if description is not None:
            self.description = description
        if effective_end_date is not None:
            self.effective_end_date = effective_end_date
        if effective_start_date is not None:
            self.effective_start_date = effective_start_date
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if product_rate_plan_charges is not None:
            self.product_rate_plan_charges = product_rate_plan_charges
        if status is not None:
            self.status = status

    @property
    def billing_period__ns(self):
        """Gets the billing_period__ns of this GETProductRatePlanType.  # noqa: E501

        Billing period associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The billing_period__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._billing_period__ns

    @billing_period__ns.setter
    def billing_period__ns(self, billing_period__ns):
        """Sets the billing_period__ns of this GETProductRatePlanType.

        Billing period associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param billing_period__ns: The billing_period__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Monthly", "Quarterly", "Annual", "Semi-Annual"]  # noqa: E501
        if billing_period__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period__ns, allowed_values)
            )

        self._billing_period__ns = billing_period__ns

    @property
    def class__ns(self):
        """Gets the class__ns of this GETProductRatePlanType.  # noqa: E501

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this GETProductRatePlanType.

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if class__ns is not None and len(class__ns) > 255:
            raise ValueError("Invalid value for `class__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._class__ns = class__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this GETProductRatePlanType.  # noqa: E501

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this GETProductRatePlanType.

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if department__ns is not None and len(department__ns) > 255:
            raise ValueError("Invalid value for `department__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._department__ns = department__ns

    @property
    def include_children__ns(self):
        """Gets the include_children__ns of this GETProductRatePlanType.  # noqa: E501

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The include_children__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._include_children__ns

    @include_children__ns.setter
    def include_children__ns(self, include_children__ns):
        """Sets the include_children__ns of this GETProductRatePlanType.

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param include_children__ns: The include_children__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Yes", "No"]  # noqa: E501
        if include_children__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `include_children__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(include_children__ns, allowed_values)
            )

        self._include_children__ns = include_children__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this GETProductRatePlanType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this GETProductRatePlanType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this GETProductRatePlanType.  # noqa: E501

        Status of the product rate plan's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this GETProductRatePlanType.

        Status of the product rate plan's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def item_type__ns(self):
        """Gets the item_type__ns of this GETProductRatePlanType.  # noqa: E501

        Type of item that is created in NetSuite for the product rate plan. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The item_type__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._item_type__ns

    @item_type__ns.setter
    def item_type__ns(self, item_type__ns):
        """Sets the item_type__ns of this GETProductRatePlanType.

        Type of item that is created in NetSuite for the product rate plan. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param item_type__ns: The item_type__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inventory", "Non Inventory", "Service"]  # noqa: E501
        if item_type__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `item_type__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(item_type__ns, allowed_values)
            )

        self._item_type__ns = item_type__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this GETProductRatePlanType.  # noqa: E501

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this GETProductRatePlanType.

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if location__ns is not None and len(location__ns) > 255:
            raise ValueError("Invalid value for `location__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._location__ns = location__ns

    @property
    def multi_currency_price__ns(self):
        """Gets the multi_currency_price__ns of this GETProductRatePlanType.  # noqa: E501

        Multi-currency price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The multi_currency_price__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._multi_currency_price__ns

    @multi_currency_price__ns.setter
    def multi_currency_price__ns(self, multi_currency_price__ns):
        """Sets the multi_currency_price__ns of this GETProductRatePlanType.

        Multi-currency price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param multi_currency_price__ns: The multi_currency_price__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if multi_currency_price__ns is not None and len(multi_currency_price__ns) > 255:
            raise ValueError("Invalid value for `multi_currency_price__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._multi_currency_price__ns = multi_currency_price__ns

    @property
    def price__ns(self):
        """Gets the price__ns of this GETProductRatePlanType.  # noqa: E501

        Price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The price__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._price__ns

    @price__ns.setter
    def price__ns(self, price__ns):
        """Sets the price__ns of this GETProductRatePlanType.

        Price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param price__ns: The price__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if price__ns is not None and len(price__ns) > 255:
            raise ValueError("Invalid value for `price__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._price__ns = price__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this GETProductRatePlanType.  # noqa: E501

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this GETProductRatePlanType.

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if subsidiary__ns is not None and len(subsidiary__ns) > 255:
            raise ValueError("Invalid value for `subsidiary__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this GETProductRatePlanType.  # noqa: E501

        Date when the product rate plan was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this GETProductRatePlanType.

        Date when the product rate plan was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def description(self):
        """Gets the description of this GETProductRatePlanType.  # noqa: E501

        Rate plan description.   # noqa: E501

        :return: The description of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GETProductRatePlanType.

        Rate plan description.   # noqa: E501

        :param description: The description of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this GETProductRatePlanType.  # noqa: E501

        Final date the rate plan is active, as `yyyy-mm-dd`. After this date, the rate plan status is `Expired`.   # noqa: E501

        :return: The effective_end_date of this GETProductRatePlanType.  # noqa: E501
        :rtype: date
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this GETProductRatePlanType.

        Final date the rate plan is active, as `yyyy-mm-dd`. After this date, the rate plan status is `Expired`.   # noqa: E501

        :param effective_end_date: The effective_end_date of this GETProductRatePlanType.  # noqa: E501
        :type: date
        """

        self._effective_end_date = effective_end_date

    @property
    def effective_start_date(self):
        """Gets the effective_start_date of this GETProductRatePlanType.  # noqa: E501

        First date the rate plan is active (i.e., available to be subscribed to), as `yyyy-mm-dd`.  Before this date, the status is `NotStarted`.   # noqa: E501

        :return: The effective_start_date of this GETProductRatePlanType.  # noqa: E501
        :rtype: date
        """
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, effective_start_date):
        """Sets the effective_start_date of this GETProductRatePlanType.

        First date the rate plan is active (i.e., available to be subscribed to), as `yyyy-mm-dd`.  Before this date, the status is `NotStarted`.   # noqa: E501

        :param effective_start_date: The effective_start_date of this GETProductRatePlanType.  # noqa: E501
        :type: date
        """

        self._effective_start_date = effective_start_date

    @property
    def id(self):
        """Gets the id of this GETProductRatePlanType.  # noqa: E501

        Unique product rate-plan charge ID.   # noqa: E501

        :return: The id of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETProductRatePlanType.

        Unique product rate-plan charge ID.   # noqa: E501

        :param id: The id of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GETProductRatePlanType.  # noqa: E501

        Name of the product rate-plan charge. (Not required to be unique.)   # noqa: E501

        :return: The name of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GETProductRatePlanType.

        Name of the product rate-plan charge. (Not required to be unique.)   # noqa: E501

        :param name: The name of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_rate_plan_charges(self):
        """Gets the product_rate_plan_charges of this GETProductRatePlanType.  # noqa: E501

        Field attributes describing the product rate plan charges:   # noqa: E501

        :return: The product_rate_plan_charges of this GETProductRatePlanType.  # noqa: E501
        :rtype: list[GETProductRatePlanChargeType]
        """
        return self._product_rate_plan_charges

    @product_rate_plan_charges.setter
    def product_rate_plan_charges(self, product_rate_plan_charges):
        """Sets the product_rate_plan_charges of this GETProductRatePlanType.

        Field attributes describing the product rate plan charges:   # noqa: E501

        :param product_rate_plan_charges: The product_rate_plan_charges of this GETProductRatePlanType.  # noqa: E501
        :type: list[GETProductRatePlanChargeType]
        """

        self._product_rate_plan_charges = product_rate_plan_charges

    @property
    def status(self):
        """Gets the status of this GETProductRatePlanType.  # noqa: E501

        Possible vales are: `Active`, `Expired`, `NotStarted`.   # noqa: E501

        :return: The status of this GETProductRatePlanType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETProductRatePlanType.

        Possible vales are: `Active`, `Expired`, `NotStarted`.   # noqa: E501

        :param status: The status of this GETProductRatePlanType.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GETProductRatePlanType, dict):
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
        if not isinstance(other, GETProductRatePlanType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other