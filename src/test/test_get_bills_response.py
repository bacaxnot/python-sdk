"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.bill import Bill
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Bill'] = Bill
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_bills_response import GetBillsResponse


class TestGetBillsResponse(unittest.TestCase):
    """GetBillsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetBillsResponse(self):
        """Test GetBillsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetBillsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
