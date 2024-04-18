"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.invoice_line_item import InvoiceLineItem
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['InvoiceLineItem'] = InvoiceLineItem
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedSupplier'] = LinkedSupplier
from apideck.model.purchase_order import PurchaseOrder


class TestPurchaseOrder(unittest.TestCase):
    """PurchaseOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPurchaseOrder(self):
        """Test PurchaseOrder"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PurchaseOrder()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
