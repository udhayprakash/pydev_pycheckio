#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/popular-words/solve/
"""


def popular_words(text: str, words: list) -> dict:
    counts = {w: 0 for w in words}
    for word in text.split():
        word = word.strip().lower()
        if word in words:
            counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
