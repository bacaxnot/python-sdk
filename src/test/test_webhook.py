"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.delivery_url import DeliveryUrl
from apideck.model.execute_base_url import ExecuteBaseUrl
from apideck.model.status import Status
from apideck.model.unified_api_id import UnifiedApiId
from apideck.model.webhook_event_type import WebhookEventType
globals()['DeliveryUrl'] = DeliveryUrl
globals()['ExecuteBaseUrl'] = ExecuteBaseUrl
globals()['Status'] = Status
globals()['UnifiedApiId'] = UnifiedApiId
globals()['WebhookEventType'] = WebhookEventType
from apideck.model.webhook import Webhook


class TestWebhook(unittest.TestCase):
    """Webhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhook(self):
        """Test Webhook"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Webhook()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
