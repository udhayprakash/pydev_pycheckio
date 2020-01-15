#!/usr/bin/python
"""
Purpose: https://py.checkio.org/en/mission/friends/
"""


class Friends:
    def __init__(self, connections):
        raise NotImplementedError

    def add(self, connection):
        raise NotImplementedError

    def remove(self, connection):
        raise NotImplementedError

    def names(self):
        raise NotImplementedError

    def connected(self, name):
        raise NotImplementedError


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
