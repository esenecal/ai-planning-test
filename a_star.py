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
    prev = dict()               # dictionary showing a node's previous node.
    dist_to_node = {key: float('inf') for key in graph.keys()}  # dictionary tracking known costs of root to a node
    dist_to_node[root] = 0              # set the distance to the root node as 0

    est_path = {key: float('inf') for key in graph.keys()}  # dictionary tracking best guess of distance from root to goal, through n.
    est_path[root] = h[root]                                # in other words, est_path[n] = dist_to_node[n] (distance from root to n) + h(n) (estimated distance from n to goal)

    open_set = [(est_path[root], root)]     # tracks nodes for expansion. We also add a node's estimated path value; in other cases with custom objects, each node can track their own distance and be updated on the fly.
    heapq.heapify(open_set)                 # convert open_set to a priority queue. It will prioritize nodes with a low estimated path (est_path)
    in_open_set = {root}           # tracks which nodes are in the priority queue, as each instance of a node will have a different distance.

    while len(open_set) != 0:   # while open_set is not empty
        current_node = heapq.heappop(open_set)      # get the node with the lowest est_path distance
        current_node_name = current_node[1]
        in_open_set.remove(current_node_name)       # update the queue tracker
        
        # if current_node is the goal node, then construct the shortest path and return it
        if current_node_name == goal:
            # reconstruct the path
            return prev
        
        # iterate through the adjacent nodes to current_node, calculating their estimated distance and updating as needed.
        for adjacent_node in graph[current_node_name]:
            adjacent_node_name = adjacent_node[0]
            adjacent_node_weight = adjacent_node[1]    # weight from current_node to adjacent
            # estimated distance to adjacent is distance from root to current_node + edge from current_node to adjacent
            estimated_dist_to_adjacent = dist_to_node[current_node_name] + adjacent_node_weight
            
            # if the current estimated distance to adjacent is less than the known distance to adjacent
            if estimated_dist_to_adjacent < dist_to_node[adjacent_node_name]:

                prev[adjacent_node_name] = current_node_name                                                # note the previous node to adjacent (which is current)
                dist_to_node[adjacent_node_name] = estimated_dist_to_adjacent                               # note that the distance from root to adjacent_node is the estimated_dist_to_adjacent
                est_path[adjacent_node_name] = estimated_dist_to_adjacent + h[adjacent_node_name]           # therefore, the estimated path from root to goal through adjacent_node is the estimated_dist_to_adjacent + the heuristic value estimate of adjacent_node to goal

                if adjacent_node_name not in in_open_set:
                    heapq.heappush(open_set, (est_path[adjacent_node_name], adjacent_node_name))    # add the adjacent node and it's estimated path to the heap.
                    in_open_set.add(adjacent_node_name)                                             # update the queue tracker
        
    return "error"
                



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