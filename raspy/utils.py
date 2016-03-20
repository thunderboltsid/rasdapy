import hashlib
import re


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


def get_type_structure_from_string(input_str):
    primary_regex = "set<marray<(char|float|int), .*>>"
    struct_regex = (
        "set<marray<struct{((char|ushort|short|ulong|long|float|double)\s+.*,)*\s+((char|ushort|short|ulong|long|float|double) .*)}, .*>>"
    )
    m = re.match(primary_regex, input_str)
    result = {
        'base_type': 'marray',
    }

    if m is None:
        m = re.match(struct_regex, input_str)

        if m is None:
            # Invalid input_str, return None
            return None

        # Result of m.groups() is a tuple alike
        # ('int foo,', 'int', 'char bar', 'char')
        sub_type = m.groups()[1::2]
        result['type'] = 'struct'
        result['sub_type'] = sub_type
    else:
        primary_type = m.group(1)
        result['type'] = primary_type

    return result
