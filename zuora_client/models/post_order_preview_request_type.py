# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.order_object_custom_fields import OrderObjectCustomFields  # noqa: F401,E501
from zuora_client.models.post_order_preview_request_type_subscriptions import POSTOrderPreviewRequestTypeSubscriptions  # noqa: F401,E501
from zuora_client.models.preview_account_info import PreviewAccountInfo  # noqa: F401,E501
from zuora_client.models.preview_options import PreviewOptions  # noqa: F401,E501


class POSTOrderPreviewRequestType(object):
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
        'custom_fields': 'OrderObjectCustomFields',
        'existing_account_number': 'str',
        'order_date': 'date',
        'order_number': 'str',
        'preview_account_info': 'PreviewAccountInfo',
        'preview_options': 'PreviewOptions',
        'subscriptions': 'list[POSTOrderPreviewRequestTypeSubscriptions]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'existing_account_number': 'existingAccountNumber',
        'order_date': 'orderDate',
        'order_number': 'orderNumber',
        'preview_account_info': 'previewAccountInfo',
        'preview_options': 'previewOptions',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, custom_fields=None, existing_account_number=None, order_date=None, order_number=None, preview_account_info=None, preview_options=None, subscriptions=None):  # noqa: E501
        """POSTOrderPreviewRequestType - a model defined in Swagger"""  # noqa: E501

        self._custom_fields = None
        self._existing_account_number = None
        self._order_date = None
        self._order_number = None
        self._preview_account_info = None
        self._preview_options = None
        self._subscriptions = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if existing_account_number is not None:
            self.existing_account_number = existing_account_number
        self.order_date = order_date
        if order_number is not None:
            self.order_number = order_number
        if preview_account_info is not None:
            self.preview_account_info = preview_account_info
        self.preview_options = preview_options
        self.subscriptions = subscriptions

    @property
    def custom_fields(self):
        """Gets the custom_fields of this POSTOrderPreviewRequestType.  # noqa: E501


        :return: The custom_fields of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: OrderObjectCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this POSTOrderPreviewRequestType.


        :param custom_fields: The custom_fields of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: OrderObjectCustomFields
        """

        self._custom_fields = custom_fields

    @property
    def existing_account_number(self):
        """Gets the existing_account_number of this POSTOrderPreviewRequestType.  # noqa: E501

        The account number that this order will be created under. It can be either the accountNumber or the account info. It will return an error if both are specified. Note that invoice owner account of the subscriptions included in this order should be the same with the account of the order.   # noqa: E501

        :return: The existing_account_number of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: str
        """
        return self._existing_account_number

    @existing_account_number.setter
    def existing_account_number(self, existing_account_number):
        """Sets the existing_account_number of this POSTOrderPreviewRequestType.

        The account number that this order will be created under. It can be either the accountNumber or the account info. It will return an error if both are specified. Note that invoice owner account of the subscriptions included in this order should be the same with the account of the order.   # noqa: E501

        :param existing_account_number: The existing_account_number of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: str
        """
        if existing_account_number is not None and len(existing_account_number) > 70:
            raise ValueError("Invalid value for `existing_account_number`, length must be less than or equal to `70`")  # noqa: E501

        self._existing_account_number = existing_account_number

    @property
    def order_date(self):
        """Gets the order_date of this POSTOrderPreviewRequestType.  # noqa: E501

        The date when the order is signed. All of the order actions under this order will use this order date as the contract effective date.  # noqa: E501

        :return: The order_date of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: date
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this POSTOrderPreviewRequestType.

        The date when the order is signed. All of the order actions under this order will use this order date as the contract effective date.  # noqa: E501

        :param order_date: The order_date of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: date
        """
        if order_date is None:
            raise ValueError("Invalid value for `order_date`, must not be `None`")  # noqa: E501

        self._order_date = order_date

    @property
    def order_number(self):
        """Gets the order_number of this POSTOrderPreviewRequestType.  # noqa: E501

        The order number of this order.  # noqa: E501

        :return: The order_number of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this POSTOrderPreviewRequestType.

        The order number of this order.  # noqa: E501

        :param order_number: The order_number of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: str
        """
        if order_number is not None and len(order_number) > 100:
            raise ValueError("Invalid value for `order_number`, length must be less than or equal to `100`")  # noqa: E501

        self._order_number = order_number

    @property
    def preview_account_info(self):
        """Gets the preview_account_info of this POSTOrderPreviewRequestType.  # noqa: E501


        :return: The preview_account_info of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: PreviewAccountInfo
        """
        return self._preview_account_info

    @preview_account_info.setter
    def preview_account_info(self, preview_account_info):
        """Sets the preview_account_info of this POSTOrderPreviewRequestType.


        :param preview_account_info: The preview_account_info of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: PreviewAccountInfo
        """

        self._preview_account_info = preview_account_info

    @property
    def preview_options(self):
        """Gets the preview_options of this POSTOrderPreviewRequestType.  # noqa: E501


        :return: The preview_options of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: PreviewOptions
        """
        return self._preview_options

    @preview_options.setter
    def preview_options(self, preview_options):
        """Sets the preview_options of this POSTOrderPreviewRequestType.


        :param preview_options: The preview_options of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: PreviewOptions
        """
        if preview_options is None:
            raise ValueError("Invalid value for `preview_options`, must not be `None`")  # noqa: E501

        self._preview_options = preview_options

    @property
    def subscriptions(self):
        """Gets the subscriptions of this POSTOrderPreviewRequestType.  # noqa: E501

        Each item includes a set of order actions, which will be applied to the same base subscription.  # noqa: E501

        :return: The subscriptions of this POSTOrderPreviewRequestType.  # noqa: E501
        :rtype: list[POSTOrderPreviewRequestTypeSubscriptions]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this POSTOrderPreviewRequestType.

        Each item includes a set of order actions, which will be applied to the same base subscription.  # noqa: E501

        :param subscriptions: The subscriptions of this POSTOrderPreviewRequestType.  # noqa: E501
        :type: list[POSTOrderPreviewRequestTypeSubscriptions]
        """
        if subscriptions is None:
            raise ValueError("Invalid value for `subscriptions`, must not be `None`")  # noqa: E501

        self._subscriptions = subscriptions

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
        if issubclass(POSTOrderPreviewRequestType, dict):
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
        if not isinstance(other, POSTOrderPreviewRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other