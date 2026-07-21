
# import the goals and actions.
import goals
import actions

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



# iterate through the actions to find a path until the desired state matches the world state.
# the desired state is determined by the goal.
# as the search, we will use an implementation of a*, though the h value will be 0, effectively making it dijkstra's algorithm.
# speed is not the issue right now; we also need to determine a way to find a reasonable heuristic value.
def build_plan(root):

    desired_state: dict = dict()

