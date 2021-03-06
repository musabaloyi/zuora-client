# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.charge_rated_result import ChargeRatedResult  # noqa: F401,E501


class SubscriptionRatedResult(object):
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
        'charge_rated_results': 'list[ChargeRatedResult]',
        'subscription_number': 'str'
    }

    attribute_map = {
        'charge_rated_results': 'chargeRatedResults',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, charge_rated_results=None, subscription_number=None):  # noqa: E501
        """SubscriptionRatedResult - a model defined in Swagger"""  # noqa: E501

        self._charge_rated_results = None
        self._subscription_number = None
        self.discriminator = None

        if charge_rated_results is not None:
            self.charge_rated_results = charge_rated_results
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def charge_rated_results(self):
        """Gets the charge_rated_results of this SubscriptionRatedResult.  # noqa: E501

        The amount changes per regular charge, or per regular charge and the discount charge if there is discount charge.  # noqa: E501

        :return: The charge_rated_results of this SubscriptionRatedResult.  # noqa: E501
        :rtype: list[ChargeRatedResult]
        """
        return self._charge_rated_results

    @charge_rated_results.setter
    def charge_rated_results(self, charge_rated_results):
        """Sets the charge_rated_results of this SubscriptionRatedResult.

        The amount changes per regular charge, or per regular charge and the discount charge if there is discount charge.  # noqa: E501

        :param charge_rated_results: The charge_rated_results of this SubscriptionRatedResult.  # noqa: E501
        :type: list[ChargeRatedResult]
        """

        self._charge_rated_results = charge_rated_results

    @property
    def subscription_number(self):
        """Gets the subscription_number of this SubscriptionRatedResult.  # noqa: E501


        :return: The subscription_number of this SubscriptionRatedResult.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this SubscriptionRatedResult.


        :param subscription_number: The subscription_number of this SubscriptionRatedResult.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(SubscriptionRatedResult, dict):
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
        if not isinstance(other, SubscriptionRatedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
