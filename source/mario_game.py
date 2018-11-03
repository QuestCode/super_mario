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
        pygame.init()
        self.game_settings = Settings()
        self.win = pygame.display.set_mode((self.game_settings.screen_width,self.game_settings.screen_height))
        pygame.display.set_caption('Super Mario')

        """Level Initialization"""
        self.level = Level1(self.game_settings,self.win)
        self.bg = pygame.image.load(self.level.bg_image).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.clock = pygame.time.Clock()
        self.game_speed = 6.5

    def redrawWindow(self):
        self.win.blit(self.bg, (self.bgX,0))
        self.win.blit(self.bg,(self.bgX2,0))
        self.mario.draw()

        for pipe in self.pipes:
            pipe.draw()

        for box in self.boxes:
            box.draw()
        pygame.display.update()


    def start(self):
        self.mario = Mario(self.game_settings,self.win)
        self.pipes = self.level.pipes
        self.boxes = self.level.boxes
        pygame.time.set_timer(USEREVENT+1,500)
        self.speed = 30

        while True:
            self.redrawWindow()
            self.objects_movement()

            self.bgX -= self.game_speed
            self.bgX2 -= self.game_speed
            if self.bgX < self.bg.get_width() *-1:
                self.bgX = self.bg.get_width()
            if self.bgX2 < self.bg.get_width() *-1:
                self.bgX2 = self.bg.get_width()

            self.event_handler()

            self.clock.tick(self.speed)

    def objects_movement(self):
        for pipe in self.pipes:
            pipe.x -= self.game_speed

        for box in self.boxes:
            box.x -= self.game_speed

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
