from Jump import Jump


class Cell:

    """
    it will keep the information of the cell along with the snake and the ladder information.
    """

    def __init__(self, position: int, jump: Jump = None):
        self.position = position
        self.jump = jump
