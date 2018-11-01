import pygame
from pygame.locals import *

class Pipe:
    def __init__(self, game_settings,window,short,x,y):
        self.game_settings = game_settings
        self.win = window
        if short:
            self.image = self.game_settings.pipe_short_image
        else:
            self.image = self.game_settings.pipe_tall_image
        self.x = x
        self.y = y
        self.image_con = self.image.convert()

    def draw(self):
        self.hit_box = (self.x,self.y,self.image_con.get_width(),self.image_con.get_height())
        self.win.blit(self.image, (self.x,self.y))
        pygame.draw.rect(self.win,(255,0,255),self.hit_box,3)