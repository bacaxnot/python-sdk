"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.tax_rate import TaxRate
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['TaxRate'] = TaxRate
from apideck.model.get_tax_rates_response import GetTaxRatesResponse


class TestGetTaxRatesResponse(unittest.TestCase):
    """GetTaxRatesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTaxRatesResponse(self):
        """Test GetTaxRatesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetTaxRatesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
