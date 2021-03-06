# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.post_subscription_preview_invoice_items_type import POSTSubscriptionPreviewInvoiceItemsType  # noqa: F401,E501
from zuora_client.models.post_subscription_preview_response_type_charge_metrics import POSTSubscriptionPreviewResponseTypeChargeMetrics  # noqa: F401,E501
from zuora_client.models.post_subscription_preview_response_type_credit_memo import POSTSubscriptionPreviewResponseTypeCreditMemo  # noqa: F401,E501


class POSTSubscriptionPreviewResponseType(object):
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
        'amount': 'str',
        'amount_without_tax': 'str',
        'charge_metrics': 'POSTSubscriptionPreviewResponseTypeChargeMetrics',
        'contracted_mrr': 'str',
        'credit_memo': 'POSTSubscriptionPreviewResponseTypeCreditMemo',
        'invoice': 'object',
        'invoice_items': 'list[POSTSubscriptionPreviewInvoiceItemsType]',
        'invoice_target_date': 'date',
        'preview_charge_metrics_response': 'str',
        'success': 'bool',
        'target_date': 'date',
        'tax_amount': 'str',
        'total_contracted_value': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_without_tax': 'amountWithoutTax',
        'charge_metrics': 'chargeMetrics',
        'contracted_mrr': 'contractedMrr',
        'credit_memo': 'creditMemo',
        'invoice': 'invoice',
        'invoice_items': 'invoiceItems',
        'invoice_target_date': 'invoiceTargetDate',
        'preview_charge_metrics_response': 'previewChargeMetricsResponse',
        'success': 'success',
        'target_date': 'targetDate',
        'tax_amount': 'taxAmount',
        'total_contracted_value': 'totalContractedValue'
    }

    def __init__(self, amount=None, amount_without_tax=None, charge_metrics=None, contracted_mrr=None, credit_memo=None, invoice=None, invoice_items=None, invoice_target_date=None, preview_charge_metrics_response=None, success=None, target_date=None, tax_amount=None, total_contracted_value=None):  # noqa: E501
        """POSTSubscriptionPreviewResponseType - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._amount_without_tax = None
        self._charge_metrics = None
        self._contracted_mrr = None
        self._credit_memo = None
        self._invoice = None
        self._invoice_items = None
        self._invoice_target_date = None
        self._preview_charge_metrics_response = None
        self._success = None
        self._target_date = None
        self._tax_amount = None
        self._total_contracted_value = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if amount_without_tax is not None:
            self.amount_without_tax = amount_without_tax
        if charge_metrics is not None:
            self.charge_metrics = charge_metrics
        if contracted_mrr is not None:
            self.contracted_mrr = contracted_mrr
        if credit_memo is not None:
            self.credit_memo = credit_memo
        if invoice is not None:
            self.invoice = invoice
        if invoice_items is not None:
            self.invoice_items = invoice_items
        if invoice_target_date is not None:
            self.invoice_target_date = invoice_target_date
        if preview_charge_metrics_response is not None:
            self.preview_charge_metrics_response = preview_charge_metrics_response
        if success is not None:
            self.success = success
        if target_date is not None:
            self.target_date = target_date
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_contracted_value is not None:
            self.total_contracted_value = total_contracted_value

    @property
    def amount(self):
        """Gets the amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Invoice amount.   # noqa: E501

        :return: The amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this POSTSubscriptionPreviewResponseType.

        Invoice amount.   # noqa: E501

        :param amount: The amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def amount_without_tax(self):
        """Gets the amount_without_tax of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Invoice amount minus tax.   # noqa: E501

        :return: The amount_without_tax of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._amount_without_tax

    @amount_without_tax.setter
    def amount_without_tax(self, amount_without_tax):
        """Sets the amount_without_tax of this POSTSubscriptionPreviewResponseType.

        Invoice amount minus tax.   # noqa: E501

        :param amount_without_tax: The amount_without_tax of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._amount_without_tax = amount_without_tax

    @property
    def charge_metrics(self):
        """Gets the charge_metrics of this POSTSubscriptionPreviewResponseType.  # noqa: E501


        :return: The charge_metrics of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: POSTSubscriptionPreviewResponseTypeChargeMetrics
        """
        return self._charge_metrics

    @charge_metrics.setter
    def charge_metrics(self, charge_metrics):
        """Sets the charge_metrics of this POSTSubscriptionPreviewResponseType.


        :param charge_metrics: The charge_metrics of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: POSTSubscriptionPreviewResponseTypeChargeMetrics
        """

        self._charge_metrics = charge_metrics

    @property
    def contracted_mrr(self):
        """Gets the contracted_mrr of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Monthly recurring revenue of the subscription.   # noqa: E501

        :return: The contracted_mrr of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._contracted_mrr

    @contracted_mrr.setter
    def contracted_mrr(self, contracted_mrr):
        """Sets the contracted_mrr of this POSTSubscriptionPreviewResponseType.

        Monthly recurring revenue of the subscription.   # noqa: E501

        :param contracted_mrr: The contracted_mrr of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._contracted_mrr = contracted_mrr

    @property
    def credit_memo(self):
        """Gets the credit_memo of this POSTSubscriptionPreviewResponseType.  # noqa: E501


        :return: The credit_memo of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: POSTSubscriptionPreviewResponseTypeCreditMemo
        """
        return self._credit_memo

    @credit_memo.setter
    def credit_memo(self, credit_memo):
        """Sets the credit_memo of this POSTSubscriptionPreviewResponseType.


        :param credit_memo: The credit_memo of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: POSTSubscriptionPreviewResponseTypeCreditMemo
        """

        self._credit_memo = credit_memo

    @property
    def invoice(self):
        """Gets the invoice of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Container for invoices.    **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. Also, the response structure is changed and the following invoice related response fields are moved to this **invoice** container:       * amount    * amountWithoutTax    * taxAmount    * invoiceItems    * targetDate    * chargeMetrics       # noqa: E501

        :return: The invoice of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: object
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this POSTSubscriptionPreviewResponseType.

        Container for invoices.    **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. Also, the response structure is changed and the following invoice related response fields are moved to this **invoice** container:       * amount    * amountWithoutTax    * taxAmount    * invoiceItems    * targetDate    * chargeMetrics       # noqa: E501

        :param invoice: The invoice of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: object
        """

        self._invoice = invoice

    @property
    def invoice_items(self):
        """Gets the invoice_items of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Container for invoice items.   # noqa: E501

        :return: The invoice_items of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: list[POSTSubscriptionPreviewInvoiceItemsType]
        """
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, invoice_items):
        """Sets the invoice_items of this POSTSubscriptionPreviewResponseType.

        Container for invoice items.   # noqa: E501

        :param invoice_items: The invoice_items of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: list[POSTSubscriptionPreviewInvoiceItemsType]
        """

        self._invoice_items = invoice_items

    @property
    def invoice_target_date(self):
        """Gets the invoice_target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Date through which charges are calculated on the invoice, as yyyy-mm-dd.  **Note:** This field is only available if you do not specify the Zuora REST API minor version or specify the minor version to 186.0, 187.0, 188.0, 189.0, and 196.0. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   # noqa: E501

        :return: The invoice_target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: date
        """
        return self._invoice_target_date

    @invoice_target_date.setter
    def invoice_target_date(self, invoice_target_date):
        """Sets the invoice_target_date of this POSTSubscriptionPreviewResponseType.

        Date through which charges are calculated on the invoice, as yyyy-mm-dd.  **Note:** This field is only available if you do not specify the Zuora REST API minor version or specify the minor version to 186.0, 187.0, 188.0, 189.0, and 196.0. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   # noqa: E501

        :param invoice_target_date: The invoice_target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: date
        """

        self._invoice_target_date = invoice_target_date

    @property
    def preview_charge_metrics_response(self):
        """Gets the preview_charge_metrics_response of this POSTSubscriptionPreviewResponseType.  # noqa: E501

          # noqa: E501

        :return: The preview_charge_metrics_response of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._preview_charge_metrics_response

    @preview_charge_metrics_response.setter
    def preview_charge_metrics_response(self, preview_charge_metrics_response):
        """Sets the preview_charge_metrics_response of this POSTSubscriptionPreviewResponseType.

          # noqa: E501

        :param preview_charge_metrics_response: The preview_charge_metrics_response of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._preview_charge_metrics_response = preview_charge_metrics_response

    @property
    def success(self):
        """Gets the success of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this POSTSubscriptionPreviewResponseType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def target_date(self):
        """Gets the target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   # noqa: E501

        :return: The target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this POSTSubscriptionPreviewResponseType.

        Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   # noqa: E501

        :param target_date: The target_date of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_amount(self):
        """Gets the tax_amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Tax amount on the invoice.   # noqa: E501

        :return: The tax_amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this POSTSubscriptionPreviewResponseType.

        Tax amount on the invoice.   # noqa: E501

        :param tax_amount: The tax_amount of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def total_contracted_value(self):
        """Gets the total_contracted_value of this POSTSubscriptionPreviewResponseType.  # noqa: E501

        Total contracted value of the subscription.   # noqa: E501

        :return: The total_contracted_value of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :rtype: str
        """
        return self._total_contracted_value

    @total_contracted_value.setter
    def total_contracted_value(self, total_contracted_value):
        """Sets the total_contracted_value of this POSTSubscriptionPreviewResponseType.

        Total contracted value of the subscription.   # noqa: E501

        :param total_contracted_value: The total_contracted_value of this POSTSubscriptionPreviewResponseType.  # noqa: E501
        :type: str
        """

        self._total_contracted_value = total_contracted_value

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
        if issubclass(POSTSubscriptionPreviewResponseType, dict):
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
        if not isinstance(other, POSTSubscriptionPreviewResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
