# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GetOrderBillingInfoResponseTypeBillingInfo(object):
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
        'billed_amount': 'float',
        'currency': 'str',
        'tcb': 'float',
        'unbilled_amount': 'float'
    }

    attribute_map = {
        'billed_amount': 'billedAmount',
        'currency': 'currency',
        'tcb': 'tcb',
        'unbilled_amount': 'unbilledAmount'
    }

    def __init__(self, billed_amount=None, currency=None, tcb=None, unbilled_amount=None):  # noqa: E501
        """GetOrderBillingInfoResponseTypeBillingInfo - a model defined in Swagger"""  # noqa: E501

        self._billed_amount = None
        self._currency = None
        self._tcb = None
        self._unbilled_amount = None
        self.discriminator = None

        if billed_amount is not None:
            self.billed_amount = billed_amount
        if currency is not None:
            self.currency = currency
        if tcb is not None:
            self.tcb = tcb
        if unbilled_amount is not None:
            self.unbilled_amount = unbilled_amount

    @property
    def billed_amount(self):
        """Gets the billed_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501


        :return: The billed_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :rtype: float
        """
        return self._billed_amount

    @billed_amount.setter
    def billed_amount(self, billed_amount):
        """Sets the billed_amount of this GetOrderBillingInfoResponseTypeBillingInfo.


        :param billed_amount: The billed_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :type: float
        """

        self._billed_amount = billed_amount

    @property
    def currency(self):
        """Gets the currency of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501

        Currency code.  # noqa: E501

        :return: The currency of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetOrderBillingInfoResponseTypeBillingInfo.

        Currency code.  # noqa: E501

        :param currency: The currency of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def tcb(self):
        """Gets the tcb of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501

        Total contracted billing of this order.  # noqa: E501

        :return: The tcb of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :rtype: float
        """
        return self._tcb

    @tcb.setter
    def tcb(self, tcb):
        """Sets the tcb of this GetOrderBillingInfoResponseTypeBillingInfo.

        Total contracted billing of this order.  # noqa: E501

        :param tcb: The tcb of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :type: float
        """

        self._tcb = tcb

    @property
    def unbilled_amount(self):
        """Gets the unbilled_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501


        :return: The unbilled_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :rtype: float
        """
        return self._unbilled_amount

    @unbilled_amount.setter
    def unbilled_amount(self, unbilled_amount):
        """Sets the unbilled_amount of this GetOrderBillingInfoResponseTypeBillingInfo.


        :param unbilled_amount: The unbilled_amount of this GetOrderBillingInfoResponseTypeBillingInfo.  # noqa: E501
        :type: float
        """

        self._unbilled_amount = unbilled_amount

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
        if issubclass(GetOrderBillingInfoResponseTypeBillingInfo, dict):
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
        if not isinstance(other, GetOrderBillingInfoResponseTypeBillingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
