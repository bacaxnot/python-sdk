"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.benefit import Benefit
from apideck.model.deduction import Deduction
from apideck.model.tax import Tax
globals()['Benefit'] = Benefit
globals()['Deduction'] = Deduction
globals()['Tax'] = Tax
from apideck.model.compensation import Compensation


class TestCompensation(unittest.TestCase):
    """Compensation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompensation(self):
        """Test Compensation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Compensation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
