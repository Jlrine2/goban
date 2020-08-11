import pygame

from goban.board import Board
from goban.point import Point

SQUARE_SIZE = 30


class Color:
    BLACK = (0, 0, 0)
    RED = (255, 45, 45)
    BACKGROUND = (212, 154, 44)


def draw_game(display: pygame.Surface, board: Board):

    for i in range(len(board.grid)):
        offset = i + 1
        start_pos = (SQUARE_SIZE * offset, SQUARE_SIZE)
        end_pos = (SQUARE_SIZE * offset, SQUARE_SIZE * len(board.grid))
        pygame.draw.line(display, Color.BLACK, start_pos, end_pos)

    for i in range(len(board.grid[0])):
        offset = i + 1
        start_pos = (SQUARE_SIZE, SQUARE_SIZE * offset)
        end_pos = (SQUARE_SIZE * len(board.grid), SQUARE_SIZE * offset)
        pygame.draw.line(display, Color.BLACK, start_pos, end_pos)

    for row in board.grid:
        for intersection in row:
            if intersection.owner is not None:
                point = Point(board.grid.index(row), row.index(intersection))
                draw_stone(display, point)


def draw_stone(display: pygame.Surface, point: Point):
    center = (SQUARE_SIZE * (point.x + 1)), (SQUARE_SIZE * (point.y + 1))
    pygame.draw.circle(display, Color.RED, center, int(SQUARE_SIZE / 2))
