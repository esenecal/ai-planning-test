# GOAP Implementation

This details the structure I will use for my GOAP system. I am using Jeff Orkin's paper and Vinicius Gerevini's demo (see [notes.md](/notes.md)) as a launching off point, but will be implementing my own system as I see fit.

## Classes:
- `Goal`
    - Attributes:
        - `expected_state`: Dictionary. Expected state of the world (not exclusive--it only states whatever variables it is checking)
- `Action`
    - Attributes:
        - `preconditions`: Dictionary. Required state of the world to be executed
        - `cost`: integer. Cost of the action, determined by the developer.
        - `effects`: Dictionary. Changes made to the state of the world.
    - Methods:
        - `apply_effect`: details the changes made.
    - A precondition check will not be implemented in the action class itself. Checking preconditions will be done in the planner.
- `Character`
    - Attributes:
        - `goals`: set. all goals assigned to that character.
        - `goal_queue`: priority queue implemented with heapq. Contains tuples of (priority (int), goal).
        - `name`: everyone needs a name.
    - Methods:
        - `get_goal`: return the highest priority goal.
- `Planner`

## world_state

`world_state` will be a dictionary detailing the entire state of the world. It will be mutable, but items will not be added or removed, only changed.

Changes by effects to world state will be done via a method outside of `Action` by returning the `effects` dictionary and altering the world state. We will use the `update` function.

have character use a priority queue for goals. This means we will have to assign priority within the agent's class, using a tuple or something.

The highest priority goal is taken care of, then popped from the queue. If world state ever changes 