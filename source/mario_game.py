import pygame
from pygame.locals import *
import os, sys, random
from source.settings import Settings
from source.mario import Mario
from source.pipe import Pipe
from source.box import Box
from source.level import *


"""Prof DropBox https://www.dropbox.com/s/qo1hbcjh2sikbge/mario_physics.zip?dl=0"""

class MarioGame:

    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.win = pygame.display.set_mode((self.game_settings.screen_width,self.game_settings.screen_height))
        pygame.display.set_caption('Super Mario')

        """Level Initialization"""
        self.level = Level1(self.game_settings,self.win)
        self.bg = pygame.image.load(self.level.bg_image).convert()

        self.startX = 0
        self.bgX = 0
        # self.bgX2 = self.bg.get_width()
        self.clock = pygame.time.Clock()
        self.game_speed = 6.5

    def redrawWindow(self):
        self.win.blit(self.bg, (self.bgX,0))
        # self.win.blit(self.bg,(self.bgX2,0))
        self.mario.draw()

        for enemy in self.enemies:
            enemy.draw()

        for pipe in self.pipes:
            pipe.draw()
            if pipe.collide(self.mario.hit_box):
                pass

        for box in self.boxes:
            box.draw()
        pygame.display.update()


    def start(self):
        self.mario = Mario(self.game_settings,self.win)
        self.pipes = self.level.pipes
        self.boxes = self.level.boxes
        self.enemies = self.level.enemies
        self.speed = 50

        while True:
            self.redrawWindow()
            self.objects_movement()
            if self.bgX < -3000:
                print('game over')
                sys.exit()

            # print('bgX x: '+str(self.bgX))
            if self.mario.moving_right:
                self.bgX -= self.game_speed
                self.mario.x += 1
                if self.mario.x > self.game_settings.HW:
                    self.mario.x = self.game_settings.HW
                    self.startX = self.bgX
            elif self.mario.moving_left:
                if not self.bgX > self.startX:
                    # print('yes')
                    self.bgX += self.game_speed
                    self.mario.x -= 1
            self.event_handler()

            self.clock.tick(self.speed)

    def objects_movement(self):
        if self.mario.moving_right:
            for pipe in self.pipes:
                pipe.x -= self.game_speed

            for box in self.boxes:
                box.x -= self.game_speed
        elif self.mario.moving_left:
            if not self.bgX > self.startX:
                for pipe in self.pipes:
                    pipe.x += self.game_speed

                for box in self.boxes:
                    box.x += self.game_speed

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if ((e.key == pygame.K_RIGHT)
                or (e.key == pygame.K_LEFT)
                or (e.key == pygame.K_UP)):
                    self.mario.MoveKeyDown(e.key)
            elif e.type == pygame.KEYUP:
                if ((e.key == pygame.K_RIGHT)
                or (e.key == pygame.K_LEFT)
                or (e.key == pygame.K_UP)):
                    self.mario.MoveKeyUp(e.key)
                elif e.key == pygame.K_q:
                    sys.exit()
