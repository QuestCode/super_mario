import os
import pygame
from source.pipe import *
from source.box import *
from source.enemy import *

class Level:
    def __init__(self,game_settings,win,image):
        self.game_settings, self.win = game_settings,win
        self.bg_image = os.path.join('assets/images',image)
        self.boxes = []
        self.pipes = []
        self.enemies = []

class Level1(Level):
    def __init__(self,game_settings,win):
        Level.__init__(self,game_settings,win,'mario_bg.png')
        self.add_pipes()
        self.add_boxes()
        self.add_enemies()

    def add_enemies(self):
        ground_height = 190
        self.enemies.append(Goomba(self.game_settings,self.win,500,ground_height))

    def add_pipes(self):
        short_pipe_h = 178
        """Short Pipes"""
        self.pipes.append(SmallPipe(self.game_settings,self.win,450,short_pipe_h))
        self.pipes.append(SmallPipe(self.game_settings,self.win,2610,short_pipe_h))
        self.pipes.append(SmallPipe(self.game_settings,self.win,2865,short_pipe_h))

        medium_pipe_h = 158
        self.pipes.append(MediumPipe(self.game_settings,self.win,605,medium_pipe_h))

        tall_pipe_h = 143
        """Tall Pipes"""
        self.pipes.append(TallPipe(self.game_settings,self.win,730,tall_pipe_h))
        self.pipes.append(TallPipe(self.game_settings,self.win,910,tall_pipe_h))

    def add_boxes(self):
        first_level_y = 145
        second_level_y = 80

        """Mystery Boxes"""
        self.boxes.append(MysteryBox(self.game_settings,self.win,280,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,350,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,380,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1215,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1700,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1750,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1800,first_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,2730,first_level_y))

        """Regular Boxes"""
        self.boxes.append(RegularBox(self.game_settings,self.win,335,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,365,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,395,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1200,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1230,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1515,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1600,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1615,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1630,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1890,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,2700,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,2715,first_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,2745,first_level_y))

        """SECOND LEVEL"""
        """Mystery Boxes"""
        self.boxes.append(MysteryBox(self.game_settings,self.win,365,second_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1515,second_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,1750,second_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,2055,second_level_y))
        self.boxes.append(MysteryBox(self.game_settings,self.win,2070,second_level_y))

        """Regular Boxes"""
        self.boxes.append(RegularBox(self.game_settings,self.win,1260,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1275,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1290,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1305,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1320,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1335,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1350,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1365,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1380,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1470,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1485,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1500,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1930,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1945,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1960,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,1975,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,2040,second_level_y))
        self.boxes.append(RegularBox(self.game_settings,self.win,2085,second_level_y))

        """Stairs"""
        floor_stairs_y = 192
        second_level_stairs_y = floor_stairs_y - 15
        third_level_stairs_y = second_level_stairs_y - 17
        fourth_level_stairs_y = third_level_stairs_y - 17
        space = 2

        """First Up Stairs"""
        self.boxes.append(StairBox(self.game_settings,self.win,2145,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2160+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2175+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2190+space,floor_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2160+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2175+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2190+space,second_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2175+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2190+space,third_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2190+space,fourth_level_stairs_y))


        """First Down Stairs"""
        self.boxes.append(StairBox(self.game_settings,self.win,2240+space,fourth_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2240+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2255+space,third_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2240+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2255+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2270+space,second_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2240+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2255+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2270+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2285+space,floor_stairs_y))


        """Second Up Stairs"""
        self.boxes.append(StairBox(self.game_settings,self.win,2370,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2385+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2400+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2415+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2430+space,floor_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2385+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2400+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2415+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2430+space,second_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2400+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2415+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2430+space,third_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2415+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2430+space,fourth_level_stairs_y))


        """Second Down Stairs"""
        self.boxes.append(StairBox(self.game_settings,self.win,2480+space,fourth_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2480+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2495+space,third_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2480+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2495+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2510+space,second_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,2480+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2495+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2510+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,2525+space,floor_stairs_y))


        first_step = 2895
        second_step = 2910
        third_step = 2925
        fourth_step = 2940
        fifth_step = 2960
        sixth_step = 2975
        seventh_step = 2990
        eighth_step = 3005
        ninth_step = 3020


        """Third Up Stairs"""
        self.boxes.append(StairBox(self.game_settings,self.win,first_step,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,second_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,third_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fourth_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fifth_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,floor_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,floor_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,second_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,third_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fourth_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fifth_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,second_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,second_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,third_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fourth_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fifth_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,third_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,third_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,fourth_step+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,fifth_step+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,fourth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,fourth_level_stairs_y))

        fifth_level_stairs_y = fourth_level_stairs_y - 15
        sixth_level_stairs_y = fifth_level_stairs_y - 15
        seventh_level_stairs_y = sixth_level_stairs_y - 15
        eighth_level_stairs_y = seventh_level_stairs_y - 15
        ninth_level_stairs_y = eighth_level_stairs_y - 15

        self.boxes.append(StairBox(self.game_settings,self.win,fifth_step+space,fifth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,fifth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,fifth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,fifth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,fifth_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,sixth_step+space,sixth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,sixth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,sixth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,sixth_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,seventh_step+space,seventh_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,seventh_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,seventh_level_stairs_y))

        self.boxes.append(StairBox(self.game_settings,self.win,eighth_step+space,eighth_level_stairs_y))
        self.boxes.append(StairBox(self.game_settings,self.win,ninth_step+space,eighth_level_stairs_y))
