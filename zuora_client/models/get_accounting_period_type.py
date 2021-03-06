# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.accounting_period_object_custom_fields import AccountingPeriodObjectCustomFields  # noqa: F401,E501
from zuora_client.models.get_accounting_period_type_file_ids import GETAccountingPeriodTypeFileIds  # noqa: F401,E501


class GETAccountingPeriodType(object):
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
        'created_by': 'str',
        'created_on': 'datetime',
        'end_date': 'date',
        'file_ids': 'GETAccountingPeriodTypeFileIds',
        'fiscal_year': 'str',
        'fiscal_quarter': 'int',
        'id': 'str',
        'name': 'str',
        'notes': 'str',
        'run_trial_balance_end': 'datetime',
        'run_trial_balance_error_message': 'str',
        'run_trial_balance_start': 'datetime',
        'run_trial_balance_status': 'str',
        'start_date': 'date',
        'status': 'str',
        'success': 'bool',
        'updated_by': 'str',
        'updated_on': 'datetime'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'end_date': 'endDate',
        'file_ids': 'fileIds',
        'fiscal_year': 'fiscalYear',
        'fiscal_quarter': 'fiscal_quarter',
        'id': 'id',
        'name': 'name',
        'notes': 'notes',
        'run_trial_balance_end': 'runTrialBalanceEnd',
        'run_trial_balance_error_message': 'runTrialBalanceErrorMessage',
        'run_trial_balance_start': 'runTrialBalanceStart',
        'run_trial_balance_status': 'runTrialBalanceStatus',
        'start_date': 'startDate',
        'status': 'status',
        'success': 'success',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn'
    }

    def __init__(self, created_by=None, created_on=None, end_date=None, file_ids=None, fiscal_year=None, fiscal_quarter=None, id=None, name=None, notes=None, run_trial_balance_end=None, run_trial_balance_error_message=None, run_trial_balance_start=None, run_trial_balance_status=None, start_date=None, status=None, success=None, updated_by=None, updated_on=None):  # noqa: E501
        """GETAccountingPeriodType - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._created_on = None
        self._end_date = None
        self._file_ids = None
        self._fiscal_year = None
        self._fiscal_quarter = None
        self._id = None
        self._name = None
        self._notes = None
        self._run_trial_balance_end = None
        self._run_trial_balance_error_message = None
        self._run_trial_balance_start = None
        self._run_trial_balance_status = None
        self._start_date = None
        self._status = None
        self._success = None
        self._updated_by = None
        self._updated_on = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if end_date is not None:
            self.end_date = end_date
        if file_ids is not None:
            self.file_ids = file_ids
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if fiscal_quarter is not None:
            self.fiscal_quarter = fiscal_quarter
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if run_trial_balance_end is not None:
            self.run_trial_balance_end = run_trial_balance_end
        if run_trial_balance_error_message is not None:
            self.run_trial_balance_error_message = run_trial_balance_error_message
        if run_trial_balance_start is not None:
            self.run_trial_balance_start = run_trial_balance_start
        if run_trial_balance_status is not None:
            self.run_trial_balance_status = run_trial_balance_status
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def created_by(self):
        """Gets the created_by of this GETAccountingPeriodType.  # noqa: E501

        ID of the user who created the accounting period.   # noqa: E501

        :return: The created_by of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GETAccountingPeriodType.

        ID of the user who created the accounting period.   # noqa: E501

        :param created_by: The created_by of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this GETAccountingPeriodType.  # noqa: E501

        Date and time when the accounting period was created.   # noqa: E501

        :return: The created_on of this GETAccountingPeriodType.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GETAccountingPeriodType.

        Date and time when the accounting period was created.   # noqa: E501

        :param created_on: The created_on of this GETAccountingPeriodType.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def end_date(self):
        """Gets the end_date of this GETAccountingPeriodType.  # noqa: E501

        The end date of the accounting period.   # noqa: E501

        :return: The end_date of this GETAccountingPeriodType.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GETAccountingPeriodType.

        The end date of the accounting period.   # noqa: E501

        :param end_date: The end_date of this GETAccountingPeriodType.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def file_ids(self):
        """Gets the file_ids of this GETAccountingPeriodType.  # noqa: E501


        :return: The file_ids of this GETAccountingPeriodType.  # noqa: E501
        :rtype: GETAccountingPeriodTypeFileIds
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this GETAccountingPeriodType.


        :param file_ids: The file_ids of this GETAccountingPeriodType.  # noqa: E501
        :type: GETAccountingPeriodTypeFileIds
        """

        self._file_ids = file_ids

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this GETAccountingPeriodType.  # noqa: E501

        Fiscal year of the accounting period.   # noqa: E501

        :return: The fiscal_year of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this GETAccountingPeriodType.

        Fiscal year of the accounting period.   # noqa: E501

        :param fiscal_year: The fiscal_year of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._fiscal_year = fiscal_year

    @property
    def fiscal_quarter(self):
        """Gets the fiscal_quarter of this GETAccountingPeriodType.  # noqa: E501

          # noqa: E501

        :return: The fiscal_quarter of this GETAccountingPeriodType.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_quarter

    @fiscal_quarter.setter
    def fiscal_quarter(self, fiscal_quarter):
        """Sets the fiscal_quarter of this GETAccountingPeriodType.

          # noqa: E501

        :param fiscal_quarter: The fiscal_quarter of this GETAccountingPeriodType.  # noqa: E501
        :type: int
        """

        self._fiscal_quarter = fiscal_quarter

    @property
    def id(self):
        """Gets the id of this GETAccountingPeriodType.  # noqa: E501

        ID of the accounting period.   # noqa: E501

        :return: The id of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETAccountingPeriodType.

        ID of the accounting period.   # noqa: E501

        :param id: The id of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GETAccountingPeriodType.  # noqa: E501

        Name of the accounting period.   # noqa: E501

        :return: The name of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GETAccountingPeriodType.

        Name of the accounting period.   # noqa: E501

        :param name: The name of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this GETAccountingPeriodType.  # noqa: E501

        Any optional notes about the accounting period.   # noqa: E501

        :return: The notes of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GETAccountingPeriodType.

        Any optional notes about the accounting period.   # noqa: E501

        :param notes: The notes of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def run_trial_balance_end(self):
        """Gets the run_trial_balance_end of this GETAccountingPeriodType.  # noqa: E501

        Date and time that the trial balance was completed. If the trial balance status is `Pending`, `Processing`, or `Error`, this field is `null`.   # noqa: E501

        :return: The run_trial_balance_end of this GETAccountingPeriodType.  # noqa: E501
        :rtype: datetime
        """
        return self._run_trial_balance_end

    @run_trial_balance_end.setter
    def run_trial_balance_end(self, run_trial_balance_end):
        """Sets the run_trial_balance_end of this GETAccountingPeriodType.

        Date and time that the trial balance was completed. If the trial balance status is `Pending`, `Processing`, or `Error`, this field is `null`.   # noqa: E501

        :param run_trial_balance_end: The run_trial_balance_end of this GETAccountingPeriodType.  # noqa: E501
        :type: datetime
        """

        self._run_trial_balance_end = run_trial_balance_end

    @property
    def run_trial_balance_error_message(self):
        """Gets the run_trial_balance_error_message of this GETAccountingPeriodType.  # noqa: E501

        If trial balance status is Error, an error message is returned in this field.   # noqa: E501

        :return: The run_trial_balance_error_message of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._run_trial_balance_error_message

    @run_trial_balance_error_message.setter
    def run_trial_balance_error_message(self, run_trial_balance_error_message):
        """Sets the run_trial_balance_error_message of this GETAccountingPeriodType.

        If trial balance status is Error, an error message is returned in this field.   # noqa: E501

        :param run_trial_balance_error_message: The run_trial_balance_error_message of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._run_trial_balance_error_message = run_trial_balance_error_message

    @property
    def run_trial_balance_start(self):
        """Gets the run_trial_balance_start of this GETAccountingPeriodType.  # noqa: E501

        Date and time that the trial balance was run. If the trial balance status is Pending, this field is null.   # noqa: E501

        :return: The run_trial_balance_start of this GETAccountingPeriodType.  # noqa: E501
        :rtype: datetime
        """
        return self._run_trial_balance_start

    @run_trial_balance_start.setter
    def run_trial_balance_start(self, run_trial_balance_start):
        """Sets the run_trial_balance_start of this GETAccountingPeriodType.

        Date and time that the trial balance was run. If the trial balance status is Pending, this field is null.   # noqa: E501

        :param run_trial_balance_start: The run_trial_balance_start of this GETAccountingPeriodType.  # noqa: E501
        :type: datetime
        """

        self._run_trial_balance_start = run_trial_balance_start

    @property
    def run_trial_balance_status(self):
        """Gets the run_trial_balance_status of this GETAccountingPeriodType.  # noqa: E501

        Status of the trial balance for the accounting period. Possible values:  * `Pending` * `Processing` * `Completed` * `Error`   # noqa: E501

        :return: The run_trial_balance_status of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._run_trial_balance_status

    @run_trial_balance_status.setter
    def run_trial_balance_status(self, run_trial_balance_status):
        """Sets the run_trial_balance_status of this GETAccountingPeriodType.

        Status of the trial balance for the accounting period. Possible values:  * `Pending` * `Processing` * `Completed` * `Error`   # noqa: E501

        :param run_trial_balance_status: The run_trial_balance_status of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._run_trial_balance_status = run_trial_balance_status

    @property
    def start_date(self):
        """Gets the start_date of this GETAccountingPeriodType.  # noqa: E501

        The start date of the accounting period.   # noqa: E501

        :return: The start_date of this GETAccountingPeriodType.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GETAccountingPeriodType.

        The start date of the accounting period.   # noqa: E501

        :param start_date: The start_date of this GETAccountingPeriodType.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this GETAccountingPeriodType.  # noqa: E501

        Status of the accounting period. Possible values: * `Open` * `PendingClose` * `Closed`   # noqa: E501

        :return: The status of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETAccountingPeriodType.

        Status of the accounting period. Possible values: * `Open` * `PendingClose` * `Closed`   # noqa: E501

        :param status: The status of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def success(self):
        """Gets the success of this GETAccountingPeriodType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETAccountingPeriodType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETAccountingPeriodType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETAccountingPeriodType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def updated_by(self):
        """Gets the updated_by of this GETAccountingPeriodType.  # noqa: E501

        ID of the user who last updated the accounting period.   # noqa: E501

        :return: The updated_by of this GETAccountingPeriodType.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this GETAccountingPeriodType.

        ID of the user who last updated the accounting period.   # noqa: E501

        :param updated_by: The updated_by of this GETAccountingPeriodType.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this GETAccountingPeriodType.  # noqa: E501

        Date and time when the accounting period was last updated.   # noqa: E501

        :return: The updated_on of this GETAccountingPeriodType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this GETAccountingPeriodType.

        Date and time when the accounting period was last updated.   # noqa: E501

        :param updated_on: The updated_on of this GETAccountingPeriodType.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

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
        if issubclass(GETAccountingPeriodType, dict):
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
        if not isinstance(other, GETAccountingPeriodType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
