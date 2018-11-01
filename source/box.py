import pygame
from pygame.locals import *

class Box:
    def __init__(self, game_settings,window,mystery,x,y):
        self.game_settings,self.win,self.mystery = game_settings,window,mystery
        self.x, self.y = x,y
        if self.mystery:
            self.image = self.game_settings.mystery_box_image
        else:
            self.image = self.game_settings.brick_box_image
        self.image_con = self.image.convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(self.image, (self.x,self.y))
        # pygame.draw.rect(self.win,(255,0,255),self.hit_box,3)
