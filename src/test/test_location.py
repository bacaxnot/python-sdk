"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.currency import Currency
globals()['Address'] = Address
globals()['Currency'] = Currency
from apideck.model.location import Location


class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocation(self):
        """Test Location"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Location()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
