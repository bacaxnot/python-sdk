"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.folder import Folder
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Folder'] = Folder
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_folders_response import GetFoldersResponse


class TestGetFoldersResponse(unittest.TestCase):
    """GetFoldersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetFoldersResponse(self):
        """Test GetFoldersResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetFoldersResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
