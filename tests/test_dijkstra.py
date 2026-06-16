from dijkstra import dijkstra_distance, dijkstra_goal

import pytest

test_weighted_graph_1 = {       # each has a tuple showing the weight between the nodes
    "a": [("b", 2), ("d", 1)],
    "b": [("a", 2), ("c", 3), ("d", 2), ("e", 4), ("f", 5)], 
    "c": [("b", 3), ("e", 1)], 
    "d": [("a", 1), ("b", 2), ("e", 3)], 
    "e": [("b", 4), ("c", 1), ("d", 3), ("f", 2)], 
    "f": [("b", 5), ("e", 2)]
}

def test_dijkstra_wg1():

    a = dijkstra_distance(test_weighted_graph_1, "a")

    goal = {
        "a": 0,
        "b": 2,
        "c": 5,
        "d": 1,
        "e": 4,
        "f": 6,
    }

    assert a == goal

def test_dijkstra_wg1_af():

    path = dijkstra_goal(test_weighted_graph_1, "a", "f")

    goal = ["a", "d", "e", "f"]

    assert path == goal
