"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.shared_link import SharedLink
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['SharedLink'] = SharedLink
from apideck.model.get_shared_links_response import GetSharedLinksResponse


class TestGetSharedLinksResponse(unittest.TestCase):
    """GetSharedLinksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetSharedLinksResponse(self):
        """Test GetSharedLinksResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetSharedLinksResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
