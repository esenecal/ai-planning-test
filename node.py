class Node:
    """
    A node has a name. Adjacent nodes will be tracked by a dictionary. The dictionary will be used because the graph will not
    be changed during runtime.
    """
    def __init__(self, name: str) -> None:
        self.name = name