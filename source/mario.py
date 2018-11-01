import pygame
from pygame.locals import *
import os, sys
from source.settings import Settings

class Mario(object):
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,
    4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,
    -2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, game_settings,window):
        self.x = game_settings.marioX
        self.y = game_settings.marioY
        self.width = game_settings.mario_width
        self.height = game_settings.mario_height
        self.run = game_settings.running_mario_images
        self.jump = game_settings.jumping_mario_images
        self.win = window
        self.jumping = False
        self.jumpCount = 0
        self.runCount = 0

    def draw(self):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            self.win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        else:
            if self.runCount > 4:
                self.runCount = 0
            self.win.blit(self.run[self.runCount//3], (self.x,self.y))
            self.runCount += 1
