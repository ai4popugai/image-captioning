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

from openapi_client.models.result_element import ResultElement  # noqa: E501

class TestResultElement(unittest.TestCase):
    """ResultElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultElement:
        """Test ResultElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultElement`
        """
        model = ResultElement()  # noqa: E501
        if include_optional:
            return ResultElement(
                item = '',
                text = '',
                start_time_code = '',
                end_time_code = '',
                index = 56,
                rank = 56,
                weight = 1.337
            )
        else:
            return ResultElement(
        )
        """

    def testResultElement(self):
        """Test ResultElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
