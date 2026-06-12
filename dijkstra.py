# https://en.wikipedia.org/wiki/Dijkstra's_algorithm
# https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

# Used to find the shortest path in a weighted graph. A precursor to a*.
import heapq

def dijkstra_distance(graph, root):

    # ensure that root is in the graph
    if root not in graph.keys():
        raise KeyError(f"Error: {root} not in graph")
    
    # find a way to implement this with a priority queue, possibly setting it up manually with dequeue
    # saw example of using heapq (given by chat gpt) with the nodes and their distances given in tuples, as (distance, node). This is based off of that idae.

    unvisited = list()           # set of all univisted nodes
    distances = dict()          # distances of each node to root
    for i in graph.keys():
        if i == root:                                   # if it is root, then set the distance to 0.
            unvisited.append((0, i))
            distances[i] = 0
        else:
            unvisited.append((float('inf'), i))             # All nodes have not been visited
            distances[i] = float('inf')                     # all nodes start with a distance of infinity
    
    heapq.heapify(unvisited)        # convert unvisited into a min-value priority queue.
    
    print(unvisited)
    print(distances)

    # Repeat while we still have nodes to visit. If we do not, skip and return the distance list.
    while len(unvisited) != 0:
        
        # select node with lowest distance that has not been visited.
        node = heapq.heappop(unvisited)     # pop the node with the lowest distance.
        node_name = node[1]                 # remember--unvisited is formatted (total_distance, node). graph is formatted (node_name, edge_length)

        # iterate through the nodes adjacent to node. Update their distances by adding their distance from node to node's total distance.
        for adjacent in graph[node_name]:        # adjacent is a tuple with (node_name, edge_length)
            # calculate distance 
            adj_dist = distances[node_name] + adjacent[1]
            if adj_dist < distances[adjacent[0]]:       # if the new distance is less than the current saved distance
                distances[adjacent[0]] = adj_dist
                heapq.heappush(unvisited, (adj_dist, node_name))        # example given just pushed things on the heap, creating duplicates. These are passed over.
        
        # remove node from unvisited
        # unvisited.remove(node)

    return distances