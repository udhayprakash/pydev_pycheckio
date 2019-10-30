#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/correct-sentence/solve/
"""


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    return text[0].upper() + text[1:].rstrip('.') + '.'


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
