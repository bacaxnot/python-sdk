"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.journal_entry_line_item import JournalEntryLineItem
from apideck.model.linked_tracking_categories import LinkedTrackingCategories
from apideck.model.pass_through_body import PassThroughBody
globals()['Currency'] = Currency
globals()['JournalEntryLineItem'] = JournalEntryLineItem
globals()['LinkedTrackingCategories'] = LinkedTrackingCategories
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.journal_entry import JournalEntry


class TestJournalEntry(unittest.TestCase):
    """JournalEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJournalEntry(self):
        """Test JournalEntry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JournalEntry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
