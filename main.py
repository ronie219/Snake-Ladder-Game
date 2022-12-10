from Game import Game
from Player import Player

if __name__ == '__main__':
    players = [
        Player("Abhishek Biswas"),
        Player("Rohit Singh")
    ]
    game = Game(players)
    game.start_game()