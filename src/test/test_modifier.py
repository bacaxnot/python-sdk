"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.idempotency_key import IdempotencyKey
globals()['Currency'] = Currency
globals()['IdempotencyKey'] = IdempotencyKey
from apideck.model.modifier import Modifier


class TestModifier(unittest.TestCase):
    """Modifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModifier(self):
        """Test Modifier"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Modifier()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
