#!/usr/bin/env python3
import os
import pygame.freetype
import pygame as pg 
from pygame.locals import *
from random import choice
from card import Card
from tokens import Tokens
from player import Player

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1300, 1400])

    #get font
    pg.font.init()
    font = pg.freetype.SysFont(pg.font.get_default_font(), 50)
    FONTCOLOR = (255,255,255)
    name = "Shop:"
    
    lvl1 = pg.sprite.Group()
    lvl2 = pg.sprite.Group()
    lvl3 = pg.sprite.Group()
    whiteTokens = pg.sprite.Group()
    blueTokens = pg.sprite.Group()
    greenTokens = pg.sprite.Group()
    redTokens = pg.sprite.Group()
    brownTokens = pg.sprite.Group()

    c1 = (50,550)
    c2 = (50,300)
    c3 = (50, 50)
    #coord, white, blue, green, red, brown, points, gem, lvl
    #0 = white   1 = blue   2 = green   3 - red   4 - black
    #Level 1 Blacks
    d1 = Card(c1,1,1,1,1,0,0,4,1)
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

    #l = list lvl
    l1 = list(lvl1)
    l2 = list(lvl2)
    l3 = list(lvl3)

    # Get font setup
    pg.freetype.init()
    #pull out random cards 
    l1c1 = choice(l1)
    l1.remove(l1c1)
    l1c1.update(200)
    l1c2 = choice(l1)
    l1.remove(l1c2)
    l1c2.update(370)
    l1c3 = choice(l1)
    l1.remove(l1c3)
    l1c3.update(540)
    l1c4 = choice(l1)
    l1.remove(l1c4)
    l1c4.update(710)

    l2c1 = choice(l2)
    l2.remove(l2c1)
    l2c1.update(200)
    l2c2 = choice(l2)
    l2.remove(l2c2)
    l2c2.update(370)
    l2c3 = choice(l2)
    l2.remove(l2c3)
    l2c3.update(540)
    l2c4 = choice(l2)
    l2.remove(l2c4)
    l2c4.update(710)

    l3c1 = choice(l3)
    l3.remove(l3c1)
    l3c1.update(200)
    l3c2 = choice(l3)
    l3.remove(l3c2)
    l3c2.update(370)
    l3c3 = choice(l3)
    l3.remove(l3c3)
    l3c3.update(540)
    l3c4 = choice(l3)
    l3.remove(l3c4)
    l3c4.update(710)

    #Card costs
    c11 = l1c1.getCost()
    c12 = l1c2.getCost()
    c13 = l1c3.getCost()
    c14 = l1c4.getCost()
    c21 = l2c1.getCost()
    c22 = l2c2.getCost()
    c23 = l2c3.getCost()
    c24 = l2c4.getCost()
    c31 = l3c1.getCost()
    c32 = l3c2.getCost()
    c33 = l3c3.getCost()
    c34 = l3c4.getCost()
    #Card points
    p11 = l1c1.getPoints()
    p12 = l1c2.getPoints()
    p13 = l1c3.getPoints()
    p14 = l1c4.getPoints()
    p21 = l2c1.getPoints()
    p22 = l2c2.getPoints()
    p23 = l2c3.getPoints()
    p24 = l2c4.getPoints()
    p31 = l3c1.getPoints()
    p32 = l3c2.getPoints()
    p33 = l3c3.getPoints()
    p34 = l3c4.getPoints()

    t0 = (20,850)
    t1 = (170,850)
    t2 = (320,850)
    t3 = (470,850)
    t4 = (620,850)
    #create tokens
    #0 = white   1 = blue   2 = green   3 - red   4 - brown
    for i in range(7):
        whiteTokens.add(Tokens(t0, 0))
    for i in range(7):
        blueTokens.add(Tokens(t1, 1))
    for i in range(7):
        greenTokens.add(Tokens(t2, 2))
    for i in range(7):
        redTokens.add(Tokens(t3, 3))
    for i in range(7):
        brownTokens.add(Tokens(t4, 4))

    #create players
    p1 = Player()
    p2 = Player()

    #Turn
    turn = 0

    # Startup the main game loop
    running = True
    while running:
        if(turn == 0):
            player = p1
        else:
            player = p2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # handle MOUSEBUTTONUP
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                # get a list of all sprites that are under the mouse cursor
                #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                # do something with the clicked sprites...

        #Draw the board
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (100,100,100), Rect(940, 790, 300, 560))
        font.render_to(screen, (950, 800), name, (255,69,0), None, size=50)
        lvl1.draw(screen)
        lvl2.draw(screen)
        lvl3.draw(screen)
        whiteTokens.draw(screen)
        blueTokens.draw(screen)
        greenTokens.draw(screen)
        redTokens.draw(screen)
        brownTokens.draw(screen)
        font.render_to(screen, (5, 5), "Cards", FONTCOLOR, None, size=50)
        font.render_to(screen, (5, 800), "Tokens", FONTCOLOR, None, size=50)
        font.render_to(screen, (5, 960), "Inventory", FONTCOLOR, None, size=50)
        font.render_to(screen, (80, 200), "ooo", (255,255,255), None, size=50)
        font.render_to(screen, (95, 450), "oo", (255,255,255), None, size=50)
        font.render_to(screen, (110, 700), "o", (255,255,255), None, size=50)
        font.render_to(screen, (260, 60), str(p31), (0,0,0), None, size=45)
        drawCardType(screen, font,(325, 65),l3c1)
        font.render_to(screen, (260, 110), "Wh: " + str(c31[0]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 140), "Bl: " + str(c31[1]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 170), "Gr: " + str(c31[2]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 200), "Rd: " + str(c31[3]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 230), "Br: " + str(c31[4]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 60), str(p32), (0,0,0), None, size=45)
        drawCardType(screen, font,(490, 65),l3c2)
        font.render_to(screen, (430, 110), "Wh: " + str(c32[0]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 140), "Bl: " + str(c32[1]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 170), "Gr: " + str(c32[2]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 200), "Rd: " + str(c32[3]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 230), "Br: " + str(c32[4]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 60), str(p33), (0,0,0), None, size=45)
        drawCardType(screen, font,(660, 65),l3c3)
        font.render_to(screen, (600, 110), "Wh: " + str(c33[0]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 140), "Bl: " + str(c33[1]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 170), "Gr: " + str(c33[2]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 200), "Rd: " + str(c33[3]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 230), "Br: " + str(c33[4]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 60), str(p34), (0,0,0), None, size=45)
        drawCardType(screen, font,(830, 65),l3c4)
        font.render_to(screen, (770, 110), "Wh: " + str(c34[0]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 140), "Bl: " + str(c34[1]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 170), "Gr: " + str(c34[2]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 200), "Rd: " + str(c34[3]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 230), "Br: " + str(c34[4]), (0,0,0), None, size=25)

        font.render_to(screen, (260, 310), str(p21), (0,0,0), None, size=45)
        drawCardType(screen, font,(325, 315),l2c1)
        font.render_to(screen, (260, 360), "Wh: " + str(c21[0]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 390), "Bl: " + str(c21[1]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 420), "Gr: " + str(c21[2]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 450), "Rd: " + str(c21[3]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 480), "Br: " + str(c21[4]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 310), str(p22), (0,0,0), None, size=45)
        drawCardType(screen, font,(490, 315),l2c2)
        font.render_to(screen, (430, 360), "Wh: " + str(c22[0]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 390), "Bl: " + str(c22[1]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 420), "Gr: " + str(c22[2]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 450), "Rd: " + str(c22[3]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 480), "Br: " + str(c22[4]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 310), str(p23), (0,0,0), None, size=45)
        drawCardType(screen, font,(660, 315),l2c3)
        font.render_to(screen, (600, 360), "Wh: " + str(c23[0]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 390), "Bl: " + str(c23[1]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 420), "Gr: " + str(c23[2]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 450), "Rd: " + str(c23[3]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 480), "Br: " + str(c23[4]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 310), str(p24), (0,0,0), None, size=45)
        drawCardType(screen, font,(830, 315),l2c4)
        font.render_to(screen, (770, 360), "Wh: " + str(c24[0]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 390), "Bl: " + str(c24[1]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 420), "Gr: " + str(c24[2]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 450), "Rd: " + str(c24[3]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 480), "Br: " + str(c24[4]), (0,0,0), None, size=25)

        font.render_to(screen, (260, 560), str(p11), (0,0,0), None, size=45)
        drawCardType(screen, font,(325, 565),l1c1)
        font.render_to(screen, (260, 610), "Wh: " + str(c11[0]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 640), "Bl: " + str(c11[1]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 670), "Gr: " + str(c11[2]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 700), "Rd: " + str(c11[3]), (0,0,0), None, size=25)
        font.render_to(screen, (260, 730), "Br: " + str(c11[4]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 560), str(p12), (0,0,0), None, size=45)
        drawCardType(screen, font,(490, 565),l1c2)
        font.render_to(screen, (430, 610), "Wh: " + str(c12[0]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 640), "Bl: " + str(c12[1]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 670), "Gr: " + str(c12[2]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 700), "Rd: " + str(c12[3]), (0,0,0), None, size=25)
        font.render_to(screen, (430, 730), "Br: " + str(c12[4]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 560), str(p13), (0,0,0), None, size=45)
        drawCardType(screen, font,(660, 565),l1c1)
        font.render_to(screen, (600, 610), "Wh: " + str(c13[0]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 640), "Bl: " + str(c13[1]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 670), "Gr: " + str(c13[2]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 700), "Rd: " + str(c13[3]), (0,0,0), None, size=25)
        font.render_to(screen, (600, 730), "Br: " + str(c13[4]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 560), str(p14), (0,0,0), None, size=45)
        drawCardType(screen, font,(830, 565),l1c1)
        font.render_to(screen, (770, 610), "Wh: " + str(c14[0]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 640), "Bl: " + str(c14[1]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 670), "Gr: " + str(c14[2]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 700), "Rd: " + str(c14[3]), (0,0,0), None, size=25)
        font.render_to(screen, (770, 730), "Br: " + str(c14[4]), (0,0,0), None, size=25)
        pg.display.flip()

#0 = white   1 = blue   2 = green   3 - red   4 - brown
def drawCardType(screen,font,coords,card):
    if card.getCardType() == 0:
        font.render_to(screen, coords, "White", (255,255,255), None, size=25)
    elif card.getCardType() == 1:
        font.render_to(screen, coords, "Blue", (0,114,160), None, size=25)
    elif card.getCardType() == 2:
        font.render_to(screen, coords, "Green", (0,100,0), None, size=25)
    elif card.getCardType() == 3:
        font.render_to(screen, coords, "Red", (255,0,0), None, size=25)
    elif card.getCardType() == 4:
        font.render_to(screen, coords, "Brown", (92,64,51), None, size=25)

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
