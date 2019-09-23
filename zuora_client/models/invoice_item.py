# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.invoice_item_object_custom_fields import InvoiceItemObjectCustomFields  # noqa: F401,E501
from zuora_client.models.invoice_item_object_ns_fields import InvoiceItemObjectNSFields  # noqa: F401,E501
from zuora_client.models.invoice_item_taxation_items import InvoiceItemTaxationItems  # noqa: F401,E501


class InvoiceItem(object):
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
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str',
        'applied_to_item_id': 'str',
        'balance': 'float',
        'charge_amount': 'float',
        'charge_description': 'str',
        'charge_id': 'str',
        'charge_name': 'str',
        'id': 'str',
        'product_name': 'str',
        'quantity': 'float',
        'service_end_date': 'date',
        'service_start_date': 'date',
        'subscription_id': 'str',
        'subscription_name': 'str',
        'success': 'bool',
        'tax_amount': 'float',
        'taxation_items': 'InvoiceItemTaxationItems',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS',
        'applied_to_item_id': 'appliedToItemId',
        'balance': 'balance',
        'charge_amount': 'chargeAmount',
        'charge_description': 'chargeDescription',
        'charge_id': 'chargeId',
        'charge_name': 'chargeName',
        'id': 'id',
        'product_name': 'productName',
        'quantity': 'quantity',
        'service_end_date': 'serviceEndDate',
        'service_start_date': 'serviceStartDate',
        'subscription_id': 'subscriptionId',
        'subscription_name': 'subscriptionName',
        'success': 'success',
        'tax_amount': 'taxAmount',
        'taxation_items': 'taxationItems',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None, applied_to_item_id=None, balance=None, charge_amount=None, charge_description=None, charge_id=None, charge_name=None, id=None, product_name=None, quantity=None, service_end_date=None, service_start_date=None, subscription_id=None, subscription_name=None, success=None, tax_amount=None, taxation_items=None, unit_of_measure=None):  # noqa: E501
        """InvoiceItem - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self._applied_to_item_id = None
        self._balance = None
        self._charge_amount = None
        self._charge_description = None
        self._charge_id = None
        self._charge_name = None
        self._id = None
        self._product_name = None
        self._quantity = None
        self._service_end_date = None
        self._service_start_date = None
        self._subscription_id = None
        self._subscription_name = None
        self._success = None
        self._tax_amount = None
        self._taxation_items = None
        self._unit_of_measure = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if applied_to_item_id is not None:
            self.applied_to_item_id = applied_to_item_id
        if balance is not None:
            self.balance = balance
        if charge_amount is not None:
            self.charge_amount = charge_amount
        if charge_description is not None:
            self.charge_description = charge_description
        if charge_id is not None:
            self.charge_id = charge_id
        if charge_name is not None:
            self.charge_name = charge_name
        if id is not None:
            self.id = id
        if product_name is not None:
            self.product_name = product_name
        if quantity is not None:
            self.quantity = quantity
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_name is not None:
            self.subscription_name = subscription_name
        if success is not None:
            self.success = success
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if taxation_items is not None:
            self.taxation_items = taxation_items
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this InvoiceItem.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this InvoiceItem.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this InvoiceItem.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this InvoiceItem.  # noqa: E501

        Status of the invoice item's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this InvoiceItem.

        Status of the invoice item's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this InvoiceItem.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this InvoiceItem.  # noqa: E501

        Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this InvoiceItem.

        Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this InvoiceItem.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def applied_to_item_id(self):
        """Gets the applied_to_item_id of this InvoiceItem.  # noqa: E501

        The unique ID of the invoice item that the discount charge is applied to.  # noqa: E501

        :return: The applied_to_item_id of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._applied_to_item_id

    @applied_to_item_id.setter
    def applied_to_item_id(self, applied_to_item_id):
        """Sets the applied_to_item_id of this InvoiceItem.

        The unique ID of the invoice item that the discount charge is applied to.  # noqa: E501

        :param applied_to_item_id: The applied_to_item_id of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._applied_to_item_id = applied_to_item_id

    @property
    def balance(self):
        """Gets the balance of this InvoiceItem.  # noqa: E501

        The balance of the invoice item.  # noqa: E501

        :return: The balance of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this InvoiceItem.

        The balance of the invoice item.  # noqa: E501

        :param balance: The balance of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def charge_amount(self):
        """Gets the charge_amount of this InvoiceItem.  # noqa: E501

        The amount of the charge. This amount does not include taxes regardless if the charge's tax mode is inclusive or exclusive.  # noqa: E501

        :return: The charge_amount of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this InvoiceItem.

        The amount of the charge. This amount does not include taxes regardless if the charge's tax mode is inclusive or exclusive.  # noqa: E501

        :param charge_amount: The charge_amount of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_amount = charge_amount

    @property
    def charge_description(self):
        """Gets the charge_description of this InvoiceItem.  # noqa: E501

        Description of the charge.  # noqa: E501

        :return: The charge_description of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_description

    @charge_description.setter
    def charge_description(self, charge_description):
        """Sets the charge_description of this InvoiceItem.

        Description of the charge.  # noqa: E501

        :param charge_description: The charge_description of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_description = charge_description

    @property
    def charge_id(self):
        """Gets the charge_id of this InvoiceItem.  # noqa: E501

        ID of the charge.  # noqa: E501

        :return: The charge_id of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this InvoiceItem.

        ID of the charge.  # noqa: E501

        :param charge_id: The charge_id of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_id = charge_id

    @property
    def charge_name(self):
        """Gets the charge_name of this InvoiceItem.  # noqa: E501

        Name of the charge.  # noqa: E501

        :return: The charge_name of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """Sets the charge_name of this InvoiceItem.

        Name of the charge.  # noqa: E501

        :param charge_name: The charge_name of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_name = charge_name

    @property
    def id(self):
        """Gets the id of this InvoiceItem.  # noqa: E501

        Item ID.  # noqa: E501

        :return: The id of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceItem.

        Item ID.  # noqa: E501

        :param id: The id of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def product_name(self):
        """Gets the product_name of this InvoiceItem.  # noqa: E501

        Name of the product associated with this item.  # noqa: E501

        :return: The product_name of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this InvoiceItem.

        Name of the product associated with this item.  # noqa: E501

        :param product_name: The product_name of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def quantity(self):
        """Gets the quantity of this InvoiceItem.  # noqa: E501

        Quantity of this item, in the configured unit of measure for the charge.  # noqa: E501

        :return: The quantity of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvoiceItem.

        Quantity of this item, in the configured unit of measure for the charge.  # noqa: E501

        :param quantity: The quantity of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def service_end_date(self):
        """Gets the service_end_date of this InvoiceItem.  # noqa: E501

        End date of the service period for this item, i.e., the last day of the service period, as _yyyy-mm-dd_.  # noqa: E501

        :return: The service_end_date of this InvoiceItem.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this InvoiceItem.

        End date of the service period for this item, i.e., the last day of the service period, as _yyyy-mm-dd_.  # noqa: E501

        :param service_end_date: The service_end_date of this InvoiceItem.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

    @property
    def service_start_date(self):
        """Gets the service_start_date of this InvoiceItem.  # noqa: E501

        Start date of the service period for this item, as _yyyy-mm-dd_. For a one-time fee item, the date of the charge.  # noqa: E501

        :return: The service_start_date of this InvoiceItem.  # noqa: E501
        :rtype: date
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this InvoiceItem.

        Start date of the service period for this item, as _yyyy-mm-dd_. For a one-time fee item, the date of the charge.  # noqa: E501

        :param service_start_date: The service_start_date of this InvoiceItem.  # noqa: E501
        :type: date
        """

        self._service_start_date = service_start_date

    @property
    def subscription_id(self):
        """Gets the subscription_id of this InvoiceItem.  # noqa: E501

        ID of the subscription for this item.  # noqa: E501

        :return: The subscription_id of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this InvoiceItem.

        ID of the subscription for this item.  # noqa: E501

        :param subscription_id: The subscription_id of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def subscription_name(self):
        """Gets the subscription_name of this InvoiceItem.  # noqa: E501

        Name of the subscription for this item.  # noqa: E501

        :return: The subscription_name of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this InvoiceItem.

        Name of the subscription for this item.  # noqa: E501

        :param subscription_name: The subscription_name of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._subscription_name = subscription_name

    @property
    def success(self):
        """Gets the success of this InvoiceItem.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this InvoiceItem.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InvoiceItem.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this InvoiceItem.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def tax_amount(self):
        """Gets the tax_amount of this InvoiceItem.  # noqa: E501

        Tax applied to the charge.  # noqa: E501

        :return: The tax_amount of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this InvoiceItem.

        Tax applied to the charge.  # noqa: E501

        :param tax_amount: The tax_amount of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def taxation_items(self):
        """Gets the taxation_items of this InvoiceItem.  # noqa: E501


        :return: The taxation_items of this InvoiceItem.  # noqa: E501
        :rtype: InvoiceItemTaxationItems
        """
        return self._taxation_items

    @taxation_items.setter
    def taxation_items(self, taxation_items):
        """Sets the taxation_items of this InvoiceItem.


        :param taxation_items: The taxation_items of this InvoiceItem.  # noqa: E501
        :type: InvoiceItemTaxationItems
        """

        self._taxation_items = taxation_items

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this InvoiceItem.  # noqa: E501

        Unit used to measure. consumption.  # noqa: E501

        :return: The unit_of_measure of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this InvoiceItem.

        Unit used to measure. consumption.  # noqa: E501

        :param unit_of_measure: The unit_of_measure of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if issubclass(InvoiceItem, dict):
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
        if not isinstance(other, InvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
