"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.compensation import Compensation
from apideck.model.payroll_totals import PayrollTotals
globals()['Compensation'] = Compensation
globals()['PayrollTotals'] = PayrollTotals
from apideck.model.payroll import Payroll


class TestPayroll(unittest.TestCase):
    """Payroll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayroll(self):
        """Test Payroll"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Payroll()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
