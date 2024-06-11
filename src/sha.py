import hashlib

def generate_sha256_hash(input_string):
    """
    Generates a SHA256 hash for the given input string.

    :param input_string: The string to hash.
    :return: The SHA256 hash of the input string.
    """
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash
