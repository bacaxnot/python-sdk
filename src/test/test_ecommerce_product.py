"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.ecommerce_product_categories import EcommerceProductCategories
from apideck.model.ecommerce_product_images import EcommerceProductImages
from apideck.model.ecommerce_product_options import EcommerceProductOptions
from apideck.model.ecommerce_product_variants import EcommerceProductVariants
globals()['EcommerceProductCategories'] = EcommerceProductCategories
globals()['EcommerceProductImages'] = EcommerceProductImages
globals()['EcommerceProductOptions'] = EcommerceProductOptions
globals()['EcommerceProductVariants'] = EcommerceProductVariants
from apideck.model.ecommerce_product import EcommerceProduct


class TestEcommerceProduct(unittest.TestCase):
    """EcommerceProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEcommerceProduct(self):
        """Test EcommerceProduct"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EcommerceProduct()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
