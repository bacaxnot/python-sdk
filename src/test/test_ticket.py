"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.assignee import Assignee
from apideck.model.collection_tag import CollectionTag
from apideck.model.pass_through_body import PassThroughBody
globals()['Assignee'] = Assignee
globals()['CollectionTag'] = CollectionTag
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.ticket import Ticket


class TestTicket(unittest.TestCase):
    """Ticket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicket(self):
        """Test Ticket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Ticket()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
