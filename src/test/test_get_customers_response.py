"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.customer import Customer
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Customer'] = Customer
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_customers_response import GetCustomersResponse


class TestGetCustomersResponse(unittest.TestCase):
    """GetCustomersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetCustomersResponse(self):
        """Test GetCustomersResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetCustomersResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
