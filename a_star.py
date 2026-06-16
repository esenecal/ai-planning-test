# A* algorithm. Any heuristic system works; try the general distance dictionary from the bfs as the heuristic algorithm 
# https://en.wikipedia.org/wiki/A*_search_algorithm

import heapq

# graph: graph for traversal. root: starting node. goal: goal node. h: heuristic dictionary.
def a_star(graph, root, goal, h):
    return 0