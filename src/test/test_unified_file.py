"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.file_type import FileType
from apideck.model.linked_folder import LinkedFolder
from apideck.model.owner import Owner
from apideck.model.unified_file_permissions import UnifiedFilePermissions
globals()['FileType'] = FileType
globals()['LinkedFolder'] = LinkedFolder
globals()['Owner'] = Owner
globals()['UnifiedFilePermissions'] = UnifiedFilePermissions
from apideck.model.unified_file import UnifiedFile


class TestUnifiedFile(unittest.TestCase):
    """UnifiedFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUnifiedFile(self):
        """Test UnifiedFile"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UnifiedFile()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
