# coding: utf-8




import pprint
import re  # noqa: F401

import six


class CreatePaymentMethodPayPalAdaptive(object):
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
        'preapproval_key': 'str'
    }

    attribute_map = {
        'preapproval_key': 'preapprovalKey'
    }

    def __init__(self, preapproval_key=None):  # noqa: E501
        """CreatePaymentMethodPayPalAdaptive - a model defined in Swagger"""  # noqa: E501

        self._preapproval_key = None
        self.discriminator = None

        if preapproval_key is not None:
            self.preapproval_key = preapproval_key

    @property
    def preapproval_key(self):
        """Gets the preapproval_key of this CreatePaymentMethodPayPalAdaptive.  # noqa: E501

        The PayPal preapproval key.   # noqa: E501

        :return: The preapproval_key of this CreatePaymentMethodPayPalAdaptive.  # noqa: E501
        :rtype: str
        """
        return self._preapproval_key

    @preapproval_key.setter
    def preapproval_key(self, preapproval_key):
        """Sets the preapproval_key of this CreatePaymentMethodPayPalAdaptive.

        The PayPal preapproval key.   # noqa: E501

        :param preapproval_key: The preapproval_key of this CreatePaymentMethodPayPalAdaptive.  # noqa: E501
        :type: str
        """

        self._preapproval_key = preapproval_key

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
        if issubclass(CreatePaymentMethodPayPalAdaptive, dict):
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
        if not isinstance(other, CreatePaymentMethodPayPalAdaptive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
