"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.idempotency_key import IdempotencyKey
globals()['Currency'] = Currency
globals()['IdempotencyKey'] = IdempotencyKey
from apideck.model.item import Item


class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testItem(self):
        """Test Item"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Item()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
