"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.5.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.application_stage import ApplicationStage
from apideck.model.pass_through_body import PassThroughBody
globals()['ApplicationStage'] = ApplicationStage
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.application import Application


class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplication(self):
        """Test Application"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Application()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
