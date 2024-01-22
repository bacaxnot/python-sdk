"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.ecommerce_api import EcommerceApi  # noqa: E501


class TestEcommerceApi(unittest.TestCase):
    """EcommerceApi unit test stubs"""

    def setUp(self):
        self.api = EcommerceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_all(self):
        """Test case for customers_all

        List Customers  # noqa: E501
        """
        pass

    def test_customers_one(self):
        """Test case for customers_one

        Get Customer  # noqa: E501
        """
        pass

    def test_orders_all(self):
        """Test case for orders_all

        List Orders  # noqa: E501
        """
        pass

    def test_orders_one(self):
        """Test case for orders_one

        Get Order  # noqa: E501
        """
        pass

    def test_products_all(self):
        """Test case for products_all

        List Products  # noqa: E501
        """
        pass

    def test_products_one(self):
        """Test case for products_one

        Get Product  # noqa: E501
        """
        pass

    def test_stores_one(self):
        """Test case for stores_one

        Get Store  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
