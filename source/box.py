import pygame
from pygame.locals import *

class Box:
    def __init__(self, game_settings,window,x,y):
        self.game_settings,self.win = game_settings,window
        self.x, self.y = x,y
        self.image = self.game_settings.brick_box_image
        self.image_con = self.image[0].convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image[0], (15,15)), (self.x,self.y))
        # pygame.draw.rect(self.win,(255,0,255),self.hit_box,3)

    # def collide_bot(self,rect):
    #     if rect[0]

class RegularBox(Box):
    def __init__(self, game_settings,window,x,y):
        Box.__init__(self,game_settings,window,x,y)
        self.game_settings,self.win = game_settings,window
        self.image = self.game_settings.brick_box_image

class MysteryBox(Box):
    def __init__(self, game_settings,window,x,y):
        Box.__init__(self,game_settings,window,x,y)
        self.game_settings,self.win = game_settings,window
        self.image = self.game_settings.mystery_box_image

class StairBox(Box):
    def __init__(self, game_settings,window,x,y):
        Box.__init__(self,game_settings,window,x,y)
        self.game_settings,self.win = game_settings,window
        # self.image = self.game_settings.stair_box_image

    def draw(self):
        self.hit_box = (self.x,self.y,15,15)
        pygame.draw.rect(self.win,(255,255,255),self.hit_box,2)
        # self.win.blit(pygame.transform.scale(self.image, (15,16)), (self.x,self.y))
