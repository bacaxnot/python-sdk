"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.ticket import Ticket
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['Ticket'] = Ticket
from apideck.model.get_tickets_response import GetTicketsResponse


class TestGetTicketsResponse(unittest.TestCase):
    """GetTicketsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTicketsResponse(self):
        """Test GetTicketsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetTicketsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
