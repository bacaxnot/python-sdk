"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.ecommerce_product import EcommerceProduct
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['EcommerceProduct'] = EcommerceProduct
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_products_response import GetProductsResponse


class TestGetProductsResponse(unittest.TestCase):
    """GetProductsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetProductsResponse(self):
        """Test GetProductsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetProductsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
