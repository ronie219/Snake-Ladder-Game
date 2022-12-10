class Jump:
    """
    it will keep the position of the snake and ladder both. ie if start<end it will be ladder
    if start > end it will act like a snake.
    """

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
