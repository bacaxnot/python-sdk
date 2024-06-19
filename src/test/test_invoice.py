"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.invoice_line_item import InvoiceLineItem
from apideck.model.linked_customer import LinkedCustomer
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tracking_category import LinkedTrackingCategory
from apideck.model.pass_through_body import PassThroughBody
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['InvoiceLineItem'] = InvoiceLineItem
globals()['LinkedCustomer'] = LinkedCustomer
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTrackingCategory'] = LinkedTrackingCategory
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.invoice import Invoice


class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoice(self):
        """Test Invoice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Invoice()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
