#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator in utils."""

    def test_memoize(self):
        """Test that a_method is only called once when a_property is accessed multiple times."""
        
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Instantiate TestClass and call a_property twice
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)

            # Verify that a_method was only called once
            mock_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
