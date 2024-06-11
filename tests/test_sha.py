import unittest
from sha import generatesha256hash

class TestHashUtils(unittest.TestCase):

    def testgenerate_sha256_hash(self):
        # Test with a known input and its expected hash output
        input_string = "hello world"
        expected_hash = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b8567e7282e50d5ff"
        self.assertEqual(generate_sha256_hash(input_string), expected_hash)

        # Test with an empty string
        input_string = ""
        expected_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        self.assertEqual(generate_sha256_hash(input_string), expected_hash)

        # Test with another known input
        input_string = "OpenAI"
        expected_hash = "6e340b9cffb37a989ca544e6bb780a2c32e592fcddbb4fa2dd31b5f7b01f5f58"
        self.assertEqual(generate_sha256_hash(input_string), expected_hash)

if __name == '__main':
    unittest.main()
