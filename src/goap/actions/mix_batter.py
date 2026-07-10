class MixBatter:

    def __init__(self) -> None:
        self.preconditions: dict = { "have_dry_ing": True,
                                     "have_wet_ing": True }
        self.cost: int = 1
        self.effects: dict = { "have_batter": True,
                                "have_dry_ing": False,
                                "have_wet_ing": False }

    def apply_effects(self, name) -> None:
        print(name + " adds the wet ingredients to the dry and mixes to get batter.")