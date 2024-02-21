"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.branch import Branch
from apideck.model.custom_field import CustomField
from apideck.model.department import Department
from apideck.model.job_links import JobLinks
from apideck.model.job_salary import JobSalary
from apideck.model.job_status import JobStatus
from apideck.model.tags import Tags
globals()['Address'] = Address
globals()['Branch'] = Branch
globals()['CustomField'] = CustomField
globals()['Department'] = Department
globals()['JobLinks'] = JobLinks
globals()['JobSalary'] = JobSalary
globals()['JobStatus'] = JobStatus
globals()['Tags'] = Tags
from apideck.model.job import Job


class TestJob(unittest.TestCase):
    """Job unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJob(self):
        """Test Job"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Job()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
