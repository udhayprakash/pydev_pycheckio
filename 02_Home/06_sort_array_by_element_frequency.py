#!/usr/bin/python
"""
Purpose: https://py.checkio.org/en/mission/sort-array-by-element-frequency/
"""
from collections import Counter


def frequency_sort(items):
    ele_counts = []
    for _index, ele in enumerate(items):
        pair = (ele, items.count(ele))
        if ele_counts.count(pair) == 0:
            ele_counts.append(pair)
    result = sorted(ele_counts, key=lambda x: -x[1])
    final = []
    for ech in result:
        final.extend([ech[0]] * ech[1])
    return final


def frequency_sort(items):
    return list(Counter(dict(Counter(items).most_common())).elements())


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    print("Coding complete? Click 'Check' to earn cool rewards!")
