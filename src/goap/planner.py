
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
def build_plan(root):

    desired_state: dict = dict()

