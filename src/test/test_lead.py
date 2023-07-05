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
from apideck.model.custom_field import CustomField
from apideck.model.email import Email
from apideck.model.phone_number import PhoneNumber
from apideck.model.social_link import SocialLink
from apideck.model.tags import Tags
from apideck.model.website import Website
globals()['Address'] = Address
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
globals()['SocialLink'] = SocialLink
globals()['Tags'] = Tags
globals()['Website'] = Website
from apideck.model.lead import Lead


class TestLead(unittest.TestCase):
    """Lead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLead(self):
        """Test Lead"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Lead()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
