#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/stressful-subject/solve/
"""


def is_stressful(subj):
    """
        recognise stressful subject
    """
    if subj.isupper() or subj.endswith('!!!'):
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
