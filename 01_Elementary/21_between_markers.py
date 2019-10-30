#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/between-markers/solve/
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin_index = text.find(begin)
    end_index = text.find(end)
    if end_index == -1:
        end_index = len(text)
    if begin_index > end_index:
        return ''
    return text.split(end)[0].split(begin)[-1]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
