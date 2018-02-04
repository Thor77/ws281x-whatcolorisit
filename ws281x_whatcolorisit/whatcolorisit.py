import struct
from collections import namedtuple

Color = namedtuple('Color', ['r', 'g', 'b'])


def hex_to_color(hex_str):
    '''
    Convert hex string to color-tuple

    :param hex_str: Hex string
    :type hex_str: str

    :return: hex_str as color-tuple
    :rtype: ws281x_whatcolorisit.whatcolorisit.Color
    '''
    # first "encode" hex_str into bytes-obj
    try:
        # Python 2
        decoded_hex_str = hex_str.decode('hex')
    except AttributeError:
        # Python 3
        decoded_hex_str = bytes.fromhex(hex_str)
    # unpack bytes-obj into tuple (B = unsigned char)
    return Color(*struct.unpack('BBB', decoded_hex_str))


def current_color(current_time):
    '''
    Calculate color for `current_time`

    :param current_time: Current time
    :type current_time: datetime.time

    :return: Color for `current_time`
    :rtype: Color
    '''
    # build hex string from current_time
    hex_str = ('{:02d}' * 3).format(
        current_time.hour, current_time.minute, current_time.second
    )
    # convert hex string to color
    return hex_to_color(hex_str)
