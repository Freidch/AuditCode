import unittest

from your_module import calculate_sha256  # Importez la fonction à tester depuis votre module

class TestCalculateSHA256(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate_sha256(''), 'e3b0c44298fc1c149afbf4c8996fb924\
            27ae41e4649b934ca495991b7852b855')

    def test_short_string(self):
        self.assertEqual(calculate_sha256('hello'), '2cf24dba5fb0a30e26e83b2\
            7a4fd26d90dbc8f0d6e4158e6')

    def test_long_string(self):
        long_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing \
            elit. Nulla varius ultricies lectus a gravida.'
        self.assertEqual(calculate_sha256(long_string), '98d5a27c07109c88f0\
            14bb74f71b31e4a4717f82d5e7f88a4ab2')

if __name__ == '__main__':
    unittest.main()

