class Goal:

    def __init__(self, expected_state: dict = dict()) -> None:
        self.expected_state = expected_state

    # checks that the expected state contains only items within the world state.
    def check_expected_state(self, world_state: dict) -> bool:
        if len(self.expected_state) == 0:
            return False                        # if expected state is empty, return false.
        for key in self.expected_state.keys():
            if key not in world_state.keys():
                return False                    # return False if any key is not in the world state.
        return True                             # return true if all keys are in the world state.