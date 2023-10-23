"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.3
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.sms_api import SmsApi  # noqa: E501


class TestSmsApi(unittest.TestCase):
    """SmsApi unit test stubs"""

    def setUp(self):
        self.api = SmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_messages_add(self):
        """Test case for messages_add

        Create Message  # noqa: E501
        """
        pass

    def test_messages_all(self):
        """Test case for messages_all

        List Messages  # noqa: E501
        """
        pass

    def test_messages_delete(self):
        """Test case for messages_delete

        Delete Message  # noqa: E501
        """
        pass

    def test_messages_one(self):
        """Test case for messages_one

        Get Message  # noqa: E501
        """
        pass

    def test_messages_update(self):
        """Test case for messages_update

        Update Message  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
