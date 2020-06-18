import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthly(self):
        """Eat should have a positive message for eating healthy food."""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
            )
    def test_eat_unhealthly(self):
        """Eat should indicate you've given up for eating healthy food."""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
            )
    def test_eat_healthly_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """Short naps should be refreshing."""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
            )
    def test_long_nap(self):
        """Long naps should be discouraging."""
        self.assertEqual(
            nap(3),
            "Ugh I overslept, I didn't mean to nap for 3 hours! "
            )

    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)
        #self.assertFalse(is_funny("tim"), "Tim should not be funnny")

    def test_is_funny_anyone_else(self):
        """Anyone else but Tim should be funny"""
        self.assertTrue(is_funny("blue"), "Blue should be funny")
        self.assertTrue(is_funny("ttammy"), "Tammy should be funny")
        self.assertTrue(is_funny("sven"), "Sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))



if __name__ == "__main__":
    unittest.main()


#To be able to see the "documentation" for each test case, run with the -v option, example: python tests.py -v
