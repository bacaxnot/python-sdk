"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.invoice_line_item import InvoiceLineItem
from apideck.model.linked_customer import LinkedCustomer
from apideck.model.linked_ledger_account import LinkedLedgerAccount
globals()['Currency'] = Currency
globals()['InvoiceLineItem'] = InvoiceLineItem
globals()['LinkedCustomer'] = LinkedCustomer
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
from apideck.model.credit_note import CreditNote


class TestCreditNote(unittest.TestCase):
    """CreditNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreditNote(self):
        """Test CreditNote"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreditNote()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
