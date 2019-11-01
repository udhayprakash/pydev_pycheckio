#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/create-intervals/solve/
"""


def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    result = []
    temp_list = []
    for num in sorted(data):
        if len(temp_list) == 0:
            temp_list.append(num)
        else:
            if temp_list[-1] + 1 == num:
                temp_list.append(num)
            else:
                result.append((temp_list[0], temp_list[-1]))
                temp_list = [num]
    if temp_list:
        result.append((temp_list[0], temp_list[-1]))
    return result


if __name__ == '__main__':
    print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
    print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}))
    # assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    # assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    # print('Almost done! The only thing left to do is to Check it!')
