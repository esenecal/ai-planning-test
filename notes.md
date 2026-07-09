# Notes

This project is an exercise to create a goal oriented planning system based on the system used by Monolith Productions in the game F.E.A.R. After hearing about the notable AI systems used in this game, I found [a paper](https://www.gamedevs.org/uploads/three-states-plan-ai-of-fear.pdf) by Jeff Orkin written on their AI planning system, called GOAP (Goal-Oriented Action Planning), which was based on STRIPS, the STanford Research Institute Problem Solver (the paper written by Richard Fikes and Nils Nilsson on it can be found [here](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf)).

From what I have gathered from these papers, STRIPS works on a defined world state, a goal condition of the world state, and operators that provide actions to alter the world state (Fikes and Nilsson, p.1-4). If the world state is provided, the goal state known, and proper actions available, the AI system can select actions that will properly fulfill the goal state (Orkin seems to use the term "action" in place of "operator", so I'll do the same).

The AI system must determine which actions are best to fulfill the goal state; if needed, it can create subgoals to work on to fulfill the goal state (Fikes and Nilsson, p.5).

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

A possible heuristic algorithm works via a bfs algorithm. It constructs "layers" and associates each node in a dictionary with a numerical "layer" from the goal node. We know our goal node, so it can make this layer fairly easily and should provide a basic structure for subgoals. Then, we can calculate according to a* using this dictionary to provide the heuristic value. 

## Using venv
https://docs.python.org/3/library/venv.html

## testing
https://docs.pytest.org/en/stable/getting-started.html#get-started

## GOAP

### GDC 2006 Paper

This is what I have been able to gather on the Goal-Oriented Action Planning System and how it differs from STRIPS, from the GDC 2006 paper written by Jeff Orkins (https://www.gamedevs.org/uploads/three-states-plan-ai-of-fear.pdf)

The STRIPS planning process, simply speaking, works with goals and actions, where goals describe a desired world state and actions are the means to modify that state. Actions rely on preconditions to be executed and have effects that alter the world state. Depending on a goal, a sequence of actions is planned to fulfill that goal. Effects contain a delete list and an add list. When an action is executed, the delete list removes items/negates them from the world state, while the add list adds.

For implementation, each AI character has a set of goals that it is responsible for fulfilling. It seems that each goal has a semblence of priority--that is, the AI will do something, but external stimuli (the appearance of an enemy, for example) may change the goal (from 'patrol' to 'attack', for example). Each NPC then has an Action Set describing various actions that can be taken. 

The GOAP System used in F.E.A.R. makes several alterations. The first is that it assigns a cost per action to each action, then uses A* to search through the actions to find a plan. In other words, if world states were nodes and actions were edges, I understand that we are know assigning a weight to each edge rather than keeping a weight of 1. This allows for prioritization of certain actions; if higher-priority (low-cost) actions are unattainable (the world state does not meet the preconditions), another action with a higher cost but valid preconditions will be used. 

GOAP also removes the add/delete lists from actions. Rather, both preconditions and effects are represented in a world-state array. This means that you can easily see which actions have certain preconditions met by other actions' effects. I am not sure what they mean, as the wording seems a little vague; I believe it means rather than using add/delete lists to delete, then add knowledge to the world state, the preconditions and effects are described in separate arrays that simply display the required world state. In other words, the effects do not specify to delete and add something, but rather, to simply shift the world state to this new state. I am not sure, however. It is unclear if the entire world state is represented in these array, but it doesn't seem so (see next paragraph).

Finally, GOAP uses procedural preconditions and effects. Preconditions use checks to ensure they are met, but only when they are needed; this is to avoid representing everything in the actions' world state arrays. Each action has the precondition world state variables array and a check function, which makes a check to ensure that this function is viable depending on the world state. If it is, then the action can be executed. This allows us to only check a precondition when needed, in cases when constantly checking a precondition would be inefficient. Procedural effects are used to apply the changes in world state to the game, to avoid an instantaneous effect. 

So, this is what I have gathered from how this system would be implemented:
- AI planning can be represented as a graph where nodes are the states and edges are the actions. 
- Each action contains three attributes:
    - An array of preconditions
    - A cost (weight)
    - An array of effects.
- Each action contains two functions/methods:
    - A precondition check (if needed)
    - A effect function to apply the change and make it smoother.

### Vinicius Gerevini Godot GOAP

I found this video explanation and accompanying Github repository demonstrating GOAP in the Godot game engine. It was very helpful.

- https://www.youtube.com/watch?v=LhnlNKWh7oc
- https://github.com/viniciusgerevini/godot-goap 

In the video, Gerevini explains that goals are prioritized, with the highest priority goal being planned for. Plans are created by working back from the goal, using the requirements of the goal to find any action that fulfills it. If that action has its own set of preconditions, the planner then finds another action to fulfill that one. This continues until an action is reached in which all the world states are fulfilled (which, I believe, would mean you reach an action that has its precondition fulfilled by the current world state). The planner would also find various other plans, and selects the most optimal plan based on the lowest cost. The optimal plan is executed until it is completed (or otherwise invalidated) or another goal is prioritized.

Given his example, it appears that specific goals are prioritized depending on the world state; the lack of a fire prioritizes the goal of building a fire, the existence of hunger prioritizes eating, etc.

I took a look at the source code for his demo to see an example of an implementation, located at the GitHub repository above. After reviewing the `goap` folder, this is what I've found.

- Actions: his actions do sort of contain this precondition check as `is_valid`. They also contain a precondition set, an action set, and an effect function.
- Goals: his goals contained a priority and a desired world state. If a goal has dynamic priority, it appears the implementation for this is contained within the goal object.
- His action planner builds a graph based on a goal retrieved (I assume from an agent). It builds the graph on each execution, to account for any added actions. His yardstick for determining if an action should be used is determining if it can fulfill one condition in the desired world state. It also adds any preconditions for an action to the desired state. In other words, as we work back from the goal, it appears we are continually adding preconditions to the world state; each precondition can be satisfied by another action, and so our preconditions are added and fulfilled until we reach a point where they are all fulfilled. This means we found our starting action.
- Each agent keeps track of their goals and current working goal, as well as the current plan they are executing.
- I couldn't discern the search algorithm used in my brief look. Haiku 4.5 told me that there is a DFS in there, but I don't know if that's right. 

On `action_planner.gd`:
`_build_plans`:
- The comments state that each node of the graph has a desired state. Remember: nodes are states, actions are edges.
- _build_plans runs recursively. It takes a step, which is a dictionary containing an action (goal), state (desired state), and children. 
- When _build_plans is run, it saves the step state (desired state) and saves it in a variable. It checks if the step state is empty, indicating that this branch has found a solution.
- It then iterates through an array of actions (which appears to be all actions). For each action it:
    - checks if the action is valid (a validation check, see below)
    - checks if the action satisfies at least one condition of the desired state. If it does, remove this condition from our desired state. It has been fulfilled.
    - If at least one condition is satisfied, the preconditions of this action are set (or added?) to the new desired state (remember, we are working backwards). The function is then recursively called.
    - In effect, we are working backwards from the goal, checking if an action satisfies what we want. If it does, we save it and add the preconditions to our desired state, effectively making those preconditions part of our goal now. Now, when we search for another action, we find one that fulfills these new states. 
- Some of these--and this is a personal note here--aspects of the algorithm are likely not set in stone. For example, the specific search algorithm he uses and how he tracks states are probably not necessary. I could use a different algorithm if needed. Likewise, the recursive implementation is likely not necessary. If I want to hard-code the map, that may be possible and would lend itself to a different solution. What is most impactful to me from this is the example of iterating through the graph with a desired state, using preconditions to search for actions.

I'm very grateful for Gerenvini's example; it gave me a good look on how GOAP can actually work in practice, which is very helpful giving me some direction for my implementation.

### AI and Games YouTube Video

https://www.youtube.com/watch?v=PaOLBOuyswI&t=685s

Some notes from this video:
- There are various actions described in the code of F.E.A.R. Each has its own class, and are assigned to relative agents.
- The game performs plan validations to ensure that, if the world state changes while a plan is being made/executed, the plan or goal changes to match.
    - A fresh plan is validated by the system by running a simulation of the plan on the current world state, ensuring that all goes correctly.
    - A Replan Required function checks if the current plan be changed, continuously. A goal can override this function.
    - Each action is evaluated in execution, ensuring the preconditions and effects can be met. When the check is complete, the action is executed.
- The plans are typically 1-2 actions long--very short. There are a lot of actions, but a lot of goals too.