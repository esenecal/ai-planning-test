import heapq
from src.goap.goal import Goal

class Character:

    def __init__(self, name: str, goals: list[tuple[int, Goal]] ) -> None:
        self.name = name
        self.goals = goals                      # simply for reference.
        self.goal_queue = heapq.heapify(goals)  # convert goals into a priority queue.
