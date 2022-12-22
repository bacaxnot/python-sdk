"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.email import Email
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.phone_number import PhoneNumber
from apideck.model.website import Website
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['Email'] = Email
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['PhoneNumber'] = PhoneNumber
globals()['Website'] = Website
from apideck.model.accounting_customer import AccountingCustomer


class TestAccountingCustomer(unittest.TestCase):
    """AccountingCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountingCustomer(self):
        """Test AccountingCustomer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountingCustomer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
