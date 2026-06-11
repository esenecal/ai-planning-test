# https://en.wikipedia.org/wiki/Dijkstra's_algorithm
# https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

# Used to find the shortest path in a weighted graph. A precursor to a*.

def dijkstra_distance(graph, root):

    # ensure that root is in the graph
    if root not in graph.keys():
        raise KeyError(f"Error: {root} not in graph")
    
    # find a way to implement this with a priority queue, possibly setting it up manually with dequeue

    unvisited = set()           # set of all univisted nodes
    distances = dict()          # distances of each node to root
    for i in graph.keys():
        unvisited.add(i)        # All nodes have not been visited
        distances[i] = float('inf')     # all nodes start with a distance of infinity
    distances[root] = 0         # replace the inf distance of root with 0
    print(unvisited)
    print(distances)

    # Repeat while we still have nodes to visit. If we do not, skip and return the distance list.
    while len(unvisited) != 0:
        
        # select node with lowest distance that has not been visited.
        node = unvisited.pop()      # the node that will contain selected node. we start with a random element in unvisited.
        unvisited.add(node)         # add it back so we don't miss it.    
        for n in unvisited:                             # iterate through the unvisited nodes.
            if (distances[n] < distances[node]):        # if the distance of n is greater than the current node, and node has not been visited 
                node = n                                # n becomes our new node selected node.

        # iterate through the nodes adjacent to node. Update their distances by adding their distance from node to node's total distance.
        for adjacent in graph[node]:        # adjacent is a tuple with (node_name, edge_length)
            # calculate distance 
            adj_dist = distances[node] + adjacent[1]
            if adj_dist < distances[adjacent[0]]:       # if the new distance is less than the current saved distance
                distances[adjacent[0]] = adj_dist
        
        # remove node from unvisited
        unvisited.remove(node)

    return distances