"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.consumer_connection import ConsumerConnection
from apideck.model.consumer_metadata import ConsumerMetadata
from apideck.model.request_count_allocation import RequestCountAllocation
globals()['ConsumerConnection'] = ConsumerConnection
globals()['ConsumerMetadata'] = ConsumerMetadata
globals()['RequestCountAllocation'] = RequestCountAllocation
from apideck.model.consumer import Consumer


class TestConsumer(unittest.TestCase):
    """Consumer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConsumer(self):
        """Test Consumer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Consumer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
