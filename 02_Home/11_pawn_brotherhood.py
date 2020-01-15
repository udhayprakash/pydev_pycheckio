#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/pawn-brotherhood/solve/
A pawn may capture an opponent's piece on a square diagonally 
in front of it on an adjacent file, by moving to that square.
"""


def is_pawn_safe(_pawn, _pawns):
    _row, _col = _pawn[0], _pawn[1]
    defending_pawns = []
    for _each_pwn in _pawns:
        if _pawn != _each_pwn and _row > _each_pwn[0]:
            prw, pcol = _each_pwn[0], _each_pwn[1]
            print(_pawn, _each_pwn)
            # if  and abs(_row - prw) == abs(_col - pcol):
            #     # print((_row, _col), '->', (prw, pcol), _row > prw, abs(_row- prw) == abs( _col - pcol))
            #     defending_pawns.append((prw, pcol))
    if defending_pawns:
        print((_row, _col), _pawn, '->', defending_pawns)
    return True if defending_pawns else False


def safe_pawns(pawns: set) -> int:
    count = 0
    for pawn in sorted(pawns, key=lambda x: x[0]):
        is_safe = is_pawn_safe(pawn, pawns)
        if is_safe:
            count += 1
    return count


# def is_pawn_safe(_row, _col, _pawns_indexes):
#     defending_pawns = []
#     for prw, pcol in _pawns_indexes:
#         if (_row, _col) != (prw, pcol) and _row > prw and abs(_row - prw) == abs(_col - pcol):
#             # print((_row, _col), '->', (prw, pcol), _row > prw, abs(_row- prw) == abs( _col - pcol))
#             defending_pawns.append((prw, pcol))
#     if defending_pawns:
#         print((_row, _col), '->', defending_pawns)
#     return True if defending_pawns else False
#
#
# def safe_pawns(pawns: set) -> int:
#     pawns_indexes = set()
#     for p in pawns:
#         row = int(p[1]) - 1
#         col = ord(p[0]) - 97
#         pawns_indexes.add((row, col))
#
#     count = 0
#     for row, col in sorted(pawns_indexes, key=lambda x: x[0]):
#         is_safe = is_pawn_safe(row, col, pawns_indexes)
#         if is_safe:
#             count += 1
#     return count


if __name__ == '__main__':
    print(safe_pawns({"a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"}))
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    # assert safe_pawns({"a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"}) == 0
    assert safe_pawns({"a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"}) == 0
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
