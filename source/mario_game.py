import pygame
from pygame.locals import *
import os, sys
from source.settings import Settings
from source.mario import Mario

class MarioGame:

    def __init__(self):
        self.game_settings = Settings()
        pygame.init()
        self.win = pygame.display.set_mode((self.game_settings.screen_width,self.game_settings.screen_height))
        pygame.display.set_caption('Super Mario')
        self.bg = pygame.image.load(os.path.join('assets/images','mario_bg.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.clock = pygame.time.Clock()

    def redrawWindow(self):
        self.win.blit(self.bg, (self.bgX,0))
        self.win.blit(self.bg,(self.bgX2,0))
        self.mario_character.draw()
        pygame.display.update()


    def start(self):
        self.mario_character = Mario(self.game_settings,self.win)
        pygame.time.set_timer(USEREVENT+1,500)
        self.speed = 30
        self.run = True

        while self.run:
            self.redrawWindow()

            self.bgX -= 1.4
            self.bgX2 -= 1.4
            if self.bgX < self.bg.get_width() *-1:
                self.bgX = self.bg.get_width()
            if self.bgX2 < self.bg.get_width() *-1:
                self.bgX2 = self.bg.get_width()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                if event.type == USEREVENT+1:
                    self.speed += 1

            self.clock.tick(self.speed)
