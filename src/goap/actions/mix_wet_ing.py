class MixWetIng:

    def __init__(self) -> None:
        self.preconditions: dict = { "have_dry_ing": True }
        self.cost: int = 1
        self.effects: dict = { "have_wet_ing": True }

    def apply_effects(self) -> None:
        print("Chell mixes the wet ingredients in a bowl.")