import pygame as pg
import pygame.sprite

from main import *



class Button:
    def __init__(self, game, x, y, image):
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        if not self.clicked:
            self.scaler((400, 400))
            self.game.screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            pass

    def scaler(self, size):
        self.image = pygame.transform.scale(self.image, size)


    def mouse(self):
        self.pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.clicked = True



class Main_menu(pygame.sprite.Sprite):
    def __init__(self, game, image_file, location, button):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.game = game
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.start_btn = button


    def scaler(self):
        self.image = pygame.transform.scale(self.image, (self.game.width, self.game.height))

    def draw(self):
        if not self.start_btn.clicked:
            self.scaler()
            self.game.screen.fill([255, 255, 255])
            self.game.screen.blit(self.image, self.rect)
            self.start_btn.draw()
        else:
            pass





