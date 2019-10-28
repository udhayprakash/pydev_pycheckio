#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/fizz-buzz/solve/
"""


def checkio(number: int) -> str:
    """
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5;
    :param number:
    :return:
    """
    result = str(number)
    if number % 3 == 0:
        result = 'Fizz'
    if number % 5 == 0:
        result = 'Buzz'
    if number % 3 == 0 and number % 5 == 0:
        result = 'Fizz Buzz'
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
