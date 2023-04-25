"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.customer_support_api import CustomerSupportApi  # noqa: E501


class TestCustomerSupportApi(unittest.TestCase):
    """CustomerSupportApi unit test stubs"""

    def setUp(self):
        self.api = CustomerSupportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_add(self):
        """Test case for customers_add

        Create Customer Support Customer  # noqa: E501
        """
        pass

    def test_customers_all(self):
        """Test case for customers_all

        List Customer Support Customers  # noqa: E501
        """
        pass

    def test_customers_delete(self):
        """Test case for customers_delete

        Delete Customer Support Customer  # noqa: E501
        """
        pass

    def test_customers_one(self):
        """Test case for customers_one

        Get Customer Support Customer  # noqa: E501
        """
        pass

    def test_customers_update(self):
        """Test case for customers_update

        Update Customer Support Customer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
