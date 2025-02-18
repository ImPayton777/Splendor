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
    screen = pg.display.set_mode([1024, 1268])

    #get font
    pg.font.init()
    font = pg.freetype.SysFont(pg.font.get_default_font(), 50)
    FONTCOLOR = (255,255,255)
    
    lvl1 = pg.sprite.Group()
    lvl2 = pg.sprite.Group()
    lvl3 = pg.sprite.Group()

    c1 = (50,550)
    c2 = (50,300)
    c3 = (50, 50)
   #coord, white, blue, green, red, brown, points, gem, lvl
   #0 = white   1 = blue   2 = green   3 - red   4 - black
   #Level 1 Blacks
    lvl1.add(Card(c1,1,1,1,1,0,0,4,1))
    lvl1.add(Card(c1,1,2,1,1,0,0,4,1))
    lvl1.add(Card(c1,2,2,0,1,0,0,4,1))
    lvl1.add(Card(c1,0,0,1,3,1,0,4,1))
    lvl1.add(Card(c1,0,0,2,1,0,0,4,1))
    lvl1.add(Card(c1,2,0,2,0,0,0,4,1))
    lvl1.add(Card(c1,0,0,3,0,0,0,4,1))
    lvl1.add(Card(c1,0,4,0,0,0,1,4,1))
   #Level 1 Blues
    lvl1.add(Card(c1,1,0,1,1,1,0,1,1))
    lvl1.add(Card(c1,1,0,1,2,1,0,1,1))
    lvl1.add(Card(c1,1,0,2,2,0,0,1,1))
    lvl1.add(Card(c1,0,1,3,1,0,0,1,1))
    lvl1.add(Card(c1,1,0,0,0,2,0,1,1))
    lvl1.add(Card(c1,0,0,2,0,2,0,1,1))
    lvl1.add(Card(c1,0,0,0,0,3,0,1,1))
    lvl1.add(Card(c1,0,0,0,4,0,1,1,1))
   #Level 1 Whites
    lvl1.add(Card(c1,0,1,1,1,1,0,0,1))
    lvl1.add(Card(c1,0,1,2,1,1,0,0,1))
    lvl1.add(Card(c1,0,2,2,0,1,0,0,1))
    lvl1.add(Card(c1,3,1,0,0,1,0,0,1))
    lvl1.add(Card(c1,0,0,0,2,1,0,0,1))
    lvl1.add(Card(c1,0,2,0,0,2,0,0,1))
    lvl1.add(Card(c1,0,3,0,0,0,0,0,1))
    lvl1.add(Card(c1,0,0,4,0,0,1,0,1))
   #Level 1 Greens
    lvl1.add(Card(c1,1,1,0,1,1,0,2,1))
    lvl1.add(Card(c1,1,1,0,1,2,0,2,1))
    lvl1.add(Card(c1,0,1,0,2,2,0,2,1))
    lvl1.add(Card(c1,1,3,1,0,0,0,2,1))
    lvl1.add(Card(c1,2,1,0,0,0,0,2,1))
    lvl1.add(Card(c1,0,2,0,2,0,0,2,1))
    lvl1.add(Card(c1,0,0,0,3,0,0,2,1))
    lvl1.add(Card(c1,0,0,0,0,4,1,2,1))
   #Level 1 Reds
    lvl1.add(Card(c1,1,1,1,0,1,0,3,1))
    lvl1.add(Card(c1,2,1,1,0,1,0,3,1))
    lvl1.add(Card(c1,2,0,1,0,2,0,3,1))
    lvl1.add(Card(c1,1,0,0,1,3,0,3,1))
    lvl1.add(Card(c1,0,2,1,0,0,0,3,1))
    lvl1.add(Card(c1,2,0,0,2,0,0,3,1))
    lvl1.add(Card(c1,3,0,0,0,0,0,3,1))
    lvl1.add(Card(c1,4,0,0,0,0,1,3,1))


   #Level 2 Blacks
    lvl2.add(Card(c2,3,2,2,0,0,1,4,2))
    lvl2.add(Card(c2,3,0,3,0,2,1,4,2))
    lvl2.add(Card(c2,0,1,4,2,0,2,4,2))
    lvl2.add(Card(c2,0,0,5,3,0,2,4,2))
    lvl2.add(Card(c2,5,0,0,0,0,2,4,2))
    lvl2.add(Card(c2,0,0,0,0,6,3,4,2))
   #Level 2 Blues
    lvl2.add(Card(c2,0,2,2,3,0,1,1,2))
    lvl2.add(Card(c2,0,2,3,0,3,1,1,2))
    lvl2.add(Card(c2,5,3,0,0,0,2,1,2))
    lvl2.add(Card(c2,2,0,0,1,4,2,1,2))
    lvl2.add(Card(c2,0,5,0,0,0,2,1,2))
    lvl2.add(Card(c2,0,6,0,0,0,3,1,2))
   #Level 2 Whites
    lvl2.add(Card(c2,0,0,3,2,2,1,0,2))
    lvl2.add(Card(c2,2,3,0,3,0,1,0,2))
    lvl2.add(Card(c2,0,0,1,4,2,2,0,2))
    lvl2.add(Card(c2,0,0,0,5,3,2,0,2))
    lvl2.add(Card(c2,0,0,0,5,0,2,0,2))
    lvl2.add(Card(c2,6,0,0,0,0,3,0,2))
   #Level 2 Greens
    lvl2.add(Card(c2,3,0,2,3,0,1,2,2))
    lvl2.add(Card(c2,2,3,0,0,2,1,2,2))
    lvl2.add(Card(c2,4,2,0,0,1,2,2,2))
    lvl2.add(Card(c2,0,5,3,0,0,2,2,2))
    lvl2.add(Card(c2,0,0,5,0,0,2,2,2))
    lvl2.add(Card(c2,0,0,6,0,0,3,2,2))
   #Level 2 Reds
    lvl2.add(Card(c2,2,0,0,2,3,1,3,2))
    lvl2.add(Card(c2,0,3,0,2,3,1,3,2))
    lvl2.add(Card(c2,1,4,2,0,0,2,3,2))
    lvl2.add(Card(c2,3,0,0,0,5,2,3,2))
    lvl2.add(Card(c2,0,0,0,0,5,2,3,2))
    lvl2.add(Card(c2,0,0,0,6,0,3,3,2))


   #Level 3 Blacks
    lvl3.add(Card(c3,3,3,5,3,0,3,4,3))
    lvl3.add(Card(c3,0,0,0,7,0,4,4,3))
    lvl3.add(Card(c3,0,0,3,6,3,4,4,3))
    lvl3.add(Card(c3,0,0,0,7,3,5,4,3))
   #Level 3 Blues
    lvl3.add(Card(c3,3,0,3,3,5,3,1,3))
    lvl3.add(Card(c3,7,0,0,0,0,4,1,3))
    lvl3.add(Card(c3,6,3,0,0,3,4,1,3))
    lvl3.add(Card(c3,7,3,0,0,0,5,1,3))
   #Level 3 Whites
    lvl3.add(Card(c3,0,3,3,5,3,3,0,3))
    lvl3.add(Card(c3,0,0,0,0,7,4,0,3))
    lvl3.add(Card(c3,3,0,0,3,6,4,0,3))
    lvl3.add(Card(c3,3,0,0,0,7,5,0,3))
   #Level 3 Greens
    lvl3.add(Card(c3,5,3,0,3,3,3,2,3))
    lvl3.add(Card(c3,0,7,0,0,0,4,2,3))
    lvl3.add(Card(c3,3,6,3,0,0,4,2,3))
    lvl3.add(Card(c3,0,7,3,0,0,5,2,3))
   #Level 3 Reds
    lvl3.add(Card(c3,3,5,3,0,3,3,3,3))
    lvl3.add(Card(c3,0,0,7,0,0,4,3,3))
    lvl3.add(Card(c3,0,3,6,3,0,4,3,3))
    lvl3.add(Card(c3,0,0,7,3,0,5,3,3))

    # Get font setup
    pg.freetype.init()
    font_size = 64
    # Make a tuple for FONTCOLOR
    FONTCOLOR = (255,0,0)
    # Startup the main game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # handle MOUSEBUTTONUP
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                # get a list of all sprites that are under the mouse cursor
                #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                # do something with the clicked sprites...
        screen.fill((0, 0, 0))
        lvl1.draw(screen)

        lvl2.draw(screen)
        lvl3.draw(screen)
        font.render_to(screen, (5, 5), "Desk", FONTCOLOR, None, size=50)
        pg.display.flip()

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
