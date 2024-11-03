#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient  # Import your GithubOrgClient
from fixtures import repos_payload, expected_repos, apache2_repos  # Import fixture data

class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function in utils module."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError with invalid path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test suite for get_json function in utils module."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns expected result with mocked requests.get."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test suite for memoize decorator in utils module."""

    def test_memoize(self):
        """Test that memoize caches the result of a_method."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient."""

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method returns expected repos list."""
        # Arrange
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = repos_payload

        # Act
        client = GithubOrgClient("example_org")
        result = client.public_repos()

        # Assert
        self.assertEqual(result, expected_repos)
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock)
    def test_public_repos_with_license(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method with license filter."""
        # Arrange
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = repos_payload

        # Act
        client = GithubOrgClient("example_org")
        result = client.public_repos(license="apache-2.0")

        # Assert
        self.assertEqual(result, apache2_repos)
        mock_get_json.assert_called_once_with("http://example.com/repos")


if __name__ == "__main__":
    unittest.main()
