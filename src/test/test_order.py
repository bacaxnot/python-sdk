"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.idempotency_key import IdempotencyKey
from apideck.model.order_customers import OrderCustomers
from apideck.model.order_discounts import OrderDiscounts
from apideck.model.order_fulfillments import OrderFulfillments
from apideck.model.order_line_items import OrderLineItems
from apideck.model.order_payments import OrderPayments
from apideck.model.order_refunds import OrderRefunds
from apideck.model.order_tenders import OrderTenders
from apideck.model.service_charges import ServiceCharges
globals()['Currency'] = Currency
globals()['IdempotencyKey'] = IdempotencyKey
globals()['OrderCustomers'] = OrderCustomers
globals()['OrderDiscounts'] = OrderDiscounts
globals()['OrderFulfillments'] = OrderFulfillments
globals()['OrderLineItems'] = OrderLineItems
globals()['OrderPayments'] = OrderPayments
globals()['OrderRefunds'] = OrderRefunds
globals()['OrderTenders'] = OrderTenders
globals()['ServiceCharges'] = ServiceCharges
from apideck.model.order import Order


class TestOrder(unittest.TestCase):
    """Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrder(self):
        """Test Order"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Order()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
