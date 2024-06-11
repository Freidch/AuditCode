import hashlib

def calculate_sha256(input_string):
    """
    Calculate SHA-256 hash of input_string.

    Args:
        input_string (str): Input string to be hashed.

    Returns:
        str: SHA-256 hash of the input string.
    """
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash

