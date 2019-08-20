# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.rate_plan_charge_object_custom_fields import RatePlanChargeObjectCustomFields  # noqa: F401,E501


class PUTSubscriptionPatchRequestTypeCharges(object):
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
        'charge_number': 'str',
        'custom_fields': 'RatePlanChargeObjectCustomFields'
    }

    attribute_map = {
        'charge_number': 'chargeNumber',
        'custom_fields': 'customFields'
    }

    def __init__(self, charge_number=None, custom_fields=None):  # noqa: E501
        """PUTSubscriptionPatchRequestTypeCharges - a model defined in Swagger"""  # noqa: E501

        self._charge_number = None
        self._custom_fields = None
        self.discriminator = None

        if charge_number is not None:
            self.charge_number = charge_number
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def charge_number(self):
        """Gets the charge_number of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501


        :return: The charge_number of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this PUTSubscriptionPatchRequestTypeCharges.


        :param charge_number: The charge_number of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def custom_fields(self):
        """Gets the custom_fields of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501


        :return: The custom_fields of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501
        :rtype: RatePlanChargeObjectCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this PUTSubscriptionPatchRequestTypeCharges.


        :param custom_fields: The custom_fields of this PUTSubscriptionPatchRequestTypeCharges.  # noqa: E501
        :type: RatePlanChargeObjectCustomFields
        """

        self._custom_fields = custom_fields

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
        if issubclass(PUTSubscriptionPatchRequestTypeCharges, dict):
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
        if not isinstance(other, PUTSubscriptionPatchRequestTypeCharges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other