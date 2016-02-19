import hashlib

def get_md5_string(input_str):
    """
    Args:
        input_str:
    Returns: MD5 hash of the input_str
    """
    hash = hashlib.md5()
    hash = hash.update(input_str)
    hash = hash.hexdigest()
    return hash