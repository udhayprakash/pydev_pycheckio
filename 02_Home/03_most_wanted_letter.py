#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/most-wanted-letter/solve/
"""


def checkio(text: str) -> str:
    counts = {}
    for ech_chr in text.lower():
        if ech_chr.isalpha():
            counts[ech_chr] = counts.get(ech_chr, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1])
    max_count = sorted_counts[-1][1]
    return sorted(key for key, val in sorted_counts if val == max_count)[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
