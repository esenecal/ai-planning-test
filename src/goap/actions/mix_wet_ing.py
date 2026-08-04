class MixWetIng:

    preconditions: dict = { "have_dry_ing": True }
    cost: int = 1
    effects: dict = { "have_wet_ing": True }

    def apply_effects(self, name) -> None:
        print(name + " mixes the wet ingredients.")