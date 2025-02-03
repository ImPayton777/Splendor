#!/usr/bin/env python3

import pygame as pg                                                              import pygame.freetype                                                           import os
from pygame.locals import *

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    # Get font setup
    pg.freetype.init()
    font_size = 64
    # Make a tuple for FONTCOLOR
    FONTCOLOR = (255,0,0)
    # Startup the main game loop
    running = True
    while running:

