import pygame
from pygame.locals import *

class Pipe:
    def __init__(self, game_settings,window,x,y):
        self.game_settings,self.win = game_settings,window
        self.x, self.y = x, y
        self.image = self.game_settings.pipe_short_image
        self.image_con = self.image.convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()



    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(self.image, (self.x,self.y))
        # pygame.draw.rect(self.win,(255,0,255),self.hit_box,2)

class SmallPipe(Pipe):
    def __init__(self,game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_short_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image, (30,30)), (self.x,self.y))

class MediumPipe(Pipe):
    def __init__(self, game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_medium_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image, (30,50)), (self.x,self.y))

class TallPipe(Pipe):
    def __init__(self, game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_tall_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image, (30,65)), (self.x,self.y))
