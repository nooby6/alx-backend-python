#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization data."""
        # Set the mock to return the expected response
        mock_get_json.return_value = expected_response

        # Initialize GithubOrgClient with org_name and get org data
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Verify that org returns the expected response
        self.assertEqual(result, expected_response)

if __name__ == "__main__":
    unittest.main()
