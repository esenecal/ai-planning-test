class Bake:

    preconditions: dict = { "have_batter": True }
    cost: int = 1
    effects: dict = { "cake": True, 
                     "oven_hot": False,
                     "have_batter": False,
                     }

    def apply_effects(self, name) -> None:
        print(name + " puts the batter into the oven to bake. He takes a cake out after 20 minutes.")