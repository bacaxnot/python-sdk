"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.employee import Employee
from apideck.model.links import Links
from apideck.model.meta import Meta
globals()['Employee'] = Employee
globals()['Links'] = Links
globals()['Meta'] = Meta
from apideck.model.get_employees_response import GetEmployeesResponse


class TestGetEmployeesResponse(unittest.TestCase):
    """GetEmployeesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetEmployeesResponse(self):
        """Test GetEmployeesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetEmployeesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
