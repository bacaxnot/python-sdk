"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.currency import Currency
from apideck.model.payment_unit import PaymentUnit
globals()['Address'] = Address
globals()['Currency'] = Currency
globals()['PaymentUnit'] = PaymentUnit
from apideck.model.employee_job import EmployeeJob


class TestEmployeeJob(unittest.TestCase):
    """EmployeeJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeeJob(self):
        """Test EmployeeJob"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeeJob()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
