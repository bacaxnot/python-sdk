"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.purchase_order import PurchaseOrder
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['PurchaseOrder'] = PurchaseOrder
from apideck.model.get_purchase_orders_response import GetPurchaseOrdersResponse


class TestGetPurchaseOrdersResponse(unittest.TestCase):
    """GetPurchaseOrdersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPurchaseOrdersResponse(self):
        """Test GetPurchaseOrdersResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetPurchaseOrdersResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
