"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.contact import Contact
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Contact'] = Contact
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_contacts_response import GetContactsResponse


class TestGetContactsResponse(unittest.TestCase):
    """GetContactsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetContactsResponse(self):
        """Test GetContactsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetContactsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
