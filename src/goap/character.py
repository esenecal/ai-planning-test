import heapq
from src.goap.goal import Goal

class Character:

    def __init__(self, name: str, goals: list[tuple[int, Goal]] ) -> None:
        self.name = name
        self.goals = goals                      # simply for reference. helpful if we want the original priorities.
        self.goal_queue = goals                 # convert goals into a priority queue.
        heapq.heapify(self.goal_queue)

    # The example here: https://github.com/viniciusgerevini/godot-goap/blob/main/goap/agent.gd
    # seems to use the character class to make a plan. This makes sense--a plan is for a specific npc, after all.

    # This class will define a character and the handling of the planning. Unlike actions and goals, with 1 class per action/goal,
    # characters will be created as objects from this one class.

    # This assumes priorities do not change. Eventually, we will need to implement a dynamic system that changes priorities according
    # to external stimuli.

    # get highest priority goal, without priority
    def get_priority_goal(self) -> Goal:
        goal = heapq.heappop(self.goal_queue)
        return goal[1]
    
    # add a goal to the priority queue.
    def add_priority_goal(self, goal: tuple[int, Goal]) -> None:
        heapq.heappush(self.goal_queue, goal)

    # get the plan for the highest priority goal.
    def get_plan(self) -> None:
        
        return None
    
