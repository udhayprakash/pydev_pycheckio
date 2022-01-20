#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/long-repeat/solve/
"""


def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    highest_count = 0
    _count = 0
    for _index, _ in enumerate(line):
        if _index and line[_index - 1] != line[_index]:
            _count = 1
        else:
            _count += 1

        if highest_count < _count:
            highest_count = _count
    return highest_count


if __name__ == '__main__':
    print(long_repeat('abababaab'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
