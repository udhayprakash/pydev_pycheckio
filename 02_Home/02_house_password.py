#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/house-password/solve/
"""


def checkio(data: str) -> bool:
    import re
    print()
    if (len(data) >= 10
            and re.search('[0-9]', data)
            and re.search('[a-z]', data)
            and re.search('[A-Z]', data)
    ):
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
