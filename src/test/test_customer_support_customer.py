"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.1.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.email import Email
from apideck.model.phone_number import PhoneNumber
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
from apideck.model.customer_support_customer import CustomerSupportCustomer


class TestCustomerSupportCustomer(unittest.TestCase):
    """CustomerSupportCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerSupportCustomer(self):
        """Test CustomerSupportCustomer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomerSupportCustomer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
