#!/usr/bin/python
"""
Purpose: https://py.checkio.org/en/mission/find-friends/solve/
"""
from pprint import pprint


class Node:
    def __init__(self, node_name, related_node):
        self.node_name = node_name
        self.related_nodes = [related_node]

    def add_related_node(self, related_node):
        self.related_nodes.append(related_node)

    def get_related_nodes(self):
        return self.related_nodes

    def __str__(self):
        return str(self.related_nodes)

    __repr__ = __str__


def check_connection(network, first, second):
    all_nodes = {}
    for each_relation in network:
        n1, n2 = each_relation.split('-')

        if n1 in all_nodes:
            all_nodes[n1].add_related_node(n2)
        else:
            all_nodes[n1] = Node(n1, n2)

        if n2 in all_nodes:
            all_nodes[n2].add_related_node(n1)
        else:
            all_nodes[n2] = Node(n2, n1)

    pprint(all_nodes)
    if (first in all_nodes) and (second in all_nodes):
        return check_relation(all_nodes, first, second)
    else:
        return False


def check_relation(_all_nodes, _first, _second):
    _related_nodes = _all_nodes[_first].get_related_nodes()
    print('checking', _first, _second, _related_nodes)
    if _second in _related_nodes:
        return True
    for each_rel_node in _related_nodes:
        if each_rel_node == _second:
            return True
        return check_relation(_all_nodes, each_rel_node, _second)
    return False


if __name__ == '__main__':
    # check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3")
    # print(check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #                         "scout3-scout1", "scout1-scout4",
    #                         "scout4-sscout", "sscout-super",), "scout2", "scout3"))
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
