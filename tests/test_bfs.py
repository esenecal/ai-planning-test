from bfs import bfs_dist, bfs_goal

import pytest

test_undirected_graph_1 = {
    "a": ["b", "d"],
    "b": ["a", "c", "d", "e", "f"], 
    "c": ["b", "e"], 
    "d": ["a", "b", "e"], 
    "e": ["b", "c", "d", "f"], 
    "f": ["b", "e"]
}

test_weighted_graph_1 = {       # each has a tuple showing the weight between the nodes
    "a": [("b", 2), ("d", 1)],
    "b": [("a", 2), ("c", 3), ("d", 2), ("e", 4), ("f", 5)], 
    "c": [("b", 3), ("e", 1)], 
    "d": [("a", 1), ("b", 2), ("e", 4)], 
    "e": [("b", 4), ("c", 1), ("d", 3), ("f", 2)], 
    "f": [("b", 5), ("e", 2)]
}

def test_bfs_goal_ug1_a_c():
    # given and when
    path = bfs_goal(test_undirected_graph_1, "a", "c")

    # then
    assert path == ["a", "b", "c"]

def test_bfs_goal_ug1_a():
    # given and when
    path = bfs_goal(test_undirected_graph_1, "a", "a")

    # then
    assert path == ["a"]

def test_bfs_goal_ug1_a_d():
    # given and when
    path = bfs_goal(test_undirected_graph_1, "a", "d")

    # then
    assert path == ["a", "d"]

def test_bfs_goal_ug1_a_f():
    # given and when
    path = bfs_goal(test_undirected_graph_1, "a", "f")

    # then
    assert path == ["a", "b", "f"]


def test_bfs_goal_ug1_no_root():
    # given

    # when
    with pytest.raises(KeyError) as exception:
        bfs_goal(test_undirected_graph_1, "g", "f")

    # then
    
    assert (
        'Error: g not in graph'
        in str(exception.value)
        # or == in str(exception.value) but due to a bug, keyerror wraps the string in more quotes. so in is more graceful.
    )

def test_bfs_goal_ug1_no_goal():
    # given

    # when
    with pytest.raises(KeyError) as exception:
        bfs_goal(test_undirected_graph_1, "a", "g")

    # then
    
    assert (
        'Error: g not in graph'
        in str(exception.value)
        # or == in str(exception.value) but due to a bug, keyerror wraps the string in more quotes. so in is more graceful.
    )

def test_bfs_dist_ug1_a():
    distance = bfs_dist(test_undirected_graph_1, "a")
    assert distance == {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 1,
        "e": 2,
        "f": 2
    }

def test_bfs_dist_ug1_f():
    distance = bfs_dist(test_undirected_graph_1, "f")
    assert distance == {
        "a": 2,
        "b": 1,
        "c": 2,
        "d": 2,
        "e": 1,
        "f": 0
    }

def test_bfs_dist_ug1_no_root():
    with pytest.raises(KeyError) as exception:
        bfs_dist(test_undirected_graph_1, "z")

    assert(
        'Error: z not in graph'
        in str(exception.value)
    )