"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.activity_attendee import ActivityAttendee
from apideck.model.address import Address
from apideck.model.custom_field import CustomField
globals()['ActivityAttendee'] = ActivityAttendee
globals()['Address'] = Address
globals()['CustomField'] = CustomField
from apideck.model.activity import Activity


class TestActivity(unittest.TestCase):
    """Activity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActivity(self):
        """Test Activity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Activity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
