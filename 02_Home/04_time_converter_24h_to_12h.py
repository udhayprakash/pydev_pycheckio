#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/time-converter-24h-to-12h/solve/
"""


def time_converter(time):
    hours, minutes = map(int, time.split(':'))
    if hours == 0:
        return f'{12}:{minutes:02} a.m.'
    elif hours == 12:
        return f'{hours}:{minutes:02} p.m.'
    elif hours > 12:
        hours = hours - 12
        return f'{hours}:{minutes:02} p.m.'
    return f'{hours}:{minutes:02} a.m.'


if __name__ == '__main__':
    # print("Example:")
    print(time_converter('12:30'))
    print(time_converter('09:00'))
    print(time_converter('23:15'))
    print(time_converter('00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
