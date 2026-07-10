class Eat:

    def __init__(self) -> None:
        self.preconditions: dict = { "cake": True }
        self.cost: int = 1
        self.effects: dict = { "cake": False,
                                "hungry": False }

    def apply_effects(self, name) -> None:
        print(name + " eats the cake.")