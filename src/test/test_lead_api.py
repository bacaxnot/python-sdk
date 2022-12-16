"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.lead_api import LeadApi  # noqa: E501


class TestLeadApi(unittest.TestCase):
    """LeadApi unit test stubs"""

    def setUp(self):
        self.api = LeadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_leads_add(self):
        """Test case for leads_add

        Create lead  # noqa: E501
        """
        pass

    def test_leads_all(self):
        """Test case for leads_all

        List leads  # noqa: E501
        """
        pass

    def test_leads_delete(self):
        """Test case for leads_delete

        Delete lead  # noqa: E501
        """
        pass

    def test_leads_one(self):
        """Test case for leads_one

        Get lead  # noqa: E501
        """
        pass

    def test_leads_update(self):
        """Test case for leads_update

        Update lead  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
