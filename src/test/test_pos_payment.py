"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.cash_details import CashDetails
from apideck.model.currency import Currency
from apideck.model.idempotency_key import IdempotencyKey
from apideck.model.pos_bank_account import PosBankAccount
from apideck.model.pos_payment_card_details import PosPaymentCardDetails
from apideck.model.pos_payment_external_details import PosPaymentExternalDetails
from apideck.model.service_charges import ServiceCharges
from apideck.model.wallet_details import WalletDetails
globals()['CashDetails'] = CashDetails
globals()['Currency'] = Currency
globals()['IdempotencyKey'] = IdempotencyKey
globals()['PosBankAccount'] = PosBankAccount
globals()['PosPaymentCardDetails'] = PosPaymentCardDetails
globals()['PosPaymentExternalDetails'] = PosPaymentExternalDetails
globals()['ServiceCharges'] = ServiceCharges
globals()['WalletDetails'] = WalletDetails
from apideck.model.pos_payment import PosPayment


class TestPosPayment(unittest.TestCase):
    """PosPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPosPayment(self):
        """Test PosPayment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PosPayment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
