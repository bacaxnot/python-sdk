"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.custom_field import CustomField
from apideck.model.linked_invoice_item import LinkedInvoiceItem
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
globals()['CustomField'] = CustomField
globals()['LinkedInvoiceItem'] = LinkedInvoiceItem
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
from apideck.model.invoice_line_item import InvoiceLineItem


class TestInvoiceLineItem(unittest.TestCase):
    """InvoiceLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoiceLineItem(self):
        """Test InvoiceLineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InvoiceLineItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
