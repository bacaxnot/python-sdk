"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.country import Country
from apideck.model.custom_field import CustomField
from apideck.model.email import Email
from apideck.model.employee_compensation import EmployeeCompensation
from apideck.model.employee_employment_role import EmployeeEmploymentRole
from apideck.model.employee_job import EmployeeJob
from apideck.model.employee_manager import EmployeeManager
from apideck.model.employment_status import EmploymentStatus
from apideck.model.gender import Gender
from apideck.model.person import Person
from apideck.model.phone_number import PhoneNumber
from apideck.model.probation_period import ProbationPeriod
from apideck.model.social_link import SocialLink
from apideck.model.tags import Tags
from apideck.model.team import Team
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Country'] = Country
globals()['CustomField'] = CustomField
globals()['Email'] = Email
globals()['EmployeeCompensation'] = EmployeeCompensation
globals()['EmployeeEmploymentRole'] = EmployeeEmploymentRole
globals()['EmployeeJob'] = EmployeeJob
globals()['EmployeeManager'] = EmployeeManager
globals()['EmploymentStatus'] = EmploymentStatus
globals()['Gender'] = Gender
globals()['Person'] = Person
globals()['PhoneNumber'] = PhoneNumber
globals()['ProbationPeriod'] = ProbationPeriod
globals()['SocialLink'] = SocialLink
globals()['Tags'] = Tags
globals()['Team'] = Team
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
