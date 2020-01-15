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
    else:
        subj = subj.lower()
        unique_str = ''
        for _index, each_ch in enumerate(subj):
            if _index and (subj[_index - 1] == each_ch or each_ch in ('.', '!', '-')):
                continue
            unique_str += each_ch

        for red_word in ("help", "asap", "urgent"):
            if red_word in unique_str:
                return True
    return False


if __name__ == '__main__':
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I neeed help") == True, "help"
    assert is_stressful("I neeed HeLp") == True, "HeLp"
    assert is_stressful("I neeed HeLp") == True, "HeLp"
    assert is_stressful("I neeed H!E!L!P!") == True, "H!E!L!P!"
    assert is_stressful("I neeed H-E-L-P") == True, "H-E-L-P"
    assert is_stressful("I neeed HHHEEEEEEEEELLP") == True, "HHHEEEEEEEEELLP"
    assert is_stressful("We need you A.S.A.P.!!") == True, "A.S.A.P.!!"
    # print('Done! Go Check it!')
