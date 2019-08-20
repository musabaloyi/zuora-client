# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.invoice_object_custom_fields import InvoiceObjectCustomFields  # noqa: F401,E501
from zuora_client.models.invoice_object_ns_fields import InvoiceObjectNSFields  # noqa: F401,E501


class PutInvoiceResponseType(object):
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
        'account_id': 'str',
        'amount': 'float',
        'auto_pay': 'bool',
        'balance': 'float',
        'cancelled_by_id': 'str',
        'cancelled_on': 'datetime',
        'comment': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'credit_balance_adjustment_amount': 'float',
        'currency': 'str',
        'due_date': 'date',
        'id': 'str',
        'invoice_date': 'date',
        'number': 'str',
        'posted_by_id': 'str',
        'posted_on': 'datetime',
        'status': 'str',
        'success': 'bool',
        'target_date': 'date',
        'tax_amount': 'float',
        'total_tax_exempt_amount': 'float',
        'transferred_to_accounting': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS',
        'account_id': 'accountId',
        'amount': 'amount',
        'auto_pay': 'autoPay',
        'balance': 'balance',
        'cancelled_by_id': 'cancelledById',
        'cancelled_on': 'cancelledOn',
        'comment': 'comment',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'credit_balance_adjustment_amount': 'creditBalanceAdjustmentAmount',
        'currency': 'currency',
        'due_date': 'dueDate',
        'id': 'id',
        'invoice_date': 'invoiceDate',
        'number': 'number',
        'posted_by_id': 'postedById',
        'posted_on': 'postedOn',
        'status': 'status',
        'success': 'success',
        'target_date': 'targetDate',
        'tax_amount': 'taxAmount',
        'total_tax_exempt_amount': 'totalTaxExemptAmount',
        'transferred_to_accounting': 'transferredToAccounting',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None, account_id=None, amount=None, auto_pay=None, balance=None, cancelled_by_id=None, cancelled_on=None, comment=None, created_by_id=None, created_date=None, credit_balance_adjustment_amount=None, currency=None, due_date=None, id=None, invoice_date=None, number=None, posted_by_id=None, posted_on=None, status=None, success=None, target_date=None, tax_amount=None, total_tax_exempt_amount=None, transferred_to_accounting=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """PutInvoiceResponseType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self._account_id = None
        self._amount = None
        self._auto_pay = None
        self._balance = None
        self._cancelled_by_id = None
        self._cancelled_on = None
        self._comment = None
        self._created_by_id = None
        self._created_date = None
        self._credit_balance_adjustment_amount = None
        self._currency = None
        self._due_date = None
        self._id = None
        self._invoice_date = None
        self._number = None
        self._posted_by_id = None
        self._posted_on = None
        self._status = None
        self._success = None
        self._target_date = None
        self._tax_amount = None
        self._total_tax_exempt_amount = None
        self._transferred_to_accounting = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if balance is not None:
            self.balance = balance
        if cancelled_by_id is not None:
            self.cancelled_by_id = cancelled_by_id
        if cancelled_on is not None:
            self.cancelled_on = cancelled_on
        if comment is not None:
            self.comment = comment
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if credit_balance_adjustment_amount is not None:
            self.credit_balance_adjustment_amount = credit_balance_adjustment_amount
        if currency is not None:
            self.currency = currency
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if number is not None:
            self.number = number
        if posted_by_id is not None:
            self.posted_by_id = posted_by_id
        if posted_on is not None:
            self.posted_on = posted_on
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success
        if target_date is not None:
            self.target_date = target_date
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_tax_exempt_amount is not None:
            self.total_tax_exempt_amount = total_tax_exempt_amount
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this PutInvoiceResponseType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this PutInvoiceResponseType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this PutInvoiceResponseType.  # noqa: E501

        Status of the invoice's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this PutInvoiceResponseType.

        Status of the invoice's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this PutInvoiceResponseType.  # noqa: E501

        Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this PutInvoiceResponseType.

        Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def account_id(self):
        """Gets the account_id of this PutInvoiceResponseType.  # noqa: E501

        The ID of the customer account associated with the invoice.   # noqa: E501

        :return: The account_id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PutInvoiceResponseType.

        The ID of the customer account associated with the invoice.   # noqa: E501

        :param account_id: The account_id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this PutInvoiceResponseType.  # noqa: E501

        The total amount of the invoice.   # noqa: E501

        :return: The amount of this PutInvoiceResponseType.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PutInvoiceResponseType.

        The total amount of the invoice.   # noqa: E501

        :param amount: The amount of this PutInvoiceResponseType.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def auto_pay(self):
        """Gets the auto_pay of this PutInvoiceResponseType.  # noqa: E501

        Whether invoices are automatically picked up for processing in the corresponding payment run.    # noqa: E501

        :return: The auto_pay of this PutInvoiceResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this PutInvoiceResponseType.

        Whether invoices are automatically picked up for processing in the corresponding payment run.    # noqa: E501

        :param auto_pay: The auto_pay of this PutInvoiceResponseType.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def balance(self):
        """Gets the balance of this PutInvoiceResponseType.  # noqa: E501

        The balance of the invoice.   # noqa: E501

        :return: The balance of this PutInvoiceResponseType.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this PutInvoiceResponseType.

        The balance of the invoice.   # noqa: E501

        :param balance: The balance of this PutInvoiceResponseType.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def cancelled_by_id(self):
        """Gets the cancelled_by_id of this PutInvoiceResponseType.  # noqa: E501

        The ID of the Zuora user who cancelled the invoice.   # noqa: E501

        :return: The cancelled_by_id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_by_id

    @cancelled_by_id.setter
    def cancelled_by_id(self, cancelled_by_id):
        """Sets the cancelled_by_id of this PutInvoiceResponseType.

        The ID of the Zuora user who cancelled the invoice.   # noqa: E501

        :param cancelled_by_id: The cancelled_by_id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._cancelled_by_id = cancelled_by_id

    @property
    def cancelled_on(self):
        """Gets the cancelled_on of this PutInvoiceResponseType.  # noqa: E501

        The date and time when the invoice was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The cancelled_on of this PutInvoiceResponseType.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled_on

    @cancelled_on.setter
    def cancelled_on(self, cancelled_on):
        """Sets the cancelled_on of this PutInvoiceResponseType.

        The date and time when the invoice was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param cancelled_on: The cancelled_on of this PutInvoiceResponseType.  # noqa: E501
        :type: datetime
        """

        self._cancelled_on = cancelled_on

    @property
    def comment(self):
        """Gets the comment of this PutInvoiceResponseType.  # noqa: E501

        Comments about the invoice.    # noqa: E501

        :return: The comment of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PutInvoiceResponseType.

        Comments about the invoice.    # noqa: E501

        :param comment: The comment of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PutInvoiceResponseType.  # noqa: E501

        The ID of the Zuora user who created the invoice.   # noqa: E501

        :return: The created_by_id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PutInvoiceResponseType.

        The ID of the Zuora user who created the invoice.   # noqa: E501

        :param created_by_id: The created_by_id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this PutInvoiceResponseType.  # noqa: E501

        The date and time when the invoice was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this PutInvoiceResponseType.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PutInvoiceResponseType.

        The date and time when the invoice was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this PutInvoiceResponseType.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_balance_adjustment_amount(self):
        """Gets the credit_balance_adjustment_amount of this PutInvoiceResponseType.  # noqa: E501

        **Note:** This filed is only available if you have the Credit Balance feature enabled and the Invoice Settlement feature disabled.  The currency amount of the adjustment applied to the customer's credit balance.   # noqa: E501

        :return: The credit_balance_adjustment_amount of this PutInvoiceResponseType.  # noqa: E501
        :rtype: float
        """
        return self._credit_balance_adjustment_amount

    @credit_balance_adjustment_amount.setter
    def credit_balance_adjustment_amount(self, credit_balance_adjustment_amount):
        """Sets the credit_balance_adjustment_amount of this PutInvoiceResponseType.

        **Note:** This filed is only available if you have the Credit Balance feature enabled and the Invoice Settlement feature disabled.  The currency amount of the adjustment applied to the customer's credit balance.   # noqa: E501

        :param credit_balance_adjustment_amount: The credit_balance_adjustment_amount of this PutInvoiceResponseType.  # noqa: E501
        :type: float
        """

        self._credit_balance_adjustment_amount = credit_balance_adjustment_amount

    @property
    def currency(self):
        """Gets the currency of this PutInvoiceResponseType.  # noqa: E501

        A currency defined in the web-based UI administrative settings.   # noqa: E501

        :return: The currency of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PutInvoiceResponseType.

        A currency defined in the web-based UI administrative settings.   # noqa: E501

        :param currency: The currency of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def due_date(self):
        """Gets the due_date of this PutInvoiceResponseType.  # noqa: E501

        The date by which the payment for this invoice is due.    # noqa: E501

        :return: The due_date of this PutInvoiceResponseType.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PutInvoiceResponseType.

        The date by which the payment for this invoice is due.    # noqa: E501

        :param due_date: The due_date of this PutInvoiceResponseType.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this PutInvoiceResponseType.  # noqa: E501

        The unique ID of the invoice.   # noqa: E501

        :return: The id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutInvoiceResponseType.

        The unique ID of the invoice.   # noqa: E501

        :param id: The id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_date(self):
        """Gets the invoice_date of this PutInvoiceResponseType.  # noqa: E501

        The date on which to generate the invoice.   # noqa: E501

        :return: The invoice_date of this PutInvoiceResponseType.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this PutInvoiceResponseType.

        The date on which to generate the invoice.   # noqa: E501

        :param invoice_date: The invoice_date of this PutInvoiceResponseType.  # noqa: E501
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def number(self):
        """Gets the number of this PutInvoiceResponseType.  # noqa: E501

        The unique identification number of the invoice.   # noqa: E501

        :return: The number of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PutInvoiceResponseType.

        The unique identification number of the invoice.   # noqa: E501

        :param number: The number of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def posted_by_id(self):
        """Gets the posted_by_id of this PutInvoiceResponseType.  # noqa: E501

        The ID of the Zuora user who posted the invoice.   # noqa: E501

        :return: The posted_by_id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._posted_by_id

    @posted_by_id.setter
    def posted_by_id(self, posted_by_id):
        """Sets the posted_by_id of this PutInvoiceResponseType.

        The ID of the Zuora user who posted the invoice.   # noqa: E501

        :param posted_by_id: The posted_by_id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._posted_by_id = posted_by_id

    @property
    def posted_on(self):
        """Gets the posted_on of this PutInvoiceResponseType.  # noqa: E501

        The date and time when the invoice was posted, in `yyyy-mm-dd hh:mm:ss` format.    # noqa: E501

        :return: The posted_on of this PutInvoiceResponseType.  # noqa: E501
        :rtype: datetime
        """
        return self._posted_on

    @posted_on.setter
    def posted_on(self, posted_on):
        """Sets the posted_on of this PutInvoiceResponseType.

        The date and time when the invoice was posted, in `yyyy-mm-dd hh:mm:ss` format.    # noqa: E501

        :param posted_on: The posted_on of this PutInvoiceResponseType.  # noqa: E501
        :type: datetime
        """

        self._posted_on = posted_on

    @property
    def status(self):
        """Gets the status of this PutInvoiceResponseType.  # noqa: E501

        The status of the invoice.   # noqa: E501

        :return: The status of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PutInvoiceResponseType.

        The status of the invoice.   # noqa: E501

        :param status: The status of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Posted", "Canceled", "Error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def success(self):
        """Gets the success of this PutInvoiceResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this PutInvoiceResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PutInvoiceResponseType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this PutInvoiceResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def target_date(self):
        """Gets the target_date of this PutInvoiceResponseType.  # noqa: E501

        The target date for the invoice, in `yyyy-mm-dd` format. For example, 2017-07-20.    # noqa: E501

        :return: The target_date of this PutInvoiceResponseType.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this PutInvoiceResponseType.

        The target date for the invoice, in `yyyy-mm-dd` format. For example, 2017-07-20.    # noqa: E501

        :param target_date: The target_date of this PutInvoiceResponseType.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PutInvoiceResponseType.  # noqa: E501

        The amount of taxation.   # noqa: E501

        :return: The tax_amount of this PutInvoiceResponseType.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PutInvoiceResponseType.

        The amount of taxation.   # noqa: E501

        :param tax_amount: The tax_amount of this PutInvoiceResponseType.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_tax_exempt_amount(self):
        """Gets the total_tax_exempt_amount of this PutInvoiceResponseType.  # noqa: E501

        The total amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :return: The total_tax_exempt_amount of this PutInvoiceResponseType.  # noqa: E501
        :rtype: float
        """
        return self._total_tax_exempt_amount

    @total_tax_exempt_amount.setter
    def total_tax_exempt_amount(self, total_tax_exempt_amount):
        """Sets the total_tax_exempt_amount of this PutInvoiceResponseType.

        The total amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :param total_tax_exempt_amount: The total_tax_exempt_amount of this PutInvoiceResponseType.  # noqa: E501
        :type: float
        """

        self._total_tax_exempt_amount = total_tax_exempt_amount

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this PutInvoiceResponseType.  # noqa: E501

        Whether the invoice was transferred to an external accounting system.   # noqa: E501

        :return: The transferred_to_accounting of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this PutInvoiceResponseType.

        Whether the invoice was transferred to an external accounting system.   # noqa: E501

        :param transferred_to_accounting: The transferred_to_accounting of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Processing", "Yes", "Error", "Ignore"]  # noqa: E501
        if transferred_to_accounting not in allowed_values:
            raise ValueError(
                "Invalid value for `transferred_to_accounting` ({0}), must be one of {1}"  # noqa: E501
                .format(transferred_to_accounting, allowed_values)
            )

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this PutInvoiceResponseType.  # noqa: E501

        The ID of the Zuora user who last updated the invoice.   # noqa: E501

        :return: The updated_by_id of this PutInvoiceResponseType.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this PutInvoiceResponseType.

        The ID of the Zuora user who last updated the invoice.   # noqa: E501

        :param updated_by_id: The updated_by_id of this PutInvoiceResponseType.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this PutInvoiceResponseType.  # noqa: E501

        The date and time when the invoice was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :return: The updated_date of this PutInvoiceResponseType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this PutInvoiceResponseType.

        The date and time when the invoice was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :param updated_date: The updated_date of this PutInvoiceResponseType.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(PutInvoiceResponseType, dict):
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
        if not isinstance(other, PutInvoiceResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other