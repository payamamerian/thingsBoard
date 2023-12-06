def hexToInt(hex_value):
    return int(hex_value, 16)
import struct
def hex_to_double(hex_str):  
    # Convert hex string to bytes
    bytes_str = bytes.fromhex(hex_str)
    # Unpack byte string to a double
    return struct.unpack('!d', bytes_str)[0]


#thingsboard_gateway/extensions/socket#