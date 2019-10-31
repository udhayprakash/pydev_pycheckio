#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/flatten-list/solve/
"""


def flat_list(array, result=None):
    if result is None:
        result = []
    # if not array:
    #     return []
    for ele in array:
        if isinstance(ele, list):
            flat_list(ele, result)
        else:
            result.append(ele)
    return result


if __name__ == '__main__':
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
    flat_list([1, [2, 2, 2], 4])
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
