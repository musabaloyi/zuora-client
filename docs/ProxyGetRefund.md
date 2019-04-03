# ProxyGetRefund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the refund&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the refund was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**syncto_net_suite__ns** | **str** | Specifies whether the refund should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** |  The ID of the account associated with this refund. Specify a value for this field only if you&#39;re creating an electronic non-referenced refund. Don&#39;t specify a value for any other type of refund; Zuora associates the refund automatically with the account from the associated payment. **Character limit**: 32 **Values**: a valid account ID  | [optional] 
**accounting_code** | **str** |  The accounting code for the payment or invoice line item that the refund applies to. If there is no accounting code, then this value is null. Accounting codes group transactions that contain similar accounting attributes. **Character limit**: 50 **Values**: automatically generated  | [optional] 
**amount** | **float** |  The amount of the refund. The amount can&#39;t exceed the amount of the associated payment. If the original payment was applied to a single invoice, then you can create a partial refund. However, if the payment was applies to multiple invoices, then you can only make a partial refund through the web-based UI, not through the API. **Character limit**: 16 **Values**: a valid currency amount  | [optional] 
**cancelled_on** | **datetime** |  The date the refund was cancelled. **Values**: automatically generated  | [optional] 
**comment** | **str** |  Use this field to record comments about the refund. **Character limit**: 255 **Values**: a string of 255 characters or fewer  | [optional] 
**created_by_id** | **str** |  The ID of the Zuora user who created the &#x60;Refund&#x60; object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the &#x60;Refund&#x60; object was created. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**gateway** | **str** |  The gateway that processed the original payment. Zuora uses this same gateway for the corresponding refund. If this payment gateway is no longer active, then the electronic refund fails. A gateway is an online service provider that connects an online shopping cart to a payment processor. **Values**: automatically inherited from the &#x60;Payment&#x60; object  | [optional] 
**gateway_response** | **str** |  The message returned from the payment gateway for the refund. This message is gateway-dependent. **Character limit**: 500 **Values**: automatically generated  | [optional] 
**gateway_response_code** | **str** |  The code returned from the payment gateway for the payment. This code is gateway-dependent. **Character limit**: 20 **System****Values**: automatically generated  | [optional] 
**gateway_state** | **str** |  The status of the payment in the gateway. **Character limit**: 19 **Values**: automatically generated  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**marked_for_submission_on** | **datetime** |  The date when a payment was marked and waiting for batch submission to the payment process. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**method_type** | **str** |  Indicates how an external refund was issued to a customer. This field is required for an external refund. You can issue an external refund on an electronic payment. **Character limit**: 30 **Values**:  - &#x60;ACH&#x60; - &#x60;Cash&#x60; - &#x60;Check&#x60; - &#x60;CreditCard&#x60; - &#x60;Other&#x60; - &#x60;PayPal&#x60; - &#x60;WireTransfer&#x60; - &#x60;DebitCard&#x60; - &#x60;CreditCardReferenceTransaction&#x60;  | [optional] 
**payment_method_id** | **str** |  The unique ID of the payment method that the customer used to make the payment. Specify a value for this field only if you&#39;re creating an electronic non-referenced refund. **Character limit**: 32 **V****alues**: a valid payment method ID  | [optional] 
**payment_method_snapshot_id** | **str** |  The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction. **Character limit**: 32 **V****alues**: a valid payment method snapshot ID  | [optional] 
**reason_code** | **str** |  A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **V****alues**: a valid reason code  | [optional] 
**reference_id** | **str** |  The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments. **Character limit**: 60 **Values**: a string of 60 characters or fewer  | [optional] 
**refund_date** | **date** |  The date of the refund, in &#x60;yyyy-mm-dd&#x60; format. The date of the refund cannot be before the payment date. Specify this field only for external refunds. Zuora automatically generates this field for electronic refunds. **Character limit**: 29  | [optional] 
**refund_number** | **str** |  The unique identifier of the refund. **Character limit**: 50 **Values**: automatically generated  | [optional] 
**refund_transaction_time** | **datetime** |  The date and time when the refund was issued. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**second_refund_reference_id** | **str** |  The transaction ID returned by the payment gateway if there is an additional transaction for the payment. Use this field to reconcile payments between your gateway and Zuora Payments. **Character limit**: 60 **Values**: a string of 60 characters or fewer  | [optional] 
**settled_on** | **datetime** |  The date when the payment was settled in the payment processor. This field is used by the Spectrum gateway only and not applicable to other gateways. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**soft_descriptor** | **str** |  A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 35 **Values**:  - 3-byte company identifier &amp;quot;*&amp;quot; 18-byte descriptor - 7-byte company identifier &amp;quot;*&amp;quot; 14-byte descriptor - 12-byte company identifier &amp;quot;*&amp;quot; 9-byte descriptor  | [optional] 
**soft_descriptor_phone** | **str** |  A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 20 **Values**:  - Customer service phone number formatted as: &#x60;NNN-NNN-NNNN&#x60; or &#x60;NNN-AAAAAAA&#x60; - URL (non-e-Commerce): Transactions sent with a URL do not qualify for the best interchange rate - Email address  | [optional] 
**source_type** | **str** |  Specifies whether the refund is a refund payment or a credit balance. This field is required when creating an non-referenced refund. If you creating an non-referenced refund, then set this value to &#x60;CreditBalance&#x60;. **Character limit**: 13 **Values**:  - &#x60;Payment&#x60; - &#x60;CreditBalance&#x60;  | [optional] 
**status** | **str** |  The status of the refund. **Character limit**: 10 **Values**: automatically generated:  - &#x60;Canceled&#x60; - &#x60;Error&#x60; - &#x60;Processed&#x60; - &#x60;Processing&#x60;  | [optional] 
**submitted_on** | **datetime** |  The date when the payment was submitted. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**transferred_to_accounting** | **str** |  Specifies whether or not the object has been transferred to an external accounting system. Use this field for integrations with accounting systems such as NetSuite. **Character limit**: 10 **Values**: automatically generated:  - &#x60;Processing&#x60; - &#x60;Yes&#x60; - &#x60;Error&#x60; - &#x60;Ignore&#x60;  | [optional] 
**type** | **str** |  Specifies if the refund is electronic or external. **Character limit**: 10 **Values**:  - &#x60;Electronic&#x60; - External  | [optional] 
**updated_by_id** | **str** |  The ID of the last user to update the object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the object was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

