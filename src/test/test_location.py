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
globals()['Address'] = Address
globals()['Currency'] = Currency
globals()['PassThroughBody'] = PassThroughBody
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
