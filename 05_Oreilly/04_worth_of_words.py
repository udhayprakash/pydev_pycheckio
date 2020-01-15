#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/worth-of-words/solve/
"""
VALUES = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}


def worth_of_words(words):
    word_values = {}
    for word in words:
        count = 0
        for char in word:
            count += VALUES[char]
        word_values[word] = count

    return sorted(word_values.items(), key=lambda x: x[1])[-1][0]


def worth_of_words(words):
    return max(words, key=lambda x: sum(VALUES[letter] for letter in x))


if __name__ == '__main__':
    print("Example:")
    print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))

    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")
