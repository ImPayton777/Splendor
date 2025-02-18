#!/usr/bin/env python3
import os
import pygame.freetype                                                          
import pygame as pg 
from pygame.locals import *
from card import Card

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    lvl1 = []
    lvl2 = []
    lvl3 = []
   #coord, white, blue, green, red, brown, points, gem, lvl
   #0 = white   1 = blue   2 = green   3 - red   4 - black
   #Level 1 Blacks
    lvl1.append(Card(c,1,1,1,1,0,0,4,1))
    lvl1.append(Card(c,1,2,1,1,0,0,4,1))
    lvl1.append(Card(c,2,2,0,1,0,0,4,1))
    lvl1.append(Card(c,0,0,1,3,1,0,4,1))
    lvl1.append(Card(c,0,0,2,1,0,0,4,1))
    lvl1.append(Card(c,2,0,2,0,0,0,4,1))
    lvl1.append(Card(c,0,0,3,0,0,0,4,1))
    lvl1.append(Card(c,0,4,0,0,0,1,4,1))
   #Level 1 Blues
    lvl1.append(Card(c,1,0,1,1,1,0,1,1))
    lvl1.append(Card(c,1,0,1,2,1,0,1,1))
    lvl1.append(Card(c,1,0,2,2,0,0,1,1))
    lvl1.append(Card(c,0,1,3,1,0,0,1,1))
    lvl1.append(Card(c,1,0,0,0,2,0,1,1))
    lvl1.append(Card(c,0,0,2,0,2,0,1,1))
    lvl1.append(Card(c,0,0,0,0,3,0,1,1))
    lvl1.append(Card(c,0,0,0,4,0,1,1,1))
   #Level 1 Whites
    lvl1.append(Card(c,0,1,1,1,1,0,0,1))
    lvl1.append(Card(c,0,1,2,1,1,0,0,1))
    lvl1.append(Card(c,0,2,2,0,1,0,0,1))
    lvl1.append(Card(c,3,1,0,0,1,0,0,1))
    lvl1.append(Card(c,0,0,0,2,1,0,0,1))
    lvl1.append(Card(c,0,2,0,0,2,0,0,1))
    lvl1.append(Card(c,0,3,0,0,0,0,0,1))
    lvl1.append(Card(c,0,0,4,0,0,1,0,1))
   #Level 1 Greens
    lvl1.append(Card(c,1,1,0,1,1,0,2,1))
    lvl1.append(Card(c,1,1,0,1,2,0,2,1))
    lvl1.append(Card(c,0,1,0,2,2,0,2,1))
    lvl1.append(Card(c,1,3,1,0,0,0,2,1))
    lvl1.append(Card(c,2,1,0,0,0,0,2,1))
    lvl1.append(Card(c,0,2,0,2,0,0,2,1))
    lvl1.append(Card(c,0,0,0,3,0,0,2,1))
    lvl1.append(Card(c,0,0,0,0,4,1,2,1))
   #Level 1 Reds
    lvl1.append(Card(c,1,1,1,0,1,0,3,1))
    lvl1.append(Card(c,2,1,1,0,1,0,3,1))
    lvl1.append(Card(c,2,0,1,0,2,0,3,1))
    lvl1.append(Card(c,1,0,0,1,3,0,3,1))
    lvl1.append(Card(c,0,2,1,0,0,0,3,1))
    lvl1.append(Card(c,2,0,0,2,0,0,3,1))
    lvl1.append(Card(c,3,0,0,0,0,0,3,1))
    lvl1.append(Card(c,4,0,0,0,0,1,3,1))


   #Level 2 Blacks
    lvl2.append(Card(c,3,2,2,0,0,1,4,1))
    lvl2.append(Card(c,3,0,3,0,2,1,4,1))
    lvl2.append(Card(c,0,1,4,2,0,2,4,1))
    lvl2.append(Card(c,0,0,5,3,0,2,4,1))
    lvl2.append(Card(c,5,0,0,0,0,2,4,1))
    lvl2.append(Card(c,0,0,0,0,6,3,4,1))
   #Level 2 Blues
    lvl2.append(Card(c,0,2,2,3,0,1,1,1))
    lvl2.append(Card(c,0,2,3,0,3,1,1,1))
    lvl2.append(Card(c,5,3,0,0,0,2,1,1))
    lvl2.append(Card(c,2,0,0,1,4,2,1,1))
    lvl2.append(Card(c,0,5,0,0,0,2,1,1))
    lvl2.append(Card(c,0,6,0,0,0,3,1,1))
   #Level 2 Whites
    lvl2.append(Card(c,0,0,3,2,2,1,0,1))
    lvl2.append(Card(c,2,3,0,3,0,1,0,1))
    lvl2.append(Card(c,0,0,1,4,2,2,0,1))
    lvl2.append(Card(c,0,0,0,5,3,2,0,1))
    lvl2.append(Card(c,0,0,0,5,0,2,0,1))
    lvl2.append(Card(c,6,0,0,0,0,3,0,1))
   #Level 2 Greens
    lvl2.append(Card(c,3,0,2,3,0,1,2,1))
    lvl2.append(Card(c,2,3,0,0,2,1,2,1))
    lvl2.append(Card(c,4,2,0,0,1,2,2,1))
    lvl2.append(Card(c,0,5,3,0,0,2,2,1))
    lvl2.append(Card(c,0,0,5,0,0,2,2,1))
    lvl2.append(Card(c,0,0,6,0,0,3,2,1))
   #Level 2 Reds
    lvl2.append(Card(c,2,0,0,2,3,1,3,1))
    lvl2.append(Card(c,0,3,0,2,3,1,3,1))
    lvl2.append(Card(c,1,4,2,0,0,2,3,1))
    lvl2.append(Card(c,3,0,0,0,5,2,3,1))
    lvl2.append(Card(c,0,0,0,0,5,2,3,1))
    lvl2.append(Card(c,0,0,0,6,0,3,3,1))


   #Level 3 Blacks
    lvl3.append(Card(c,3,3,5,3,0,3,4,1))
    lvl3.append(Card(c,0,0,0,7,0,4,4,1))
    lvl3.append(Card(c,0,0,3,6,3,4,4,1))
    lvl3.append(Card(c,0,0,0,7,3,5,4,1))
   #Level 3 Blues
    lvl3.append(Card(c,3,0,3,3,5,3,1,1))
    lvl3.append(Card(c,7,0,0,0,0,4,1,1))
    lvl3.append(Card(c,6,3,0,0,3,4,1,1))
    lvl3.append(Card(c,7,3,0,0,0,5,1,1))
   #Level 3 Whites
    lvl3.append(Card(c,0,3,3,5,3,3,0,1))
    lvl3.append(Card(c,0,0,0,0,7,4,0,1))
    lvl3.append(Card(c,3,0,0,3,6,4,0,1))
    lvl3.append(Card(c,3,0,0,0,7,5,0,1))
   #Level 3 Greens
    lvl3.append(Card(c,5,3,0,3,3,3,2,1))
    lvl3.append(Card(c,0,7,0,0,0,4,2,1))
    lvl3.append(Card(c,3,6,3,0,0,4,2,1))
    lvl3.append(Card(c,0,7,3,0,0,5,2,1))
   #Level 3 Reds
    lvl3.append(Card(c,3,5,3,0,3,3,3,1))
    lvl3.append(Card(c,0,0,7,0,0,4,3,1))
    lvl3.append(Card(c,0,3,6,3,0,4,3,1))
    lvl3.append(Card(c,0,0,7,3,0,5,3,1))

    # Get font setup
    pg.freetype.init()
    font_size = 64
    # Make a tuple for FONTCOLOR
    FONTCOLOR = (255,0,0)
    # Startup the main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        pg.display.flip()