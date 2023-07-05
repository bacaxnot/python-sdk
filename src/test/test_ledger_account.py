"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.ledger_account_categories import LedgerAccountCategories
from apideck.model.ledger_account_parent_account import LedgerAccountParentAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['LedgerAccountCategories'] = LedgerAccountCategories
globals()['LedgerAccountParentAccount'] = LedgerAccountParentAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
from apideck.model.ledger_account import LedgerAccount


class TestLedgerAccount(unittest.TestCase):
    """LedgerAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLedgerAccount(self):
        """Test LedgerAccount"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LedgerAccount()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
