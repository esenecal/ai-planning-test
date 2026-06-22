# A* algorithm. Any heuristic system works; try the general distance dictionary from the bfs as the heuristic algorithm 
# https://en.wikipedia.org/wiki/A*_search_algorithm, circa 2026/6/22

import heapq

# graph: graph for traversal. root: starting node. goal: goal node. h: heuristic dictionary.
# h is a dictionary detailing the heuristic values from the goal (how far a node is from goal)
def a_star(graph, root, goal, h):
    # ensure that root is in the graph
    if root not in graph.keys():
        raise KeyError(f"Error: {root} not in graph")
    
    # Rewriting the algorithm based off of the pseudocode in the wikipedia article, as the implementation using my dijkstra's algorithm was inefficient.
    open_set = [root]           # tracks nodes for expansion. 
    heapq.heapify(open_set)     # convert open_set to a priority queue.

    prev = dict()               # dictionary showing a node's previous node.
    dist_to_node = {key: float('inf') for key in graph.keys()}  # dictionary tracking known costs of root to a node
    dist_to_node[root] = 0              # set the distance to the root node as 0

    est_dist_to_goal = {key: float('inf') for key in graph.keys()}  # dictionary tracking best guess of distance from root to goal, through n.
    est_dist_to_goal[root] = h[root]                                # in other words, est_dist_to_goal[n] = dist_to_node[n] (distance from root to n) + h(n) (estimated distance from n to goal)

    while len(open_set) != 0:   # while open_set is not empty




test_weighted_graph_1 = {       # each has a tuple showing the weight between the nodes
    "a": [("b", 2), ("d", 1)],
    "b": [("a", 2), ("c", 3), ("d", 2), ("e", 4), ("f", 5)], 
    "c": [("b", 3), ("e", 1)], 
    "d": [("a", 1), ("b", 2), ("e", 3)], 
    "e": [("b", 4), ("c", 1), ("d", 3), ("f", 2)], 
    "f": [("b", 5), ("e", 2)]
}

h = {
        "a": 2,
        "b": 1,
        "c": 2,
        "d": 2,
        "e": 1,
        "f": 0
    }

print(a_star(test_weighted_graph_1, "a", "f", h))