import pygame
from pygame.locals import *

class Pipe:
    def __init__(self, game_settings,window,short,x,y):
        self.game_settings,self.win = game_settings,window
        self.x, self.y = x, y
        if short:
            self.image = self.game_settings.pipe_short_image
        else:
            self.image = self.game_settings.pipe_tall_image
        self.image_con = self.image.convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()


    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(self.image, (self.x,self.y))
        pygame.draw.rect(self.win,(255,0,255),self.hit_box,3)
