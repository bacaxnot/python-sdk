"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.order import Order
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['Order'] = Order
from apideck.model.get_orders_response import GetOrdersResponse


class TestGetOrdersResponse(unittest.TestCase):
    """GetOrdersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetOrdersResponse(self):
        """Test GetOrdersResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetOrdersResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
