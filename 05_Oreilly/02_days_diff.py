#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/days-diff/solve/
"""
from datetime import datetime


def days_diff(a, b):
    dt_a = datetime.strptime('%04d %02d %02d' % tuple(a), '%Y %m %d')
    dt_b = datetime.strptime('%04d %02d %02d' % tuple(b), '%Y %m %d')
    return abs(dt_a - dt_b).days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff([1, 1, 1], [9999, 12, 31]) == 3652058
    print("Coding complete? Click 'Check' to earn cool rewards!")
