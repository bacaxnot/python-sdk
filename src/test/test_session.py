"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.consumer_metadata import ConsumerMetadata
from apideck.model.session_settings import SessionSettings
from apideck.model.session_theme import SessionTheme
globals()['ConsumerMetadata'] = ConsumerMetadata
globals()['SessionSettings'] = SessionSettings
globals()['SessionTheme'] = SessionTheme
from apideck.model.session import Session


class TestSession(unittest.TestCase):
    """Session unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSession(self):
        """Test Session"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Session()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
