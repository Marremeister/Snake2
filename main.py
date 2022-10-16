import pygame as pg
from game_objects import *
import sys
from Button import *
from Point_counter import *
from player import *
from score_history import *

class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 1000
        self.width = 1500
        self.height = 1000
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.new_game()


    def draw_grid(self): # Ritar de vita grid-linjerna
        [pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
        for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
        for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def score_saver(self):
        self.round_score = Score_history(self, self.player.name, self.snake.score)


        #1. Få input om nickname
        #2. Appenda scoret i en lista med namnet i format [[namn1, score1], [namn2, score2], ...]
        #3. Kolla igenom alla scores och skapa text av score + namn, visa dessa highscores under nuvarande score på snake.

    def new_game(self): # Skapar ny snake och mat varje gång det blir new_game.
        start_img = pg.image.load("Bilder/green_start.png").convert_alpha()
        background_img = ("Bilder/snake.jpg")
        self.player = Player(self, "Nickname", 1200, 200, "freesansbold.ttf", 32) #Hur får jag input?
        self.score = Point_counter(self, 1200, 100, "freesansbold.ttf", 32)
        self.start_btn = Button(self, 250, 300, start_img)
        self.snake = Snake(self, self.score)
        self.food = Food(self)
        self.main_menu = Main_menu(self, background_img, (0, 0), self.start_btn)


    def update(self): #Vet ej vad pg.display.flip() är men self.clock.tick(60) sätter displayen på 60 fps. Här körs även update-funktionen från snake, vilket typ är det viktigaste.
        self.snake.update()
        pg.display.flip()
        self.clock.tick(60)


    def draw(self): #Är funktionen som är ansvarig för hur bakgrunden ser ut
        self.screen.fill([0, 0, 0])
        self.draw_grid()
        self.food.draw()
        self.snake.draw()
        self.player.draw()
        self.score.draw()
        try:
            self.round_score.draw_highscore()
        except Exception:
            print("No highscore yet")
        self.main_menu.draw()

    def check_event(self): # Kör en loop sålänge spelet inte quittas
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            Button.mouse(self.start_btn)
            if self.start_btn.clicked:
                self.snake.control(event)


    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.run()

