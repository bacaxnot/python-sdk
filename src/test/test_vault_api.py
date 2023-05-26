"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.5.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.vault_api import VaultApi  # noqa: E501


class TestVaultApi(unittest.TestCase):
    """VaultApi unit test stubs"""

    def setUp(self):
        self.api = VaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connection_settings_all(self):
        """Test case for connection_settings_all

        Get resource settings  # noqa: E501
        """
        pass

    def test_connection_settings_update(self):
        """Test case for connection_settings_update

        Update settings  # noqa: E501
        """
        pass

    def test_connections_all(self):
        """Test case for connections_all

        Get all connections  # noqa: E501
        """
        pass

    def test_connections_delete(self):
        """Test case for connections_delete

        Deletes a connection  # noqa: E501
        """
        pass

    def test_connections_import(self):
        """Test case for connections_import

        Import connection  # noqa: E501
        """
        pass

    def test_connections_one(self):
        """Test case for connections_one

        Get connection  # noqa: E501
        """
        pass

    def test_connections_update(self):
        """Test case for connections_update

        Update connection  # noqa: E501
        """
        pass

    def test_consumer_request_counts_all(self):
        """Test case for consumer_request_counts_all

        Consumer request counts  # noqa: E501
        """
        pass

    def test_consumers_add(self):
        """Test case for consumers_add

        Create consumer  # noqa: E501
        """
        pass

    def test_consumers_all(self):
        """Test case for consumers_all

        Get all consumers  # noqa: E501
        """
        pass

    def test_consumers_delete(self):
        """Test case for consumers_delete

        Delete consumer  # noqa: E501
        """
        pass

    def test_consumers_one(self):
        """Test case for consumers_one

        Get consumer  # noqa: E501
        """
        pass

    def test_consumers_update(self):
        """Test case for consumers_update

        Update consumer  # noqa: E501
        """
        pass

    def test_logs_all(self):
        """Test case for logs_all

        Get all consumer request logs  # noqa: E501
        """
        pass

    def test_sessions_create(self):
        """Test case for sessions_create

        Create Session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
