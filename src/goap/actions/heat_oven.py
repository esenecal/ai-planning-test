class HeatOven:

    preconditions: dict = { "hungry": True }
    cost: int = 1
    effects: dict = { "oven_hot": True }

    def apply_effects(self, name) -> None:
        print(name + " turns on the oven to preheat.")