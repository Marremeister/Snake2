from main import *
from Super_class import *

class Point_counter(Text):
    def __init__(self, game, x, y, font, font_size):
        self.score = 0
        output = "Score : " + str(self.score) # Fråga om att implementera, vill ha drawfunktionen i en superklass
        color = (255, 255, 255)
        super().__init__(game, x, y, font, font_size)

    def draw(self):
        self.text = self.font.render("Score : " + str(self.score), True, (255, 255, 255))  #Vill helt enkelt byta ut första del mot "output" och andra del mot "color"
        self.game.screen.blit(self.text, (self.x, self.y))

