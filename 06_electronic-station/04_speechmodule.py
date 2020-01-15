#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/speechmodule/solve/

Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.

How it is used: This concept may be useful for the speech synthesis software or automatic reports systems. This system can also be used when writing a chatbot by assigning words or phrases numerical values and having a system retrieve responses based on those values.

Precondition: 0 < number < 1000
"""
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


# 20  30 40 50 60 70 80 90 100
# 0    1  2  3  4  5  6 7   8

def checkio(number):
    if not 0 < number < 1000:
        return "Value out of scope"

    num_str = ''
    if 1000 > number >= 100:
        hundreds = FIRST_TEN[(number // 100) - 1] + " " + HUNDRED
        number %= 100
        num_str += hundreds

    if 100 > number >= 20:
        print(number,  (number // 100) - 1)
        tens = OTHER_TENS[(number // 100) - 1]
        number %= 10
        num_str += ' ' + tens

    if 20 > number >= 10:
        tens = SECOND_TEN[number - 10]
        number %= 10
        num_str += ' ' + tens

    if 10 > number >= 1:
        ones = FIRST_TEN[number - 1]
        num_str += ' ' + ones

    # if 1 <= number < 10:
    #     return FIRST_TEN[number - 1]
    # elif 10 <= number < 20:
    #     return SECOND_TEN[number - 10]
    # elif 20 <= number < 100:
    #     ones_pos = (number % 10) - 1
    #     tens_pos = ((number - ones_pos + 1) // 10) - 2
    #     return OTHER_TENS[tens_pos] + ('' if ones_pos == -1 else ' ' + FIRST_TEN[ones_pos])
    # elif 100 <= number < 1000:
    #     hundreds = FIRST_TEN[number // 100 - 1] + " " + HUNDRED
    #     # ones_pos = (number % 10) - 1
    #     # tens_pos = ((number - ones_pos + 1) // 10) - 2
    #     print(number, hundreds)
    #     # return OTHER_TENS[tens_pos] + ('' if ones_pos == -1 else ' ' + FIRST_TEN[ones_pos])
    return num_str


if __name__ == '__main__':
    for i in range(994, 985, -1):
        print("%3d" % i, checkio(i))
    # print(checkio(999))
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(4) == 'four', "1st example"
    # assert checkio(133) == 'one hundred thirty three', "2nd example"
    # assert checkio(12) == 'twelve', "3rd example"
    # assert checkio(101) == 'one hundred one', "4th example"
    # assert checkio(212) == 'two hundred twelve', "5th example"
    # assert checkio(40) == 'forty', "6th example"
    # assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    # print('Done! Go and Check it!')
