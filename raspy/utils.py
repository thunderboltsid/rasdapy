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
    primary_regex = "set\s*<marray\s*<(char|ushort|short|ulong|long|float|double),\s*.*>>"
    struct_regex = (
        "set\s*<marray\s*<struct\s*{((char|ushort|short|ulong|long|float|double)\s*.*,)*\s*((char|ushort|short|ulong|long|float|double)\s*.*)},\s*.*>>"
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
        temp = m.groups()[2].split(" ")[:-1]
        types = temp[0::2]
        names = temp[1::2]

        sub_type = {"types": types, "names": names}

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
        result = struct.unpack("B"*len(data), data)
    elif dtype == "ushort":
        result = struct.unpack("H"*len(data), data)
    elif dtype == "short":
        result = struct.unpack("h"*len(data), data)
    elif dtype == "ulong":
        result = struct.unpack("L"*len(data), data)
    elif dtype == "long":
        result = struct.unpack("l"*len(data), data)
    elif dtype == "float":
        result = struct.unpack("f"*len(data), data)
    elif dtype == "double":
        result = struct.unpack("d"*len(data), data)
    else:
        raise Exception("Unknown Data type provided")
    return result[0]


def get_size_from_data_type(dtype):
    if dtype == "char":
        result = 1
    elif dtype == "ushort":
        result = 2
    elif dtype == "short":
        result = 2
    elif dtype == "ulong":
        result = 4
    elif dtype == "long":
        result = 4
    elif dtype == "float":
        result = 4
    elif dtype == "double":
        result = 8
    else:
        raise Exception("Unknown Data type provided")
    return result


def convert_data_stream_from_bin(dtype, data, array_len, cell_len):
    arr = []
    if dtype["type"] == "struct":
        for i in xrange(0, array_len, cell_len):
            cell_counter = 0
            temp = []
            for idx, dt in enumerate(dtype["sub_type"]["types"]):
                dtsize = get_size_from_data_type(dt)
                temp.append(convert_data_from_bin(dt, data[i + cell_counter:i + cell_counter + dtsize]))
                cell_counter += dtsize
            arr.append(temp)
    else:
        for i in xrange(0, array_len, cell_len):
            arr.append(convert_data_from_bin(dtype["type"], data[i]))
    return arr
