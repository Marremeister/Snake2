import pygame as pg
from random import randrange
from Super_class import *
from main import *

vec2 = pg.math.Vector2

class Snake(Movables):
    def __init__(self, game, score):
        super().__init__(game)
        self.direction = vec2(0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        self.score = score


    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and self.directions[pg.K_a]:
                self.direction = vec2(self.size, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}


    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def check_borders(self): #Kollar så att inte snaken kör på kanten av spelet
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.score_saver()
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.score_saver()
            self.game.new_game()

    def check_food(self): #self.rect.center är var något befinner sig just nu, i detta fall snaken. för att fatta var food befinner sig används self.game.food...
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1
            self.score.score += 1

    def check_selfeating(self): #Kollar så att man inte kör in i sig själv.
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.score_saver()
            self.game.new_game()

    def move(self): #När vi enl. funktionen self.control omvandlat en input till att data använder vi den datan för att faktiskt röra på oss.
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self): #Detta är funktionen som körs i denna klassen
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
       [pg.draw.rect(self.game.screen, "green", segment) for segment in self.segments]

class Food(Movables):
    def __init__(self, game):
        super().__init__(game)

    def draw(self):
        pg.draw.rect(self.game.screen, "red", self.rect)



