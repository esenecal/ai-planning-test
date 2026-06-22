# A* algorithm. Any heuristic system works; try the general distance dictionary from the bfs as the heuristic algorithm 
# https://en.wikipedia.org/wiki/A*_search_algorithm

import heapq

# graph: graph for traversal. root: starting node. goal: goal node. h: heuristic dictionary.
# h is a dictionary detailing the heuristic values from the goal (how far a node is from goal)
def a_star(graph, root, goal, h):
    # ensure that root is in the graph
    if root not in graph.keys():
        raise KeyError(f"Error: {root} not in graph")
    
    # find a way to implement this with a priority queue, possibly setting it up manually with dequeue
    # saw example of using heapq (given by chat gpt) with the nodes and their distances given in tuples, as (distance, node). This is based off of that idae.

    unvisited = list()      # set of all univisted nodes
    distances = dict()      # distances of each node to root, with [distance, previous_node]
    for i in graph.keys():
        if i == root:                                   # if it is root, then set the distance to 0.
            unvisited.append((0, i))
            distances[i] = [0, None]
        else:
            unvisited.append((float('inf'), i))             # All nodes have not been visited
            distances[i] = [float('inf'), None]                     # all nodes start with a distance of infinity

    heapq.heapify(unvisited)        # convert unvisited into a min-value priority queue.

    node = (None, None)             # create a blank current node tuple
    # Repeat while we have not reached the goal node.
    while node[1] != goal:

        # distances tracks the actual distances of the nodes, while the values in unvisited are our estimates using our h value

        # select node with lowest distance that has not been visited.
        node = heapq.heappop(unvisited)     # pop the node with the lowest distance.
        node_name = node[1]                 # remember--unvisited is formatted (total_distance, node). graph is formatted (node_name, edge_length)
        if node_name

        # iterate through the nodes adjacent to node. Update their distances by adding their distance from node to node's total distance.
        for adjacent in graph[node_name]:        # adjacent is a tuple with (node_name, edge_length)

            adjacent_name = adjacent[0]
            
            # calculate distance 
            adj_dist = distances[node_name][0] + adjacent[1]
            if adj_dist < distances[adjacent_name][0]:                    # if the new distance is less than the current saved distance

                distances[adjacent_name][0] = adj_dist
                distances[adjacent_name][1] = node_name                     # set the previous node for adjacent to node_name. This means that moving from that node to it's previous node puts it along the simplest route. See the attached YouTube video
                                                                            # In other words, if the path along node_name is faster for adjacent_node than the path already saved (denoted by distances[n][1]), switch to this new path (thus, this new previous_node)

                estimated_distance = adj_dist + h[adjacent_name]        # the estimated distance from root to goal, through adjacent. This is pushed on the heap and used to prioritize paths with a potentially cheap path.

                # the a_star wikipedia pseudocode has a conditional where it only pushes onto the heap if the node is not already on it.
                # as this implementation tracks distances in the heap, not sure how effective this will be. But may bo good for edge cases.
                if (adj_dist, adjacent_name) not in unvisited:
                    heapq.heappush(unvisited, (estimated_distance, adjacent_name))    # example given just pushed things on the heap, creating duplicates. These are passed over.
                                                                            # we are placing the new distances for the each node in the heap.
    
    # construct the shortest path from root to goal, working backwards from goal. Similar to bfs_goal
    path = [goal]
    n = goal
    while distances[n][1] != None:      # The root will have a previous_node of None
        path.insert(0, distances[n][1]) # insert the node previous to n.
        n = distances[n][1]
    return path