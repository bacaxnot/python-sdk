"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.webhook import Webhook
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['Webhook'] = Webhook
from apideck.model.get_webhooks_response import GetWebhooksResponse


class TestGetWebhooksResponse(unittest.TestCase):
    """GetWebhooksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetWebhooksResponse(self):
        """Test GetWebhooksResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetWebhooksResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
