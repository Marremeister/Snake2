import pygame as pg
from random import  randrange

class Movables:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()

    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2


class Text:
    def __init__(self, game, x, y, font, font_size):
        self.game = game
        self.x = x
        self.y = y
        self.font = pg.font.Font(font, font_size)
        #self.output = output
        #self.color = color

    #def draw(self):
        #self.text = self.font.render(self.output, True, self.color)
        #self.game.screen.blit(self.text, (self.x, self.y))