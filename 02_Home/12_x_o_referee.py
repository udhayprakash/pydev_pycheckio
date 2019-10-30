#!/usr/bin/python
"""
Purpose: https://py.checkio.org/en/mission/x-o-referee/solve/

"""
from typing import List

def checkio(game_result: List[str]) -> str:
    # row-wise check
    for ech_row in game_result:
        row_unique = ''.join(set(ech_row))
        if len(row_unique) == 1 and row_unique in ('O', 'X'):
            return row_unique

    # column-wise check
    for index, _ in enumerate(game_result):
        column_unique = ''.join({er[index] for er in game_result})
        if len(column_unique) == 1 and column_unique in ('O', 'X'):
            return column_unique

    # two principal diagonals check 
    first_diagonal = set()
    second_diagonal = set()
    for _index, ech_row in enumerate(game_result):
        first_diagonal.add(ech_row[_index])
        second_diagonal.add(ech_row[len(ech_row) - _index -1])

    first_diagonal_unique = ''.join(first_diagonal)
    if len(first_diagonal_unique) == 1 and first_diagonal_unique in ('O', 'X'):
            return first_diagonal_unique

    second_diagonal_unique = ''.join(second_diagonal)
    if len(second_diagonal_unique) == 1 and second_diagonal_unique in ('O', 'X'):
            return second_diagonal_unique
    
    # draw
    return 'D' 

if __name__ == '__main__':
    # print("Example:")
    print(checkio([ "O.X",
                    "XX.",
                    "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "OOO",
        "XOX",
        "XOX"]) == "O", "first row"
    assert checkio([
        "OXO",
        "XXX",
        "XOX"]) == "X", "second row"
    assert checkio([
        "OXO",
        "XXX",
        "XXX"]) == "X", "third row"
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "first column"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "second column"
    assert checkio([
        "O.X",
        "XOX",
        "XOX"]) == "X", "third column"
    assert checkio([
        "O.X",
        "XO.",
        "XOO"]) == "O", "first diagonal"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "second diagonal"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")