"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.applicant_social_links import ApplicantSocialLinks
from apideck.model.applicant_websites import ApplicantWebsites
from apideck.model.custom_field import CustomField
from apideck.model.email import Email
from apideck.model.phone_number import PhoneNumber
from apideck.model.tags import Tags
globals()['Address'] = Address
globals()['ApplicantSocialLinks'] = ApplicantSocialLinks
globals()['ApplicantWebsites'] = ApplicantWebsites
globals()['CustomField'] = CustomField
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
globals()['Tags'] = Tags
from apideck.model.applicant import Applicant


class TestApplicant(unittest.TestCase):
    """Applicant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicant(self):
        """Test Applicant"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Applicant()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
