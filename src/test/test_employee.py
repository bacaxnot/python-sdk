"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.applicant_social_links import ApplicantSocialLinks
from apideck.model.compensation import Compensation
from apideck.model.custom_field import CustomField
from apideck.model.email import Email
from apideck.model.employee_bank_accounts import EmployeeBankAccounts
from apideck.model.employee_employment_role import EmployeeEmploymentRole
from apideck.model.employee_manager import EmployeeManager
from apideck.model.employee_team import EmployeeTeam
from apideck.model.employment_status import EmploymentStatus
from apideck.model.gender import Gender
from apideck.model.job import Job
from apideck.model.person import Person
from apideck.model.phone_number import PhoneNumber
from apideck.model.probation_period import ProbationPeriod
globals()['Address'] = Address
globals()['ApplicantSocialLinks'] = ApplicantSocialLinks
globals()['Compensation'] = Compensation
globals()['CustomField'] = CustomField
globals()['Email'] = Email
globals()['EmployeeBankAccounts'] = EmployeeBankAccounts
globals()['EmployeeEmploymentRole'] = EmployeeEmploymentRole
globals()['EmployeeManager'] = EmployeeManager
globals()['EmployeeTeam'] = EmployeeTeam
globals()['EmploymentStatus'] = EmploymentStatus
globals()['Gender'] = Gender
globals()['Job'] = Job
globals()['Person'] = Person
globals()['PhoneNumber'] = PhoneNumber
globals()['ProbationPeriod'] = ProbationPeriod
from apideck.model.employee import Employee


class TestEmployee(unittest.TestCase):
    """Employee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployee(self):
        """Test Employee"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Employee()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
