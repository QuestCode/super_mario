import pygame
from pygame.locals import *

class Enemy:
    def __init__(self,game_settings,window,x,y):
        self.game_settings,self.win = game_settings,window
        self.x, self.y = x, y
        self.walking_images = self.game_settings.goomba_walking_images
        self.down_image = self.game_settings.goomba_squish_image
        self.image_con = self.down_image[0].convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()
        self.image_count = 0
        self.hit_top = False

class Goomba(Enemy):
    def __init__(self,game_settings,window,x,y):
        Enemy.__init__(self,game_settings,window,x,y)
        self.walking_images = self.game_settings.goomba_walking_images
        self.down_image = self.game_settings.goomba_squish_image

    def draw(self):
        if self.image_count >= 4:
            self.image_count = 0
        self.hit_box = (self.x,self.y,20,20)
        self.win.blit(pygame.transform.scale(self.walking_images[self.image_count//2][0],(20,20)), (self.x,self.y))
        self.image_count += 1
        pygame.draw.rect(self.win,(255,0,255),self.hit_box,2)

class KoopaTroopa(Enemy):
    def __init__(self,game_settings,window,x,y):
        Enemy.__init__(self,game_settings,window,x,y)
        self.walking_images = self.game_settings.goomba_walking_images

    def draw(self):
        pass
