from src.goap.goal import Goal

def test_goal_expected_state():

    world_state = {
                    "a": 0, 
                    "b": 0, 
                    "c": 0
                   }
                   

    goal = Goal({"a": 1, "c": 2})

    assert True == goal.check_expected_state(world_state)

def test_goal_failed_expected_state():

    world_state = {
                    "a": 0, 
                    "b": 0, 
                    "c": 0
                   }
                   

    goal = Goal({"a": 1, "d": 2})

    assert False == goal.check_expected_state(world_state)