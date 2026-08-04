class Eat:

    preconditions: dict = { "cake": True }
    cost: int = 1
    effects: dict = { "cake": False,
                   "hungry": False }

    def apply_effects(self, name) -> None:
        print(name + " eats the cake.")