"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.invoice_item_sales_details import InvoiceItemSalesDetails
from apideck.model.linked_ledger_account import LinkedLedgerAccount
globals()['InvoiceItemSalesDetails'] = InvoiceItemSalesDetails
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
from apideck.model.invoice_item import InvoiceItem


class TestInvoiceItem(unittest.TestCase):
    """InvoiceItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoiceItem(self):
        """Test InvoiceItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InvoiceItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
