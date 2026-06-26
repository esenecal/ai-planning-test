from a_star import a_star
from bfs import bfs_dist_weighted
from convert_graph import directed_to_bidirectional

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

    result = a_star(test_weighted_graph_1, "a", "f", h)

    assert result == ["a", "d", "e", "f"]

def test_a_star_wg1_ac():

    h = bfs_dist_weighted(test_weighted_graph_1, "c")

    assert h == {
        "a": 2,
        "b": 1,
        "c": 0,
        "d": 2,
        "e": 1,
        "f": 2,
    }

    result = a_star(test_weighted_graph_1, "a", "c", h)

    assert result == ["a", "b", "c"]

def test_a_star_wd1_ac():

    # the bfs assumes bidirectional graphs. To get the accurate bfs, we must make it bidirectional.
    graph = directed_to_bidirectional(test_weighted_directed_1)

    h = bfs_dist_weighted(graph, "c")

    assert h == {
        "a": 1,
        "b": 1,
        "c": 0,
        "d": 1,
    }

    result = a_star(test_weighted_directed_1, "a", "c", h)

    assert result == ["a", "b", "c"]