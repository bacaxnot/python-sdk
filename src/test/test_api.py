"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.api_resources import ApiResources
from apideck.model.api_status import ApiStatus
globals()['ApiResources'] = ApiResources
globals()['ApiStatus'] = ApiStatus
from apideck.model.api import Api


class TestApi(unittest.TestCase):
    """Api unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApi(self):
        """Test Api"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Api()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
