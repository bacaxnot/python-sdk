"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.currency import Currency
from apideck.model.pass_through_body import PassThroughBody
from apideck.model.service_charge import ServiceCharge
globals()['Address'] = Address
globals()['Currency'] = Currency
globals()['PassThroughBody'] = PassThroughBody
globals()['ServiceCharge'] = ServiceCharge
from apideck.model.merchant import Merchant


class TestMerchant(unittest.TestCase):
    """Merchant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMerchant(self):
        """Test Merchant"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Merchant()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
