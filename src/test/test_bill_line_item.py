"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.linked_invoice_item import LinkedInvoiceItem
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
globals()['LinkedInvoiceItem'] = LinkedInvoiceItem
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
from apideck.model.bill_line_item import BillLineItem


class TestBillLineItem(unittest.TestCase):
    """BillLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBillLineItem(self):
        """Test BillLineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BillLineItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
