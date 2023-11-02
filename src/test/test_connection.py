"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.auth_type import AuthType
from apideck.model.connection_configuration import ConnectionConfiguration
from apideck.model.connection_state import ConnectionState
from apideck.model.custom_mapping import CustomMapping
from apideck.model.form_field import FormField
from apideck.model.integration_state import IntegrationState
from apideck.model.o_auth_grant_type import OAuthGrantType
from apideck.model.webhook_subscription import WebhookSubscription
globals()['AuthType'] = AuthType
globals()['ConnectionConfiguration'] = ConnectionConfiguration
globals()['ConnectionState'] = ConnectionState
globals()['CustomMapping'] = CustomMapping
globals()['FormField'] = FormField
globals()['IntegrationState'] = IntegrationState
globals()['OAuthGrantType'] = OAuthGrantType
globals()['WebhookSubscription'] = WebhookSubscription
from apideck.model.connection import Connection


class TestConnection(unittest.TestCase):
    """Connection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnection(self):
        """Test Connection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Connection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
