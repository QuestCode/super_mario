import pygame
from pygame.locals import *

class Pipe:
    def __init__(self, game_settings,window,x,y):
        self.game_settings,self.win = game_settings,window
        self.x, self.y = x, y
        self.image = self.game_settings.pipe_short_image
        self.image_con = self.image[0].convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()



    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(self.image, (self.x,self.y))
        # pygame.draw.rect(self.win,(255,0,255),self.hit_box,2)

    def collide(self,rect):
        # rect[0] == x rect[2] == width
        # rect[1] == y rect[4] == height
        if rect[0] + rect[2] > self.hit_box[0]:
            print('hit left')
            return True
        elif rect[0] < self.hit_box[0] + self.hit_box[2]:
            # if rect[1] + rect[3] > self.hit_box[1]:
            print('hit right')
            return True
        return False

class SmallPipe(Pipe):
    def __init__(self,game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_short_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image[0], (30,30)), (self.x,self.y))

class MediumPipe(Pipe):
    def __init__(self, game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_medium_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image[0], (30,50)), (self.x,self.y))

class TallPipe(Pipe):
    def __init__(self, game_settings,window,x,y):
        Pipe.__init__(self,game_settings,window,x,y)
        self.image = self.game_settings.pipe_tall_image

    def draw(self):
        self.hit_box = (self.x,self.y,self.width,self.height)
        self.win.blit(pygame.transform.scale(self.image[0], (30,65)), (self.x,self.y))
