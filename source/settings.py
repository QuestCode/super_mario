import pygame
import os, sys
from pygame.locals import *
# Needed to flip image
# from PIL import Image

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.game_title = 'Mario'
        self.screen_width,self.screen_height = 500,235
        self.HW, self.HH = self.screen_width/2, self.screen_height/2
        self.bg_color = (0,0,0)
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        # self.read_score_file()

        self.marioX = self.HW
        self.marioY = 175

        self.big_stopped_mario_image = self.__load_image('mario-0')
        self.big_jumping_mario_images = [self.__load_image('mario-' + str(x),-1) for x in range(16,21)]
        self.big_running_rt_mario_images = [self.__load_image('mario-' + str(x),-1) for x in range(1,4)]
        self.big_running_lt_mario_images = [self.__load_image('mario-' + str(x)+'-lt',-1) for x in range(1,4)]

        self.goomba_walking_images = [self.__load_image('goomba-0',-1),self.__load_image('goomba-1',-1)]
        self.goomba_squish_image = self.__load_image('goomba-2',-1)

        # self.reverse_image()

        self.pipe_short_image = self.__load_image('pipe_short')
        self.pipe_medium_image = self.__load_image('pipe_medium')
        self.pipe_tall_image = self.__load_image('pipe_tall')

        self.brick_box_image = self.__load_image('box_brick')
        self.mystery_box_image = self.__load_image('box_mystery')
        self.stair_box_image = self.__load_image('box_stair')


    def __load_image(self,name, colorkey=None):
        self.path = os.path.join('assets', 'images')
        fullname = os.path.join(self.path, name)
        fullpath = fullname+'.png'
        try:
            image = pygame.image.load(fullpath)
        except:
            print ('Cannot load image:', fullpath)
            raise SystemExit
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image , fullname

    # def flip_image(self,image_path,saved_location):
    #     image_obj = Image.open(image_path)
    #     rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    #     rotated_image.save(saved_location)
    #     return rotated_image

    # def reverse_image(self):
    #     self.running_lt_mario_images = []
    #     for image in self.running_rt_mario_images:
    #         flipped = self.flip_image(str(image[1])+'.png',str(image[1])+'-lt.png')
    #         self.running_lt_mario_images.append(flipped)

    def play_sound(self,name):
        fullname = os.path.join('assets', 'sounds')
        fullname = os.path.join(fullname,name)
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
