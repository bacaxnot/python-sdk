"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.company import Company
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Company'] = Company
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_companies_response import GetCompaniesResponse


class TestGetCompaniesResponse(unittest.TestCase):
    """GetCompaniesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetCompaniesResponse(self):
        """Test GetCompaniesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetCompaniesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
