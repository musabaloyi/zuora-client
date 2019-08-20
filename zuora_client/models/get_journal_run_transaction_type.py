# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETJournalRunTransactionType(object):
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
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):  # noqa: E501
        """GETJournalRunTransactionType - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self.discriminator = None

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this GETJournalRunTransactionType.  # noqa: E501

        Transaction type. Invoice Adjustment is deprecated on Production. Zuora recommends that you use the Invoice Item Adjustment instead.  If you enable the Invoice Settlement feature, Debit Memo Item, Credit Memo Item, and Credit Memo Application Item are available, Payment and Refund will be replaced by Payment Application and Refund Application.   If you enable both the Invoice Settlement feature and the Invoice Item Settlement feature, Payment and Refund will be replaced by Payment Application Item and Refund Application Item.    # noqa: E501

        :return: The type of this GETJournalRunTransactionType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GETJournalRunTransactionType.

        Transaction type. Invoice Adjustment is deprecated on Production. Zuora recommends that you use the Invoice Item Adjustment instead.  If you enable the Invoice Settlement feature, Debit Memo Item, Credit Memo Item, and Credit Memo Application Item are available, Payment and Refund will be replaced by Payment Application and Refund Application.   If you enable both the Invoice Settlement feature and the Invoice Item Settlement feature, Payment and Refund will be replaced by Payment Application Item and Refund Application Item.    # noqa: E501

        :param type: The type of this GETJournalRunTransactionType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Invoice Item", "Taxation Item", "Invoice Item Adjustment (Invoice)", "Invoice Item Adjustment (tax)", "Invoice Adjustment", "Electronic Payment", "External Payment", "Electronic Refund", "External Refund", "Electronic Credit Balance Payment", "External Credit Balance Payment", "Electronic Credit Balance Refund", "External Credit Balance Refund", "Credit Balance Adjustment (Applied from Credit Balance)", "Credit Balance Adjustment (Transferred to Credit Balance)", "Revenue Event Item", "Debit Memo Item (Charge)", "Debit Memo Item (tax)", "Credit Memo Item (Charge)", "Credit Memo Item (tax)", "Credit Memo Application Item", "Electronic Payment Application", "External Payment Application", "Electronic Refund Application", "External Refund Application", "Electronic Payment Application Item", "External Payment Application Item", "Electronic Refund Application Item", "External Refund Application Item"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(GETJournalRunTransactionType, dict):
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
        if not isinstance(other, GETJournalRunTransactionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other