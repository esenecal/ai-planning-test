class HeatOven:

    def __init__(self) -> None:
        self.preconditions: dict = { "hungry": True }
        self.cost: int = 1
        self.effects: dict = { "oven_hot": True }

    def apply_effects(self) -> None:
        print("Bill turns on the oven to preheat.")