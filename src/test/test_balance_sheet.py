"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.balance_sheet_assets import BalanceSheetAssets
from apideck.model.balance_sheet_equity import BalanceSheetEquity
from apideck.model.balance_sheet_liabilities import BalanceSheetLiabilities
globals()['BalanceSheetAssets'] = BalanceSheetAssets
globals()['BalanceSheetEquity'] = BalanceSheetEquity
globals()['BalanceSheetLiabilities'] = BalanceSheetLiabilities
from apideck.model.balance_sheet import BalanceSheet


class TestBalanceSheet(unittest.TestCase):
    """BalanceSheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBalanceSheet(self):
        """Test BalanceSheet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BalanceSheet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
