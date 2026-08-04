
# import the goals and actions.
import goals 
from actions import *
import copy

# The planner.

# starting world state
world_state: dict = {
    "oven_hot": False,
    "have_wet_ing": False,
    "have_dry_ing": False,
    "have_batter": False,
    "cake": False,
    "hungry": True
}

actions = {
    Bake,
    Eat,
    HeatOven,
    MixBatter,  
    MixDryIng,
    MixWetIng
}


# iterate through the actions to find a path until the desired state matches the world state.
# the desired state is determined by the goal.
# as the search, we will use dijkstra's algorithm.
# speed is not the issue right now; we also need to determine a way to find a reasonable heuristic value.
# Vinicius Gerevini's code made multiple routes and found the most efficient one; we won't do that here (yet).
def build_plan(goal):                   
    goal_state = goal.expected_state    # the expected state that we want to reach
    plan = list()

    # check if goal_state is already fulfilled. if so, terminate.

    # set the desired state to be the expected state.
    desired_state = copy.deepcopy(goal.expected_state)  # copying over the expected state

    # start at the desired_state.

    # search all possible actions; find one that fulfills part of the desired_state.
    action = get_possible_action(desired_state)

    # set this as 

def get_possible_action(desired_state):
    for action in actions:  # see if there is any overlap between the desired state and action's effects. if so, select it. Haiku 4.5 helped me out with the set intersection.
        if set(action.effects.items()) & set(desired_state):
            return action