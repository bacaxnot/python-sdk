"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.currency import Currency
from apideck.model.pipeline_stages import PipelineStages
globals()['Currency'] = Currency
globals()['PipelineStages'] = PipelineStages
from apideck.model.pipeline import Pipeline


class TestPipeline(unittest.TestCase):
    """Pipeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPipeline(self):
        """Test Pipeline"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Pipeline()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
