"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.tender import Tender
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['Tender'] = Tender
from apideck.model.get_tenders_response import GetTendersResponse


class TestGetTendersResponse(unittest.TestCase):
    """GetTendersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTendersResponse(self):
        """Test GetTendersResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetTendersResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
