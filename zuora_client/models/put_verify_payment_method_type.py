# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.put_verify_payment_method_type_gateway_options import PUTVerifyPaymentMethodTypeGatewayOptions  # noqa: F401,E501


class PUTVerifyPaymentMethodType(object):
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
        'gateway_options': 'PUTVerifyPaymentMethodTypeGatewayOptions',
        'payment_gateway_name': 'str',
        'security_code': 'str'
    }

    attribute_map = {
        'gateway_options': 'gatewayOptions',
        'payment_gateway_name': 'paymentGatewayName',
        'security_code': 'securityCode'
    }

    def __init__(self, gateway_options=None, payment_gateway_name=None, security_code=None):  # noqa: E501
        """PUTVerifyPaymentMethodType - a model defined in Swagger"""  # noqa: E501

        self._gateway_options = None
        self._payment_gateway_name = None
        self._security_code = None
        self.discriminator = None

        if gateway_options is not None:
            self.gateway_options = gateway_options
        if payment_gateway_name is not None:
            self.payment_gateway_name = payment_gateway_name
        if security_code is not None:
            self.security_code = security_code

    @property
    def gateway_options(self):
        """Gets the gateway_options of this PUTVerifyPaymentMethodType.  # noqa: E501


        :return: The gateway_options of this PUTVerifyPaymentMethodType.  # noqa: E501
        :rtype: PUTVerifyPaymentMethodTypeGatewayOptions
        """
        return self._gateway_options

    @gateway_options.setter
    def gateway_options(self, gateway_options):
        """Sets the gateway_options of this PUTVerifyPaymentMethodType.


        :param gateway_options: The gateway_options of this PUTVerifyPaymentMethodType.  # noqa: E501
        :type: PUTVerifyPaymentMethodTypeGatewayOptions
        """

        self._gateway_options = gateway_options

    @property
    def payment_gateway_name(self):
        """Gets the payment_gateway_name of this PUTVerifyPaymentMethodType.  # noqa: E501

        The name of the payment gateway instance. If no value is specified for this field, the default payment gateway of the customer account will be used.   # noqa: E501

        :return: The payment_gateway_name of this PUTVerifyPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway_name

    @payment_gateway_name.setter
    def payment_gateway_name(self, payment_gateway_name):
        """Sets the payment_gateway_name of this PUTVerifyPaymentMethodType.

        The name of the payment gateway instance. If no value is specified for this field, the default payment gateway of the customer account will be used.   # noqa: E501

        :param payment_gateway_name: The payment_gateway_name of this PUTVerifyPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._payment_gateway_name = payment_gateway_name

    @property
    def security_code(self):
        """Gets the security_code of this PUTVerifyPaymentMethodType.  # noqa: E501

        The CVV or CVV2 security code for the credit card or debit card. To ensure PCI compliance, the value of this field is not stored and cannot be queried.   # noqa: E501

        :return: The security_code of this PUTVerifyPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PUTVerifyPaymentMethodType.

        The CVV or CVV2 security code for the credit card or debit card. To ensure PCI compliance, the value of this field is not stored and cannot be queried.   # noqa: E501

        :param security_code: The security_code of this PUTVerifyPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

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
        if issubclass(PUTVerifyPaymentMethodType, dict):
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
        if not isinstance(other, PUTVerifyPaymentMethodType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
