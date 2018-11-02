import os
import pygame
from source.pipe import Pipe
from source.box import Box

class Level:
    def __init__(self,image):
        self.bg_image = os.path.join('assets/images',image)
        self.boxes = []
        self.pipes = []

class Level1(Level):
    def __init__(self):
        Level.__init__(self,'mario_bg.png')
