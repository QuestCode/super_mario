import pygame
from pygame.locals import *

class Mario:
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,
    4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,
    -2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, game_settings,window):
        self.game_settings = game_settings
        self.win = window
        self.x = self.game_settings.marioX
        self.y = self.game_settings.marioY
        self.run_rt = self.game_settings.running_rt_mario_images
        self.run_lt = self.game_settings.running_lt_mario_images
        self.jump = self.game_settings.jumping_mario_images
        self.stopped_im = self.game_settings.stopped_mario_image
        self.image_con = self.stopped_im[0].convert()
        self.width,self.height = self.image_con.get_width(),self.image_con.get_height()
        self.jumping = False
        self.moving_left = False
        self.moving_right = False
        self.stopped = True
        self.jumpCount = 0
        self.runCount = 0

    def draw(self):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            self.win.blit(self.jump[self.jumpCount//5][0], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 20:
                self.y = self.game_settings.marioY
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        else:
            if self.moving_right:
                if self.runCount >= 4:
                    self.runCount = 0
                self.win.blit(self.run_rt[self.runCount//2][0], (self.x,self.y))
                self.runCount += 1
            elif self.moving_left:
                if self.runCount >= 4:
                    self.runCount = 0
                self.win.blit(self.run_lt[self.runCount//2][0], (self.x,self.y))
                self.runCount += 1
            elif self.stopped:
                self.win.blit(self.stopped_im[0], (self.x,self.y))

        self.hit_box = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(self.win,(255,0,255),self.hit_box,2)

    def MoveKeyDown(self,key):
        self.stopped = False
        if key == pygame.K_RIGHT:
            self.moving_right = True
        elif key == pygame.K_LEFT:
            self.moving_left = True
        elif key == pygame.K_UP:
            if not self.jumping:
                self.jumping = True

    def MoveKeyUp(self,key):
        self.stopped = True
        if key == pygame.K_RIGHT:
            self.moving_right = False
        elif key == pygame.K_LEFT:
            self.moving_left = False
        elif key == pygame.K_UP:
            pass
