#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/count-consecutive-summers/solve/

Positive integers can be expressed as sums of "consecutive positive integers" in various ways.
For example, 42 can be expressed as such a sum in four different ways:
        (a) 3+4+5+6+7+8+9,
        (b) 9+10+11+12,
        (c) 13+14+15 and
        (d) 42.
As the last solution (d) shows, any positive integer can always be trivially expressed as a
singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.

Precondition: Input is always a positive integer.

========================
The sum of the integers from 1 to n is n(n+1)/2.
The sum of the integers from k to k+n is then
    k+(k+1)+⋯+(k+n)
        =(n+1)k+1+⋯+n
        =(n+1)k+n(n+1)/2
        =(n+1)(2k+n)/2.

If N is sum of k consecutive numbers, then
following must be true.

N = [(n+k)(n+k+1) - n(n+1)] / 2

OR

2 * N = [(n+k)(n+k+1) - n(n+1)]

2 * N = (last - first) * (last + first + 1)
"""


def get_consecutive_sums(last, first):
    cons_sums = [first]
    first += 1
    for x in range(first, last + 1):
        cons_sums.append(x)
    return cons_sums


def count_consecutive_summers(num):
    no_of_possibilities = 1  # num * 1
    for last in range(1, num):
        for first in range(0, last):
            if 2 * num == (last - first) * (last + first + 1):
                print(num, get_consecutive_sums(last, first + 1))
                no_of_possibilities += 1
    return no_of_possibilities


if __name__ == '__main__':
    print("Example:")
    # print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(10) == 2
    assert count_consecutive_summers(24) == 2
    assert count_consecutive_summers(8) == 1
    assert count_consecutive_summers(1) == 1
    # print("Coding complete? Click 'Check' to earn cool rewards!")
