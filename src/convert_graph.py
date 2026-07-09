# take a weighted, directed graph and convert it to a weighted, bidirectional graph. 

import copy

test_weighted_directed_1 = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2), ("d", 2)],
    "c": [],
    "d": [("a", 2), ("c", 1)]
}

def directed_to_bidirectional(graph):
    bidirectional_graph = copy.deepcopy(graph)      # creates a deepcopy of graph. If not, cahnging bidirectonal_graph may change graph.
    # this is not necessarily an issue, as once we check a node it is good, but it can lead to duplicates and thus take more time.

    # iterate through the graph.
    for node, neighbors in graph.items():
        for edge in neighbors:
            neighbor_name = edge[0]
            edge_weight = edge[1]
            bidirectional_graph[neighbor_name].append((node, edge_weight))
    # for each node adjacent to node n, make the 
    return bidirectional_graph

print(directed_to_bidirectional(test_weighted_directed_1))