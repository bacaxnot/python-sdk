"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.delivery_url import DeliveryUrl
from apideck.model.status import Status
from apideck.model.webhook_event_type import WebhookEventType
globals()['DeliveryUrl'] = DeliveryUrl
globals()['Status'] = Status
globals()['WebhookEventType'] = WebhookEventType
from apideck.model.update_webhook_request import UpdateWebhookRequest


class TestUpdateWebhookRequest(unittest.TestCase):
    """UpdateWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateWebhookRequest(self):
        """Test UpdateWebhookRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateWebhookRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
