"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.custom_field import CustomField
from apideck.model.email import Email
from apideck.model.phone_number import PhoneNumber
from apideck.model.social_link import SocialLink
from apideck.model.tags import Tags
from apideck.model.website import Website
globals()['Address'] = Address
globals()['CustomField'] = CustomField
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
globals()['SocialLink'] = SocialLink
globals()['Tags'] = Tags
globals()['Website'] = Website
from apideck.model.contact import Contact


class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContact(self):
        """Test Contact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Contact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
