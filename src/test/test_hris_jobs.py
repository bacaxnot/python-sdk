"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.employee import Employee
from apideck.model.hris_job import HrisJob
globals()['Employee'] = Employee
globals()['HrisJob'] = HrisJob
from apideck.model.hris_jobs import HrisJobs


class TestHrisJobs(unittest.TestCase):
    """HrisJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHrisJobs(self):
        """Test HrisJobs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HrisJobs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
