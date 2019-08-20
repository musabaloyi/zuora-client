# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_invoice_tax_item_type import GETInvoiceTaxItemType  # noqa: F401,E501


class InvoiceItemTaxationItems(object):
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
        'data': 'list[GETInvoiceTaxItemType]',
        'next_page': 'str'
    }

    attribute_map = {
        'data': 'data',
        'next_page': 'nextPage'
    }

    def __init__(self, data=None, next_page=None):  # noqa: E501
        """InvoiceItemTaxationItems - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._next_page = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if next_page is not None:
            self.next_page = next_page

    @property
    def data(self):
        """Gets the data of this InvoiceItemTaxationItems.  # noqa: E501

        List of taxation items.   # noqa: E501

        :return: The data of this InvoiceItemTaxationItems.  # noqa: E501
        :rtype: list[GETInvoiceTaxItemType]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InvoiceItemTaxationItems.

        List of taxation items.   # noqa: E501

        :param data: The data of this InvoiceItemTaxationItems.  # noqa: E501
        :type: list[GETInvoiceTaxItemType]
        """

        self._data = data

    @property
    def next_page(self):
        """Gets the next_page of this InvoiceItemTaxationItems.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this InvoiceItemTaxationItems.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this InvoiceItemTaxationItems.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this InvoiceItemTaxationItems.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

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
        if issubclass(InvoiceItemTaxationItems, dict):
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
        if not isinstance(other, InvoiceItemTaxationItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other