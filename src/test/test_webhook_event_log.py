"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.unified_api_id import UnifiedApiId
from apideck.model.webhook_event_log_attempts import WebhookEventLogAttempts
from apideck.model.webhook_event_log_service import WebhookEventLogService
globals()['UnifiedApiId'] = UnifiedApiId
globals()['WebhookEventLogAttempts'] = WebhookEventLogAttempts
globals()['WebhookEventLogService'] = WebhookEventLogService
from apideck.model.webhook_event_log import WebhookEventLog


class TestWebhookEventLog(unittest.TestCase):
    """WebhookEventLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookEventLog(self):
        """Test WebhookEventLog"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookEventLog()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
