"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.webhook_event_log import WebhookEventLog
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['WebhookEventLog'] = WebhookEventLog
from apideck.model.get_webhook_event_logs_response import GetWebhookEventLogsResponse


class TestGetWebhookEventLogsResponse(unittest.TestCase):
    """GetWebhookEventLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetWebhookEventLogsResponse(self):
        """Test GetWebhookEventLogsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetWebhookEventLogsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
