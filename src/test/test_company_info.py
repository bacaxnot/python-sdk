"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.currency import Currency
from apideck.model.email import Email
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.phone_number import PhoneNumber
globals()['Address'] = Address
globals()['Currency'] = Currency
globals()['Email'] = Email
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['PhoneNumber'] = PhoneNumber
from apideck.model.company_info import CompanyInfo


class TestCompanyInfo(unittest.TestCase):
    """CompanyInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompanyInfo(self):
        """Test CompanyInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CompanyInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
