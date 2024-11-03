#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json

class TestGetJson(unittest.TestCase):
    """Tests for the get_json function in utils."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns expected output and mocks requests.get."""
        with patch('utils.requests.get') as mock_get:
            # Create a Mock response object and set the json method return value
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and verify it returns test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Check that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

if __name__ == "__main__":
    unittest.main()
