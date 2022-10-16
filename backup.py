import pygame as pg
from game_objects import *
import sys



class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 1000
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.new_game()


    def draw_grid(self): # Ritar de vita grid-linjerna
        [pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
        for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
        for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def new_game(self): # Skapar ny snake och mat varje gång det blir new_game.
        self.snake = Snake(self)
        self.food = Food(self)


    def update(self): #Vet ej vad pg.display.flip() är men self.clock.tick(60) sätter displayen på 60 fps. Här körs även update-funktionen från snake, vilket typ är det viktigaste.
        self.snake.update()
        pg.display.flip()
        self.clock.tick(60)


    def draw(self): #Är funktionen som är ansvarig för hur bakgrunden ser ut
        self.screen.fill("black")
        self.draw_grid()
        self.food.draw()
        self.snake.draw()


    def check_event(self): # Kör en loop såläng spelet inte quittas
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            self.snake.control(event)


    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()





