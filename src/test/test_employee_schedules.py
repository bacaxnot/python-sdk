"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.employee import Employee
from apideck.model.schedule import Schedule
globals()['Employee'] = Employee
globals()['Schedule'] = Schedule
from apideck.model.employee_schedules import EmployeeSchedules


class TestEmployeeSchedules(unittest.TestCase):
    """EmployeeSchedules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeeSchedules(self):
        """Test EmployeeSchedules"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeeSchedules()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
