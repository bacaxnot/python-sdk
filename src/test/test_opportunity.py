"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.tags import Tags
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['Tags'] = Tags
from apideck.model.opportunity import Opportunity


class TestOpportunity(unittest.TestCase):
    """Opportunity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOpportunity(self):
        """Test Opportunity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Opportunity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
