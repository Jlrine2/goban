from goban.board import Board
from goban.game import Game
from goban.point import Point


def is_legal_move(game: Game, point: Point) -> bool:
    pass


def get_chain(point: Point, board: Board, unfinished_chain: list[Point] = []) -> list[Point]:
    unfinished_chain.append(point)
    for neighbor_point in get_neighbor_points(point, board.size):
        if neighbor_point not in unfinished_chain:
            unfinished_chain += get_chain(neighbor_point, board, unfinished_chain)
    return unfinished_chain


def get_neighbor_points(point: Point, board_size: Point) -> list[Point]:
    result = []
    directions = [
        Point(0, 1),
        Point(0, -1),
        Point(1, 0),
        Point(-1, 0),
    ]
    for direction in directions:
        neighbor_point = point + direction
        if is_on_board(neighbor_point, board_size):
            result.append(neighbor_point)
    return result


def is_on_board(point: Point, board_size: Point) -> bool:
    return 0 <= point.x < board_size.x and 0 <= point.y < board_size.y
