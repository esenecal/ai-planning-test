A possible heuristic algorithm works via a bfs algorithm. It constructs "layers" and associates each node in a dictionary with a numerical "layer" from the goal node. We know our goal node, so it can make this layer fairly easily and should provide a basic structure for subgoals. Then, we can calculate according to a* using this dictionary to provide the heuristic value. 

## Using venv
https://docs.python.org/3/library/venv.html

## testing
https://docs.pytest.org/en/stable/getting-started.html#get-started


## STRIPS
STRIPS is made of an initial state, goal state, and a set of oeprators (actions) with preconditions and postconditions (requirements to be performed and effects on the world state).

An instance can be defined as $\langle P, O, I, G\rangle$ where:
- $P$: set of conditions or propositional variables (which is an input variable that can be either true or false - https://en.wikipedia.org/wiki/Propositional_variable)
- $O$: set of operators, each defined as $\langle \alpha, \beta, \gamma, \delta\rangle$:
    - $\alpha$: conditions that must be true for an operator to be executed (preconditions)
    - $\beta$: conditions that must be false for an operator to be executed (preconditions)
    - $\gamma$: conditions that will be made true by execution (postconditions)
    - $\delta$: conditions that will be made false by execution (postconditions)
- $I$: initial state as a set of conditions that are considered true; all conditions not included in the set are assumed false.
- $G$: goal state represented as $\langle N, M\rangle$, where 
    - $N$: conditions that must be true
    - $M$: conditions that must be false

https://en.wikipedia.org/wiki/Stanford_Research_Institute_Problem_Solver#, 2026/6/21

Note that the goal state does not necessarily consider all conditions, only some that are true and some that are false. This is because a *goal state is not necessarily reliant on the entirety of the world condition; it can be predicated on only certain conditions being true or false.*

Also note that there may be a possibility to use propositional statements in an operator's preconditions. For example, the use of $A\cup B$ may be possible. 

I believe that a directed graph (with weights later given) can be created by considering which operator, when executed, fulfills conditions that are required by another operator. It is possible that multiple operators not necessarily chained together may create effects that fulfill another operator's preconditions; this is a more complex situation that may need to be accounted for. This may be addressed by starting goal-first (see below).

So, each member of the operator class will contain each of these four ($\langle \alpha, \beta, \gamma, \delta\rangle$) sets of conditions. When they are executed, the world state will be changed according to this data. 

The planning algorithm works by two ways: we can either start at the goal state and move back via preconditions until we reach preconditions that are fulfilled by the world's state, or start at the initial state, search for an operator in which the world state fulfills its preconditions, and then search along the operators until we reach one that fulfills the goal state. The STRIPS paper (https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf) seems to suggest the former by, to my understanding, stating the preconditions required of the operator fulfilling the goal state would become a subgoal (page 5), which makes sense; searching for a start then for the goal is less efficient. 

In the event that an operator does not fulfill a goal/subgoal state (which, again, may be the preconditions for anotehr operator), the algorithm should select an operator that fulfills the most--for example, that fulfills only part of the conditions required. Then the search can continue, using this new world state to find more operators that work.

Here is an example of a STRIPS instance:

$$
\langle
    (P, Q),
    (
        \langle (P), (Q), (Q), ()\rangle,
        \langle (P, Q), (), (), (P)\rangle,
        \langle (Q), (P), (P), ()\rangle,
        \langle (), (P, Q), (P), ()\rangle
    ),
    (P),
    \langle (Q), (P)\rangle
\rangle
$$

To break it down:
- $P = (P, Q)$ where $P$ and $Q$ are true/false conditions.
- $O = (\langle (P), (Q), (Q), ()\rangle, \langle (P, Q), (), (), (P)\rangle, \langle (Q), (P), (P), ()\rangle, \langle (), (P, Q), (P), ()\rangle)$ where:
    - $O_1 = \langle (P), (Q), (Q), ()\rangle$:
        - $preconditions(P = T, Q = F)$,  $postconditions(Q = T)$
    - $O_2 = \langle (P, Q), (), (), (P)\rangle$:
        - $preconditions(P = T, Q = T)$,  $postconditions(P = F)$
    - $O_3 = \langle (Q), (P), (P), ()\rangle$:
        - $preconditions(Q = T, P = F)$,  $postconditions(P = T)$
    - $O_4 = \langle (), (P, Q), (P), ()\rangle$:
        - $preconditions(P = F, Q = F)$,  $postconditions(P = T)$
- $I = (P)$; $P = T$, $Q = F$ is the initial world state
- $\langle (Q), (P)\rangle$; $Q = T$, $P = F$ is the goal

## A*

The A* search algorithm is similar to Dijkstra's with the difference being that it uses a heuristic function $h$ to approximate the most efficient path, where $h$ is a problem-specific estimate of a node's distance to the goal (https://en.wikipedia.org/wiki/A*_search_algorithm)

Our code, based on the pseudocode found at the Wikipedia article above, uses the heuristic function h. A dictionary `est_path_dist` tracks the sum of the distance from root to a node and h(n), the estimated distance from the node to the goal. This estimated path distance is then placed in the priority queue, meaning nodes with a low estimated path distance will be prioritized for selection.

The current implementation does not use a closed set. Some implementations I have seen do. From what I have gathered, a closed list is needed if the heuristic function is consistent. The Wikipedia article providing the pseudocode our implementation was based off of explains that the specific pseudocode allows for a heuristic function that is not consistent by adding nodes back to open_set if a more efficient path through it appears (https://stackoverflow.com/questions/45577114/a-star-algorithm-open-and-closed-lists). It allows for a heuristic function that is "admissible but not consistent" (https://en.wikipedia.org/wiki/A*_search_algorithm).  

### Admissible Heuristic Functions

An admissible heuristic function if the estimated path distance to the goal is not higher than the lowest possible path. It never overestimates the cost to the goal and acts as a lower bound (https://en.wikipedia.org/wiki/Admissible_heuristic).

So, $h(n) <= h*(n)$, for all nodes $n$. $h*(n)$ is the true cost of the minimal cost path from n to goal. $h(n)$ is the estimated cost from n to goal (https://pages.cs.wisc.edu/~dyer/cs540/notes/search2.html).

Our heuristic function simply assumes that the weight of each edge is 1; thus, $h(n)$ for a given node will always be the number of edges between $n$ and goal. Because, in our model, the weight of an edge must be a whole number greater than 0, this provides a minumum estimate. Thus, I believe our heuristic function is admissible. 

### Consistent Heuristic Functions

A consistent or monotone heuristic function is one where the "estimate is always less than or equal to the estimated distance from any neighbouring vertext to the goal, plus the cost of reaching that neighbor" (https://en.wikipedia.org/wiki/Consistent_heuristic).

This article provides an equation:

$h(N) \leq c(N,P) + h(P)$ and
$h(G) = 0$

- $h$: consistent heuristic function
- $N$: any node in the graph
- $P$: any descendant of $N$
- $G$: goal node
- $c(N,P)$: cost of reachng node $P$ from $N$ (in our case, the weight of the edge between the two)

This means that the estimated distance from N to G must be less from the estimated distance from P to G, plus the distance from N to P (which, as neighbors, is their edge weight). The estimate of the distance from G to G must be 0. 

