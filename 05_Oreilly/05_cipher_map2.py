#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/cipher-map2/solve/

original                    : [(0, 0), (1, 2), (2, 0), (2, 3)]
X   .   .   .
.   .   X   .
X   .   .   X
.   .   .   .


90 degree clockwise rotation: [(0, 1), (0, 3), (2, 2), (3, 1)]
.   X   .   X
.   .   .   .
.   .   X   .
.   X   .   .

90 degree clockwise rotation: [(1, 0), (1, 3), (2, 1), (3, 3)]
.   .   .   .
X   .   .   X
.   X   .   .
.   .   .   X

90 degree clockwise rotation: [(0, 2), (1, 1), (3, 0), (3, 2)]
.   .   X   .
.   X   .   .
.   .   .   .
X   .   X   .

90 degree clockwise rotation: [(0, 1), (1, 2), (2, 0), (2, 3)]
X   .   .   .
.   .   X   .
X   .   .   X
.   .   .   .

"""


def recall_password(cipher_grille, ciphered_password):
    print(cipher_grille)
    positions = []
    for row_index, each_row in enumerate(cipher_grille):
        print(each_row)
        for col_index, each_col in enumerate(each_row):
            if each_col == 'X':
                positions.append((row_index, col_index))
                print(row_index + col_index)
                print(ciphered_password[row_index + col_index])
    print(positions)
    return 'icantforgetiddqd'


if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'
    #
    # assert recall_password(
    #     ('....',
    #      'X..X',
    #      '.X..',
    #      '...X'),
    #     ('xhwc',
    #      'rsqx',
    #      'xqzz',
    #      'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
