"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.linked_customer import LinkedCustomer
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
from apideck.model.payment_allocations import PaymentAllocations
globals()['Currency'] = Currency
globals()['LinkedCustomer'] = LinkedCustomer
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedSupplier'] = LinkedSupplier
globals()['PaymentAllocations'] = PaymentAllocations
from apideck.model.payment import Payment


class TestPayment(unittest.TestCase):
    """Payment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayment(self):
        """Test Payment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Payment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
