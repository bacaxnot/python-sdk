"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.error import Error
from apideck.model.price import Price
globals()['Error'] = Error
globals()['Price'] = Price
from apideck.model.message import Message


class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessage(self):
        """Test Message"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Message()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
