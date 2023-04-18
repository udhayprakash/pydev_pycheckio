def unruly(grid):
    return grid


if __name__ == '__main__':
    def grid2spec(grid):
        """To get the game id."""
        import re
        nb_rows, nb_cols = len(grid), len(grid[0])
        spec, length = [f'{nb_cols}x{nb_rows}:'], nb_rows * nb_cols
        for points, item in re.findall(r'(\.*)(B|W)', ''.join(grid)):
            length -= len(points) + 1
            char = chr(ord('a') + len(points))
            spec.append(char.upper() if item == 'B' else char)
        spec.append(chr(ord('a') + length))
        return ''.join(spec)


    def checker(grid, result):
        try:
            result = list(result)
        except TypeError:
            raise AssertionError('You must return an iterable/list/tuple.')
        assert all(isinstance(row, str) for row in result), \
            'Must return an iterable of strings.'
        nb_rows, nb_cols = len(grid), len(grid[0])
        assert len(result) == nb_rows and \
               all(len(row) == nb_cols for row in result), 'Wrong size.'
        forbidden_chars = ''.join(set.union(*map(set, result)) - set('WB.'))
        assert not forbidden_chars, \
            f'Only the chars "WB." are allowed, not {forbidden_chars!r}.'
        forbidden_changes = sum(c1 != c2 for r1, r2 in zip(grid, result)
                                for c1, c2 in zip(r1, r2) if c1 != '.')
        assert not forbidden_changes, \
            f'You changed {forbidden_changes} cells given at the start.'
        miss = sum(row.count('.') for row in result)
        if miss:
            print('You can look what is missing here:')
            print('https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/'
                  f'unruly.html#{grid2spec(result)}')
            print('You just need to open a new webpage with that url.')
        assert not miss, f'{miss} cells are still empty.'
        columns = map(''.join, zip(*result))
        for _type, lines in (('row', result), ('column', columns)):
            for n, line in enumerate(lines):
                Ws, Bs = map(line.count, 'WB')
                assert Ws == Bs, f'{Ws} W & {Bs} B in {_type} {n} {line!r}.'
                for item in 'WB':
                    assert item * 3 not in line, \
                        f'{item * 3} found in {_type} {n} {line!r}.'


    TESTS = (
        ('......',
         '..B...',
         'W.B.W.',
         '......',
         'W...W.',
         'WW..W.'),
        ('....WW.B',
         'W..B....',
         '.B...W..',
         'BW....W.',
         '........',
         '.WW.....',
         'W...BB.B',
         'W....B..'),
        ('B..........B',
         '..BB.B.W..B.',
         'B........B..',
         '....BW.W...W',
         '.W........W.',
         '.W...B.....B',
         '..B..BB...W.',
         'BW....B.....'),
    )

    for test_nb, grid in enumerate(TESTS, 1):
        result = unruly(grid)
        try:
            checker(grid, result)
        except AssertionError as error:
            print(f'You failed the test #{test_nb}:', error.args[0])
            print('Your result:', *result, sep='\n')
            break
    else:
        print('Well done! Click on "Check" for bigger tests.')
