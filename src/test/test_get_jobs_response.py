"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.job import Job
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Job'] = Job
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_jobs_response import GetJobsResponse


class TestGetJobsResponse(unittest.TestCase):
    """GetJobsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetJobsResponse(self):
        """Test GetJobsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetJobsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
