class Bake:

    def __init__(self) -> None:
        self.preconditions: dict = { "have_batter": True }
        self.cost: int = 1
        self.effects: dict = { "cake": True,
                              "oven_hot": False,
                              "have_batter": False,
                               }

    def apply_effects(self) -> None:
        print("Bill puts the batter into the oven to bake. He takes a cake out after 20 minutes.")