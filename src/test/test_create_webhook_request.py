"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.delivery_url import DeliveryUrl
from apideck.model.status import Status
from apideck.model.unified_api_id import UnifiedApiId
from apideck.model.webhook_event_type import WebhookEventType
globals()['DeliveryUrl'] = DeliveryUrl
globals()['Status'] = Status
globals()['UnifiedApiId'] = UnifiedApiId
globals()['WebhookEventType'] = WebhookEventType
from apideck.model.create_webhook_request import CreateWebhookRequest


class TestCreateWebhookRequest(unittest.TestCase):
    """CreateWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateWebhookRequest(self):
        """Test CreateWebhookRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateWebhookRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
