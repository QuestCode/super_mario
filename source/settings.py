import pygame
import os, sys
from pygame.locals import *

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.game_title = 'Mario'
        self.screen_width = 500
        self.screen_height = 235
        self.bg_color = (0,0,0)
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        # self.read_score_file()

        self.marioX = 300
        self.marioY = 175
        self.mario_width = 64
        self.mario_height = 64

        self.jumping_mario_images = [self.__load_image('mario-' + str(x) + '.png',-1) for x in range(8,16)]
        self.running_mario_images = [self.__load_image('mario-' + str(x) + '.png',-1) for x in range(1,4)]

        self.pipe_short_image = self.__load_image('pipe_short.png')
        self.pipe_medium_image = self.__load_image('pipe_medium.png')
        self.pipe_tall_image = self.__load_image('pipe_tall.png')

        self.brick_box_image = self.__load_image('box_brick.png')
        self.mystery_box_image = self.__load_image('box_mystery.png')
        self.stair_box_image = self.__load_image('box_stair.png')


    def __load_image(self,name, colorkey=None):
        fullname = os.path.join('assets', 'images')
        fullname = os.path.join(fullname, name)
        try:
            image = pygame.image.load(fullname)
        except:
            print ('Cannot load image:', fullname)
            raise SystemExit
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image


    def play_sound(self,name):
        fullname = os.path.join('assets', 'sounds')
        fullname = os.path.join(fullname,'pacman_'+name)
        try:
            pygame.mixer.music.load(fullname)
            pygame.mixer.music.play()
        except :
            pass

    def read_score_file(self):
        filename = os.path.join('assets', 'scores.txt')
        try:
            self.r_scoreFile = open(filename,'r')
        except :
            print('no file')
            pass

    def write_score_file(self):
        filename = os.path.join('assets', 'scores.txt')
        try:
            self.w_scoreFile = open(filename,'w')
        except :
            print('no file')
            pass
