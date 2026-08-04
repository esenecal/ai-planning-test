class MixBatter:

    preconditions: dict = { "have_dry_ing": True,
                               "have_wet_ing": True }
    cost: int = 1
    effects: dict = { "have_batter": True,
                                "have_dry_ing": False,
                                "have_wet_ing": False }

    def apply_effects(self, name) -> None:
        print(name + " adds the wet ingredients to the dry and mixes to get batter.")