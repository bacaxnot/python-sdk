"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.ecommerce_customer_addresses import EcommerceCustomerAddresses
from apideck.model.email import Email
from apideck.model.linked_ecommerce_order import LinkedEcommerceOrder
from apideck.model.phone_number import PhoneNumber
globals()['Currency'] = Currency
globals()['EcommerceCustomerAddresses'] = EcommerceCustomerAddresses
globals()['Email'] = Email
globals()['LinkedEcommerceOrder'] = LinkedEcommerceOrder
globals()['PhoneNumber'] = PhoneNumber
from apideck.model.ecommerce_customer import EcommerceCustomer


class TestEcommerceCustomer(unittest.TestCase):
    """EcommerceCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEcommerceCustomer(self):
        """Test EcommerceCustomer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EcommerceCustomer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
