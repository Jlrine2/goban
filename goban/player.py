from random import randrange

from goban.point import Point


class Player:
    def __init__(self):
        pass

    def take_turn(self):
        x = randrange(1, 19)
        y = randrange(1, 19)
        return Point(x, y)
