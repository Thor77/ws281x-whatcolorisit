from datetime import time

import pytest

from ws281x_whatcolorisit.whatcolorisit import (Color, current_color,
                                                hex_to_color)


@pytest.mark.parametrize('hex_str,expected', [
    ('220000', Color(34, 0, 0)), ('010000', Color(1, 0, 0)),
    ('223030', Color(34, 48, 48)), ('000010', Color(0, 0, 16)),
])
def test_hex_to_color(hex_str, expected):
    assert hex_to_color(hex_str) == expected


@pytest.mark.parametrize('input_time,expected', [
    (time(8), Color(8, 0, 0))
])
def test_current_color(input_time, expected):
    assert current_color(input_time) == expected
