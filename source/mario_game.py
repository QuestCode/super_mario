import pygame
from pygame.locals import *
import os, sys, random
from source.settings import Settings
from source.mario import Mario
from source.pipe import Pipe
from source.box import Box
from source.level import *

class MarioGame:

    def __init__(self):
        self.game_settings = Settings()
        self.level = Level1()
        pygame.init()
        self.win = pygame.display.set_mode((self.game_settings.screen_width,self.game_settings.screen_height))
        pygame.display.set_caption('Super Mario')
        self.bg = pygame.image.load(self.level.bg_image).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.clock = pygame.time.Clock()

    def redrawWindow(self):
        self.win.blit(self.bg, (self.bgX,0))
        self.win.blit(self.bg,(self.bgX2,0))
        self.mario.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.brick_box.draw()
        self.mystery_box.draw()
        pygame.display.update()


    def start(self):
        self.mario = Mario(self.game_settings,self.win)
        self.pipes = []
        self.mystery_box = Box(self.game_settings,self.win,True,280,120)
        self.brick_box = Box(self.game_settings,self.win,False,300,120)
        pygame.time.set_timer(USEREVENT+1,500)
        pygame.time.set_timer(USEREVENT+2,random.randrange(2000,8500))
        self.speed = 30

        while True:
            self.redrawWindow()
            self.pipes_movement()

            self.bgX -= 1.4
            self.bgX2 -= 1.4
            if self.bgX < self.bg.get_width() *-1:
                self.bgX = self.bg.get_width()
            if self.bgX2 < self.bg.get_width() *-1:
                self.bgX2 = self.bg.get_width()

            self.event_handler()

            self.clock.tick(self.speed)

    def pipes_movement(self):
        for pipe in self.pipes:
            pipe.x -= 1.4

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == USEREVENT+1:
                self.speed += 1
            elif e.type == USEREVENT+2:
                r = random.randrange(0,2)
                if r == 0: # spawn a short pipe
                    self.pipes.append(Pipe(self.game_settings,self.win,True,1000,160))
                else: # spawn a tall pipe
                    self.pipes.append(Pipe(self.game_settings,self.win,False,1000,135))
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
