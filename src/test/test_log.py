"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.log_operation import LogOperation
from apideck.model.log_service import LogService
globals()['LogOperation'] = LogOperation
globals()['LogService'] = LogService
from apideck.model.log import Log


class TestLog(unittest.TestCase):
    """Log unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLog(self):
        """Test Log"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Log()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
