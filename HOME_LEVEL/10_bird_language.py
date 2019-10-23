#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/bird-language/solve/
"""
import re
VOWELS = "aeiouy"

def translate(phrase):
    phrase = phrase.lower()
    words = phrase.split(' ')
    for word_index, ech_word in enumerate(words):
        for _index, _ in enumerate(ech_word):
            if _index:
                sub_phrase = ech_word[_index -1 :_index +1]
                if (len(sub_phrase) == 2) and  (sub_phrase[0] not in VOWELS) and  (sub_phrase[1] in VOWELS):
                    ech_word = ech_word.replace(sub_phrase, sub_phrase[0])
        words[word_index] = ech_word
    phrase = ' '.join(words)

    for ech_vwl in VOWELS:
        phrase = re.sub('%s{2,3}'%ech_vwl, ech_vwl, phrase)
    return phrase

if __name__ == '__main__':
    print("Example:")
    print(translate("aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    assert translate("aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa") == "abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba", "Large"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
