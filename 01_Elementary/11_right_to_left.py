#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/right-to-left/solve/
"""


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return ','.join([word.replace('right', 'left') for word in phrases])


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
