from typing import List

from Board import Board
from Cell import Cell
from Dice import Dice
from Player import Player
from collections import deque


class Game:
    """
    this is the facade design pattern in which we give whole responsibility to Game class to design different object
    """

    def __init__(self, players: List[Player]):
        self.board = Board()
        self.dice = Dice(2)
        self.player_queue = deque()
        self.player_queue.extend(players)
        self.winner = None

    def start_game(self) -> None:
        """
        start game will responsible to play the game until we found a winner.
        :return: None
        """
        while self.winner is None:
            player = self.get_player()
            dice_count = self.dice.roll_dice()
            new_position = player.position + dice_count
            if new_position == len(self.board.board) - 1:
                print(f"There Winner is {player.name}")
                self.winner = player
            elif new_position < len(self.board.board) - 1:
                board_position = self.board.board[new_position]
                self.print_statement(player, board_position)
                if board_position.jump:
                    player.position = board_position.jump.end
                else:
                    player.position = board_position.position

    def get_player(self) -> Player:
        """
        get the player information for which we have our current turn
        :return: Player object
        """
        player = self.player_queue.popleft()
        self.player_queue.append(player)
        return player

    @staticmethod
    def print_statement(player: Player, position: Cell) -> None:
        """
        static class which will responsible for printing the player and its new position.
        :param player: Player info
        :param position: board information at that position.
        :return: None
        """
        if position.jump is None:
            print(f'{player.name} new position will be {position.position}')
        elif position.jump.start < position.jump.end:
            print(f'{player.name} has get ladder and new position will be {position.jump.end}')
        else:
            print(f'{player.name} has bitten by snake and new position will be {position.jump.end}')
