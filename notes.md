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

I believe that a directed graph (with weights later given) can be created by considering which operator, when executed, fulfills conditions that are required by another operator. It is possible that multiple operators not necessarily chained together may create effects that fulfill another operator's preconditions; this is a more complex situation that may need to be accounted for. 

So, each member of the operator class will contain each of these four ($\langle \alpha, \beta, \gamma, \delta\rangle$) sets of conditions. When they are executed, the world state will be changed according to this data. 

The planning algorithm works by two ways: we can either start at the goal state and move back via preconditions until we reach preconditions that are fulfilled by the world's state, or start at the initial state, search for an operator in which the world state fulfills its preconditions, and then search along the operators until we reach one that fulfills the goal state. The STRIPS paper (https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf) seems to suggest the former by, to my understanding, stating the preconditions required of the operator fulfilling the goal state would become a subgoal (page 5), which makes sense; searching for a start then for the goal is less efficient.