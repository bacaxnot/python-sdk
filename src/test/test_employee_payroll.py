"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.compensation import Compensation
from apideck.model.payroll_totals import PayrollTotals
globals()['Compensation'] = Compensation
globals()['PayrollTotals'] = PayrollTotals
from apideck.model.employee_payroll import EmployeePayroll


class TestEmployeePayroll(unittest.TestCase):
    """EmployeePayroll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeePayroll(self):
        """Test EmployeePayroll"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeePayroll()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
