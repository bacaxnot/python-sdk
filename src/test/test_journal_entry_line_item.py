"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.linked_tracking_category import LinkedTrackingCategory
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['LinkedTrackingCategory'] = LinkedTrackingCategory
from apideck.model.journal_entry_line_item import JournalEntryLineItem


class TestJournalEntryLineItem(unittest.TestCase):
    """JournalEntryLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJournalEntryLineItem(self):
        """Test JournalEntryLineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JournalEntryLineItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
