from is_even import is_even
import unittest

class test_is_even(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_even(1))
        self.assertTrue(is_even(2))
