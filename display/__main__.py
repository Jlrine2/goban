import pygame

from goban.game import Game
from display.draw_util import Color, draw_game

pygame.init()

screensize = width, height = 600, 600
screen: pygame.Surface = pygame.display.set_mode(screensize)


game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                point = game.player.take_turn()
                game.update_point(point)

    screen.fill(Color.BACKGROUND)
    draw_game(screen, game.board)

    pygame.display.flip()
