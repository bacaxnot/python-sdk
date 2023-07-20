"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.email import Email
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.phone_number import PhoneNumber
from apideck.model.website import Website
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['Email'] = Email
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['PhoneNumber'] = PhoneNumber
globals()['Website'] = Website
from apideck.model.supplier import Supplier


class TestSupplier(unittest.TestCase):
    """Supplier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSupplier(self):
        """Test Supplier"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Supplier()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
