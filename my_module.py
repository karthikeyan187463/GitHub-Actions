import unittest

class TestPlayerCredit(unittest.TestCase):

    def test_initial_credit(self):
        """Test that player's initial credit is set correctly."""
        player = Player("John")
        self.assertEqual(player.credit, 0)  # Default credit should be 0

    def test_add_credit(self):
        """Test that adding credit increases player's credit."""
        player = Player("John", 100)
        player.add_credit(50)
        self.assertEqual(player.credit, 150)  # Credit should be 100 + 50 = 150

    def test_subtract_credit(self):
        """Test that subtracting credit decreases player's credit."""
        player = Player("John", 100)
        player.subtract_credit(30)
        self.assertEqual(player.credit, 70)  # Credit should be 100 - 30 = 70

    def test_subtract_credit_not_enough(self):
        """Test that trying to subtract more credit than available raises an error."""
        player = Player("John", 50)
        with self.assertRaises(ValueError):
            player.subtract_credit(100)  # Should raise ValueError because credit is less than 100

if __name__ == "__main__":
    unittest.main()
