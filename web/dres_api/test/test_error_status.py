# coding: utf-8

"""
    DRES API

    API for DRES (Distributed Retrieval Evaluation Server), Version 1.0

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dres_api.models.error_status import ErrorStatus  # noqa: E501

class TestErrorStatus(unittest.TestCase):
    """ErrorStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorStatus:
        """Test ErrorStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorStatus`
        """
        model = ErrorStatus()  # noqa: E501
        if include_optional:
            return ErrorStatus(
                description = '',
                status = True
            )
        else:
            return ErrorStatus(
                description = '',
                status = True,
        )
        """

    def testErrorStatus(self):
        """Test ErrorStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
