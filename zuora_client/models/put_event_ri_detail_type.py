# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.event_revenue_item_type import EventRevenueItemType  # noqa: F401,E501


class PUTEventRIDetailType(object):
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
        'revenue_items': 'list[EventRevenueItemType]'
    }

    attribute_map = {
        'revenue_items': 'revenueItems'
    }

    def __init__(self, revenue_items=None):  # noqa: E501
        """PUTEventRIDetailType - a model defined in Swagger"""  # noqa: E501

        self._revenue_items = None
        self.discriminator = None

        self.revenue_items = revenue_items

    @property
    def revenue_items(self):
        """Gets the revenue_items of this PUTEventRIDetailType.  # noqa: E501

        Revenue items are listed in ascending order by the accounting period start date.  Include at least one custom field.   # noqa: E501

        :return: The revenue_items of this PUTEventRIDetailType.  # noqa: E501
        :rtype: list[EventRevenueItemType]
        """
        return self._revenue_items

    @revenue_items.setter
    def revenue_items(self, revenue_items):
        """Sets the revenue_items of this PUTEventRIDetailType.

        Revenue items are listed in ascending order by the accounting period start date.  Include at least one custom field.   # noqa: E501

        :param revenue_items: The revenue_items of this PUTEventRIDetailType.  # noqa: E501
        :type: list[EventRevenueItemType]
        """
        if revenue_items is None:
            raise ValueError("Invalid value for `revenue_items`, must not be `None`")  # noqa: E501

        self._revenue_items = revenue_items

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
        if issubclass(PUTEventRIDetailType, dict):
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
        if not isinstance(other, PUTEventRIDetailType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
