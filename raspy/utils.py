import hashlib
import re
import struct


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
    primary_regex = "set\s+<marray\s+<(char|ushort|short|ulong|long|float|double),\s+.*>>"
    struct_regex = (
        "set\s+<marray\s+<struct{((char|ushort|short|ulong|long|float|double)\s+.*,)*\s+((char|ushort|short|ulong|long|float|double)\s+.*)},\s+.*>>"
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

    if result is None:
        raise Exception("Failed to retrieve type structure from string")

    return result


def convert_data_from_bin(dtype, data):
    if dtype == "char":
        result = struct.unpack("B", data)
    elif dtype == "ushort":
        result = struct.unpack("H", data)
    elif dtype == "short":
        result = struct.unpack("h", data)
    elif dtype == "ulong":
        result = struct.unpack("L", data)
    elif dtype == "long":
        result = struct.unpack("l", data)
    elif dtype == "float":
        result = struct.unpack("f", data)
    elif dtype == "double":
        result = struct.unpack("d", data)
    else:
        raise Exception("Unknown Data type provided")
    return result[0]


def convert_data_stream_from_bin(dtype, data, array_len, cell_len):
    arr = []
    for i in xrange(0, array_len, cell_len):
        arr.append(convert_data_from_bin(dtype, data[i]))
    return arr
