class Action:

    def __init__(self, preconditions: dict = dict(), cost: int = 1, effects: dict = dict(), text: str = "null") -> None:
        self.preconditions = preconditions
        self.cost = cost
        self.effects = effects
        self.text = text

    def blank_init(self) -> None:
        self.preconditions: dict = {}
        self.cost: int = 1
        self.effects: dict = {}

    def apply_effects(self, name):    # display message when Action is executed.
        print(self.text)