from main import *
from Super_class import *

class Player(Text):
    def __init__(self, game, name, x, y, font, font_size):
        super().__init__(game, x, y, font, font_size)
        self.name = name

    def draw(self):
        self.text = self.font.render(self.name, True, (255, 255, 255))
        self.game.screen.blit(self.text, (self.x, self.y))


class Special_text(Text):
    def __init__(self, game, output, x, y, font, font_size, color):
        super().__init__(game, x, y, font, font_size)
        self.output = output
        self.color = color

    def draw(self):
        self.text = self.font.render(self.output, True, self.color)
        self.game.screen.blit(self.text, (self.x, self.y))

