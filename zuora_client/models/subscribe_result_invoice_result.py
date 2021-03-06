# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.subscribe_result_invoice_result_invoice import SubscribeResultInvoiceResultInvoice  # noqa: F401,E501


class SubscribeResultInvoiceResult(object):
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
        'invoice': 'list[SubscribeResultInvoiceResultInvoice]'
    }

    attribute_map = {
        'invoice': 'Invoice'
    }

    def __init__(self, invoice=None):  # noqa: E501
        """SubscribeResultInvoiceResult - a model defined in Swagger"""  # noqa: E501

        self._invoice = None
        self.discriminator = None

        if invoice is not None:
            self.invoice = invoice

    @property
    def invoice(self):
        """Gets the invoice of this SubscribeResultInvoiceResult.  # noqa: E501

          # noqa: E501

        :return: The invoice of this SubscribeResultInvoiceResult.  # noqa: E501
        :rtype: list[SubscribeResultInvoiceResultInvoice]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this SubscribeResultInvoiceResult.

          # noqa: E501

        :param invoice: The invoice of this SubscribeResultInvoiceResult.  # noqa: E501
        :type: list[SubscribeResultInvoiceResultInvoice]
        """

        self._invoice = invoice

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
        if issubclass(SubscribeResultInvoiceResult, dict):
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
        if not isinstance(other, SubscribeResultInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
