#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/even-last/solve/
"""


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    result = 0
    if not array:
        return result
    for index, ele in enumerate(array):
        if index % 2 == 0:
            result += ele
    result *= array[-1]
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
