"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.1.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.issue_tracking_api import IssueTrackingApi  # noqa: E501


class TestIssueTrackingApi(unittest.TestCase):
    """IssueTrackingApi unit test stubs"""

    def setUp(self):
        self.api = IssueTrackingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_collection_tags_all(self):
        """Test case for collection_tags_all

        List Tags  # noqa: E501
        """
        pass

    def test_collection_ticket_comments_add(self):
        """Test case for collection_ticket_comments_add

        Create Comment  # noqa: E501
        """
        pass

    def test_collection_ticket_comments_all(self):
        """Test case for collection_ticket_comments_all

        List Comments  # noqa: E501
        """
        pass

    def test_collection_ticket_comments_delete(self):
        """Test case for collection_ticket_comments_delete

        Delete Comment  # noqa: E501
        """
        pass

    def test_collection_ticket_comments_one(self):
        """Test case for collection_ticket_comments_one

        Get Comment  # noqa: E501
        """
        pass

    def test_collection_ticket_comments_update(self):
        """Test case for collection_ticket_comments_update

        Update Comment  # noqa: E501
        """
        pass

    def test_collection_tickets_add(self):
        """Test case for collection_tickets_add

        Create Ticket  # noqa: E501
        """
        pass

    def test_collection_tickets_all(self):
        """Test case for collection_tickets_all

        List Tickets  # noqa: E501
        """
        pass

    def test_collection_tickets_delete(self):
        """Test case for collection_tickets_delete

        Delete Ticket  # noqa: E501
        """
        pass

    def test_collection_tickets_one(self):
        """Test case for collection_tickets_one

        Get Ticket  # noqa: E501
        """
        pass

    def test_collection_tickets_update(self):
        """Test case for collection_tickets_update

        Update Ticket  # noqa: E501
        """
        pass

    def test_collection_users_all(self):
        """Test case for collection_users_all

        List Users  # noqa: E501
        """
        pass

    def test_collection_users_one(self):
        """Test case for collection_users_one

        Get user  # noqa: E501
        """
        pass

    def test_collections_all(self):
        """Test case for collections_all

        List Collections  # noqa: E501
        """
        pass

    def test_collections_one(self):
        """Test case for collections_one

        Get Collection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
