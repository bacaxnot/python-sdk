"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.order_type import OrderType
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['OrderType'] = OrderType
from apideck.model.get_order_types_response import GetOrderTypesResponse


class TestGetOrderTypesResponse(unittest.TestCase):
    """GetOrderTypesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetOrderTypesResponse(self):
        """Test GetOrderTypesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetOrderTypesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
