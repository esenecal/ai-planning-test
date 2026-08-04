# to treat these all as the same type "Action", Haiku 4.5 recommended I create a base class; it provided an example, showing the first four lines of Action, Bake (without the specific preconditions), and a few more.
class Action:
    preconditions: dict
    cost: int
    effects: dict

    @staticmethod
    def apply_effects(name: str) -> None:
        print()

class Bake(Action):

    preconditions: dict = { "have_batter": True }
    cost: int = 1
    effects: dict = { "cake": True, 
                     "oven_hot": False,
                     "have_batter": False,
                     }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " puts the batter into the oven to bake. He takes a cake out after 20 minutes.")

class Eat(Action):

    preconditions: dict = { "cake": True }
    cost: int = 1
    effects: dict = { "cake": False,
                   "hungry": False }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " eats the cake.")

class HeatOven(Action):

    preconditions: dict = { "hungry": True }
    cost: int = 1
    effects: dict = { "oven_hot": True }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " turns on the oven to preheat.")

class MixBatter(Action):

    preconditions: dict = { "have_dry_ing": True,
                               "have_wet_ing": True }
    cost: int = 1
    effects: dict = { "have_batter": True,
                                "have_dry_ing": False,
                                "have_wet_ing": False }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " adds the wet ingredients to the dry and mixes to get batter.")

class MixDryIng(Action):
    
    preconditions: dict = { "oven_hot": True }
    cost: int = 1
    effects: dict = { "have_dry_ing": True }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " mixes the dry ingredients.")

class MixWetIng(Action):

    preconditions: dict = { "have_dry_ing": True }
    cost: int = 1
    effects: dict = { "have_wet_ing": True }

    @staticmethod
    def apply_effects(name) -> None:
        print(name + " mixes the wet ingredients.")