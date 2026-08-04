class MixDryIng:
    
    preconditions: dict = { "oven_hot": True }
    cost: int = 1
    effects: dict = { "have_dry_ing": True }

    def apply_effects(self, name) -> None:
        print(name + " mixes the dry ingredients.")