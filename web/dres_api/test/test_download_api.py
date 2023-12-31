# coding: utf-8

"""
    DRES API

    API for DRES (Distributed Retrieval Evaluation Server), Version 1.0

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dres_api.api.download_api import DownloadApi  # noqa: E501


class TestDownloadApi(unittest.TestCase):
    """DownloadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DownloadApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_api_v1_download_competition_with_competitionid(self) -> None:
        """Test case for get_api_v1_download_competition_with_competitionid

        Provides a JSON download of the entire competition description structure.  # noqa: E501
        """
        pass

    def test_get_api_v1_download_run_with_runid(self) -> None:
        """Test case for get_api_v1_download_run_with_runid

        Provides a JSON download of the entire competition run structure.  # noqa: E501
        """
        pass

    def test_get_api_v1_download_run_with_runid_scores(self) -> None:
        """Test case for get_api_v1_download_run_with_runid_scores

        Provides a CSV download with the scores for a given competition run.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
