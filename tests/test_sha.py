# test_sha.py

import unittest
from src.sha import calculate_sha256

class TestCalculateSHA256(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate_sha256(''), 'e3b0c44298fc1c149afbf4c8996fb924')

    def test_short_string(self):
        self.assertEqual(calculate_sha256('hello'), '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')

    def test_long_string(self):
        long_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        self.assertEqual(calculate_sha256(long_string), '98d5a27c07109c88f014bb74f71b31e4a4717f82d5e7f88a4ab2')

if __name__ == '__main__':
    unittest.main()

