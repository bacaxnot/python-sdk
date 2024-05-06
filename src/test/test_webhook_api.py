"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.webhook_api import WebhookApi  # noqa: E501


class TestWebhookApi(unittest.TestCase):
    """WebhookApi unit test stubs"""

    def setUp(self):
        self.api = WebhookApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_logs_all(self):
        """Test case for event_logs_all

        List event logs  # noqa: E501
        """
        pass

    def test_webhooks_add(self):
        """Test case for webhooks_add

        Create webhook subscription  # noqa: E501
        """
        pass

    def test_webhooks_all(self):
        """Test case for webhooks_all

        List webhook subscriptions  # noqa: E501
        """
        pass

    def test_webhooks_delete(self):
        """Test case for webhooks_delete

        Delete webhook subscription  # noqa: E501
        """
        pass

    def test_webhooks_one(self):
        """Test case for webhooks_one

        Get webhook subscription  # noqa: E501
        """
        pass

    def test_webhooks_update(self):
        """Test case for webhooks_update

        Update webhook subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
