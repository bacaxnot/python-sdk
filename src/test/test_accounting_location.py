"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.pass_through_body import PassThroughBody
from apideck.model.subsidiary_reference import SubsidiaryReference
globals()['Address'] = Address
globals()['PassThroughBody'] = PassThroughBody
globals()['SubsidiaryReference'] = SubsidiaryReference
from apideck.model.accounting_location import AccountingLocation


class TestAccountingLocation(unittest.TestCase):
    """AccountingLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountingLocation(self):
        """Test AccountingLocation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountingLocation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
