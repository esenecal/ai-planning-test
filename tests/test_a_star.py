from a_star import a_star
from bfs import bfs_dist_weighted

import pytest

test_weighted_graph_1 = {       # each has a tuple showing the weight between the nodes
    "a": [("b", 2), ("d", 1)],
    "b": [("a", 2), ("c", 3), ("d", 2), ("e", 4), ("f", 5)], 
    "c": [("b", 3), ("e", 1)], 
    "d": [("a", 1), ("b", 2), ("e", 3)], 
    "e": [("b", 4), ("c", 1), ("d", 3), ("f", 2)], 
    "f": [("b", 5), ("e", 2)]
}

test_weighted_directed_1 = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2), ("d", 2)],
    "c": [],
    "d": [("a", 2), ("c", 1)]
}

def test_a_star_wg1_af():

    h = bfs_dist_weighted(test_weighted_graph_1, "f")

    assert h == {
        "a": 2,
        "b": 1,
        "c": 2,
        "d": 2,
        "e": 1,
        "f": 0
    }

    