"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.1.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.employee import Employee
from apideck.model.payroll import Payroll
globals()['Employee'] = Employee
globals()['Payroll'] = Payroll
from apideck.model.employee_payrolls import EmployeePayrolls


class TestEmployeePayrolls(unittest.TestCase):
    """EmployeePayrolls unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeePayrolls(self):
        """Test EmployeePayrolls"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeePayrolls()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
