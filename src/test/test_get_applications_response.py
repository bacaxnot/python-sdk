"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.application import Application
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Application'] = Application
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_applications_response import GetApplicationsResponse


class TestGetApplicationsResponse(unittest.TestCase):
    """GetApplicationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetApplicationsResponse(self):
        """Test GetApplicationsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetApplicationsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
