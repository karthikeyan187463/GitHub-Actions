"""
This module contains unit tests for the randomizer function.
The randomizer function generates a random integer within a specified range.
"""

import unittest
from my_module import randomizer  # Replace 'my_module' with the actual module name

class TestRandomizer(unittest.TestCase):
    """
    Unit test class for testing the randomizer function.
    """

    def test_output_within_range(self):
        """Test that randomizer output is within the specified range."""
        min_value, max_value = 1, 10
        for _ in range(100):  # Test multiple calls for consistency
            result = randomizer(min_value, max_value)
            self.assertGreaterEqual(result, min_value)
            self.assertLessEqual(result, max_value)

    def test_edge_case_same_min_max(self):
        """Test that randomizer returns the same number when min_value == max_value."""
        min_value = max_value = 5
        result = randomizer(min_value, max_value)
        self.assertEqual(result, 5)  # Should always return the single possible value

    def test_output_type(self):
        """Test that randomizer returns an integer."""
        min_value, max_value = 1, 10
        result = randomizer(min_value, max_value)
        self.assertIsInstance(result, int)

    def test_randomness(self):
        """Test that multiple calls produce varied results."""
        min_value, max_value = 1, 10
        results = {randomizer(min_value, max_value) for _ in range(100)}
        # Expect varied results over 100 calls (could be less than 10 unique due to randomness)
        self.assertGreater(len(results), 1)

if __name__ == '__main__':
    unittest.main()
