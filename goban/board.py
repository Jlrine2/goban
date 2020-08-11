from goban.player import Player
from goban.point import Point


class Intersection:
    def __init__(self):
        self.owner = None


class Board:
    def __init__(self, size: Point = Point(19, 19)):
        self.size = size
        self.grid = [[Intersection() for x in range(size.x)] for y in range(size.y)]

    def update_point(self, point: Point, player: Player):
        self.grid[point.x][point.y].owner = player
