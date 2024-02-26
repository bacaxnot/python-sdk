"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.ecommerce_address import EcommerceAddress
from apideck.model.ecommerce_discount import EcommerceDiscount
from apideck.model.ecommerce_order_line_item import EcommerceOrderLineItem
from apideck.model.ecommerce_order_status import EcommerceOrderStatus
from apideck.model.linked_ecommerce_customer import LinkedEcommerceCustomer
from apideck.model.tracking_item import TrackingItem
globals()['Currency'] = Currency
globals()['EcommerceAddress'] = EcommerceAddress
globals()['EcommerceDiscount'] = EcommerceDiscount
globals()['EcommerceOrderLineItem'] = EcommerceOrderLineItem
globals()['EcommerceOrderStatus'] = EcommerceOrderStatus
globals()['LinkedEcommerceCustomer'] = LinkedEcommerceCustomer
globals()['TrackingItem'] = TrackingItem
from apideck.model.ecommerce_order import EcommerceOrder


class TestEcommerceOrder(unittest.TestCase):
    """EcommerceOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEcommerceOrder(self):
        """Test EcommerceOrder"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EcommerceOrder()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
