# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.credit_memo_response_type import CreditMemoResponseType  # noqa: F401,E501
from zuora_client.models.invoice_response_type import InvoiceResponseType  # noqa: F401,E501


class GenerateBillingDocumentResponseType(object):
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
        'credit_memos': 'list[CreditMemoResponseType]',
        'invoices': 'list[InvoiceResponseType]',
        'success': 'bool'
    }

    attribute_map = {
        'credit_memos': 'creditMemos',
        'invoices': 'invoices',
        'success': 'success'
    }

    def __init__(self, credit_memos=None, invoices=None, success=None):  # noqa: E501
        """GenerateBillingDocumentResponseType - a model defined in Swagger"""  # noqa: E501

        self._credit_memos = None
        self._invoices = None
        self._success = None
        self.discriminator = None

        if credit_memos is not None:
            self.credit_memos = credit_memos
        if invoices is not None:
            self.invoices = invoices
        if success is not None:
            self.success = success

    @property
    def credit_memos(self):
        """Gets the credit_memos of this GenerateBillingDocumentResponseType.  # noqa: E501

        Container for generated credit memos.  **Note:** This container is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The credit_memos of this GenerateBillingDocumentResponseType.  # noqa: E501
        :rtype: list[CreditMemoResponseType]
        """
        return self._credit_memos

    @credit_memos.setter
    def credit_memos(self, credit_memos):
        """Sets the credit_memos of this GenerateBillingDocumentResponseType.

        Container for generated credit memos.  **Note:** This container is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param credit_memos: The credit_memos of this GenerateBillingDocumentResponseType.  # noqa: E501
        :type: list[CreditMemoResponseType]
        """

        self._credit_memos = credit_memos

    @property
    def invoices(self):
        """Gets the invoices of this GenerateBillingDocumentResponseType.  # noqa: E501

        Container for generated invoics.   # noqa: E501

        :return: The invoices of this GenerateBillingDocumentResponseType.  # noqa: E501
        :rtype: list[InvoiceResponseType]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this GenerateBillingDocumentResponseType.

        Container for generated invoics.   # noqa: E501

        :param invoices: The invoices of this GenerateBillingDocumentResponseType.  # noqa: E501
        :type: list[InvoiceResponseType]
        """

        self._invoices = invoices

    @property
    def success(self):
        """Gets the success of this GenerateBillingDocumentResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this GenerateBillingDocumentResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GenerateBillingDocumentResponseType.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this GenerateBillingDocumentResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(GenerateBillingDocumentResponseType, dict):
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
        if not isinstance(other, GenerateBillingDocumentResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
