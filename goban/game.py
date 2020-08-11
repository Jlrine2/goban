from goban.board import Board
from goban.player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def update_point(self, point):
        self.board.update_point(point, self.player)
