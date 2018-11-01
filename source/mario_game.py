import pygame
from pygame.locals import *
import os, sys
from source.settings import Settings
from source.mario import Mario
from source.pipe import Pipe

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
        self.mario.draw()
        self.short_pipe.draw()
        self.tall_pipe.draw()
        pygame.display.update()


    def start(self):
        self.mario = Mario(self.game_settings,self.win)
        self.short_pipe = Pipe(self.game_settings,self.win,True,400,160)
        self.tall_pipe = Pipe(self.game_settings,self.win,False,600,135)
        pygame.time.set_timer(USEREVENT+1,500)
        self.speed = 30

        while True:
            self.redrawWindow()

            self.bgX -= 1.4
            self.bgX2 -= 1.4
            if self.bgX < self.bg.get_width() *-1:
                self.bgX = self.bg.get_width()
            if self.bgX2 < self.bg.get_width() *-1:
                self.bgX2 = self.bg.get_width()

            self.event_handler()

            self.clock.tick(self.speed)

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == USEREVENT+1:
                self.speed += 1
            elif e.type == pygame.KEYDOWN:
                if ((e.key == pygame.K_RIGHT)
                or (e.key == pygame.K_LEFT)
                or (e.key == pygame.K_UP)
                or (e.key == pygame.K_DOWN)):
                    self.mario.MoveKeyDown(e.key)
            elif e.type == pygame.KEYUP:
                if ((e.key == pygame.K_RIGHT)
                or (e.key == pygame.K_LEFT)
                or (e.key == pygame.K_UP)
                or (e.key == pygame.K_DOWN)):
                    self.mario.MoveKeyUp(e.key)
                elif e.key == pygame.K_q:
                    sys.exit()
