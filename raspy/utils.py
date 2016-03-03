import hashlib


def get_md5_string(input_str):
    """
    Args:
        input_str:
    Returns: MD5 hash of the input_str
    """
    hashed_str = hashlib.md5()
    hashed_str.update(input_str)
    hashed_str = hashed_str.hexdigest()
    return hashed_str


