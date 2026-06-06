# Algorithm for a breadth-first search. Assuming unweighted graph.
# https://en.wikipedia.org/wiki/Breadth-first_search

from collections import deque       # for the use of queues. https://www.geeksforgeeks.org/python/queue-in-python/

def bfs_goal(graph, root, goal):    # find shortest path to goal.
    # verify the root is in the graph.
    if root not in graph.keys():
        return 0
    
    q = deque()                 # initialize queue
    visited = {root}            # add root to visited set
    q.append(root)              # add root to queue
    parent_nodes = {}           # create an empty dictionary with the keys of the graph.
    for key in graph.key():
        parent_nodes[key] = None
    # parent_nodes provides the parent of each node. "f": "a" means "a" is the parent of "f"

    while len(q) != 0:          # while our queue is not empty
        vertex = q.popleft()    # pop node on top of queue, name it vertex
        
        # check if we have reached the goal node
        if vertex == goal:
            output_path = deque([goal])         # add a the goal to a queue
                                                # output_path will provide the shortest path, root to goal.
            n = goal
            while parent_nodes[n] != None:      # iterate through parent_nodes, tracking from the goal to the root. Each node has only one parent.
                output_path.appendleft(parent_nodes[n])
                n = parent_nodes[n][0]
            return list(output_path)            # return output_path as a list
    
        # for each node connected to vertex
        for node in graph.get(vertex):
            if node not in visited:             # if this node is has not been visited...
                visited.add(node)               # mark it as visited
                parent_nodes[node] = vertex     # mark vertex as node's parent.
                q.append(node)                  # add node to the queue so we can iterate through its children later

# returns dictionary with distance from root to each node
def bfs_dist(graph, root):
    # verify root is in graph
    if root not in graph.keys():
        return 0
    
    q = deque()             # initialize queue
    visited = {root}        # add root to visited set
    q.append(root)          # add root to q
    d = {}                  # create empty dictionary with keys for each node
    for key in graph.keys():
        d[key] = 0          # distance is, by default, 0.
    
    i = 1                   # iterable for tracking distance
    while len(q) != 0:      # while our q is not empty:

        vertex = q.popleft()        # get node on top of q, name it vertex.

        # for each node connected to the vertex
        for node in graph.get(vertex):
            if node not in visited:     # if node has not been visited.
                visited.add(node)       # add node to visited
                d[node] = i             # ad distance from root to d
                q.append(node)          # add node to q
        i += 1
    return d