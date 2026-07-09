class MixDryIng:

    def __init__(self) -> None:
        self.preconditions: dict = { "oven_hot": True }
        self.cost: int = 1
        self.effects: dict = { "have_dry_ing": True }

    def apply_effects(self) -> None:
        print("Chell mixes the dry ingredients.")