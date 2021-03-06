# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.create_order_charge_update import CreateOrderChargeUpdate  # noqa: F401,E501
from zuora_client.models.rate_plan_object_custom_fields import RatePlanObjectCustomFields  # noqa: F401,E501


class CreateOrderRatePlanUpdate(object):
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
        'charge_updates': 'list[CreateOrderChargeUpdate]',
        'custom_fields': 'RatePlanObjectCustomFields',
        'rate_plan_id': 'str',
        'specific_update_date': 'date',
        'unique_token': 'str'
    }

    attribute_map = {
        'charge_updates': 'chargeUpdates',
        'custom_fields': 'customFields',
        'rate_plan_id': 'ratePlanId',
        'specific_update_date': 'specificUpdateDate',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, charge_updates=None, custom_fields=None, rate_plan_id=None, specific_update_date=None, unique_token=None):  # noqa: E501
        """CreateOrderRatePlanUpdate - a model defined in Swagger"""  # noqa: E501

        self._charge_updates = None
        self._custom_fields = None
        self._rate_plan_id = None
        self._specific_update_date = None
        self._unique_token = None
        self.discriminator = None

        if charge_updates is not None:
            self.charge_updates = charge_updates
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if rate_plan_id is not None:
            self.rate_plan_id = rate_plan_id
        if specific_update_date is not None:
            self.specific_update_date = specific_update_date
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def charge_updates(self):
        """Gets the charge_updates of this CreateOrderRatePlanUpdate.  # noqa: E501


        :return: The charge_updates of this CreateOrderRatePlanUpdate.  # noqa: E501
        :rtype: list[CreateOrderChargeUpdate]
        """
        return self._charge_updates

    @charge_updates.setter
    def charge_updates(self, charge_updates):
        """Sets the charge_updates of this CreateOrderRatePlanUpdate.


        :param charge_updates: The charge_updates of this CreateOrderRatePlanUpdate.  # noqa: E501
        :type: list[CreateOrderChargeUpdate]
        """

        self._charge_updates = charge_updates

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateOrderRatePlanUpdate.  # noqa: E501


        :return: The custom_fields of this CreateOrderRatePlanUpdate.  # noqa: E501
        :rtype: RatePlanObjectCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateOrderRatePlanUpdate.


        :param custom_fields: The custom_fields of this CreateOrderRatePlanUpdate.  # noqa: E501
        :type: RatePlanObjectCustomFields
        """

        self._custom_fields = custom_fields

    @property
    def rate_plan_id(self):
        """Gets the rate_plan_id of this CreateOrderRatePlanUpdate.  # noqa: E501

        The id of the rate plan to be updated. It can be the latest version or any history version id.   # noqa: E501

        :return: The rate_plan_id of this CreateOrderRatePlanUpdate.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, rate_plan_id):
        """Sets the rate_plan_id of this CreateOrderRatePlanUpdate.

        The id of the rate plan to be updated. It can be the latest version or any history version id.   # noqa: E501

        :param rate_plan_id: The rate_plan_id of this CreateOrderRatePlanUpdate.  # noqa: E501
        :type: str
        """

        self._rate_plan_id = rate_plan_id

    @property
    def specific_update_date(self):
        """Gets the specific_update_date of this CreateOrderRatePlanUpdate.  # noqa: E501

        Used for the 'update before update' and 'update before remove' cases.  # noqa: E501

        :return: The specific_update_date of this CreateOrderRatePlanUpdate.  # noqa: E501
        :rtype: date
        """
        return self._specific_update_date

    @specific_update_date.setter
    def specific_update_date(self, specific_update_date):
        """Sets the specific_update_date of this CreateOrderRatePlanUpdate.

        Used for the 'update before update' and 'update before remove' cases.  # noqa: E501

        :param specific_update_date: The specific_update_date of this CreateOrderRatePlanUpdate.  # noqa: E501
        :type: date
        """

        self._specific_update_date = specific_update_date

    @property
    def unique_token(self):
        """Gets the unique_token of this CreateOrderRatePlanUpdate.  # noqa: E501

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.   # noqa: E501

        :return: The unique_token of this CreateOrderRatePlanUpdate.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this CreateOrderRatePlanUpdate.

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.   # noqa: E501

        :param unique_token: The unique_token of this CreateOrderRatePlanUpdate.  # noqa: E501
        :type: str
        """

        self._unique_token = unique_token

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
        if issubclass(CreateOrderRatePlanUpdate, dict):
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
        if not isinstance(other, CreateOrderRatePlanUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
