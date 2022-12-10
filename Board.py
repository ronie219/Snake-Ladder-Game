from Cell import Cell
from random import randint

from Jump import Jump


class Board:
    """
    Board class which will keep all the information of each position.
    """

    def __init__(self, dimension: int = 10, snake: int = 5, ladder: int = 5):
        self.board = [Cell(idx) for idx in range(dimension * dimension)]
        self.initialize_snake(dimension, snake)
        self.initialize_ladder(dimension, ladder)

    def initialize_snake(self, dimension: int, snake_count: int) -> None:
        """
        it will initialize the snake into the board.
        :param dimension: dimension of the board
        :param snake_count: number snake is present in our board.
        :return: None
        """
        while snake_count > 0:
            start = randint(1, (dimension * dimension) - 1)
            end = randint(1, start)
            if self.board[start].jump is None:
                self.board[start].jump = Jump(start, end)
                snake_count -= 1

    def initialize_ladder(self, dimension: int, ladder_count: int) -> None:
        """
        it will initialize the ladder into the board.
        :param dimension: dimension of the board
        :param ladder_count: number snake is present in our board.
        :return:
        """
        while ladder_count > 0:
            start = randint(1, (dimension * dimension) - 1)
            end = randint(start, (dimension * dimension) - 1)
            if self.board[start].jump is None:
                self.board[start].jump = Jump(start, end)
                ladder_count -= 1
