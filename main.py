#!/usr/bin/env python3
import os
import pygame.freetype
import pygame as pg 
from pygame.locals import *
from random import choice
from card import Card
from tokens import Tokens
from player import Player
from noble import Noble

class Main():
    def main(self):
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
        goldTokens = pg.sprite.Group()
        nobles = pg.sprite.Group()

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

        t0 = (20,850)
        t1 = (170,850)
        t2 = (320,850)
        t3 = (470,850)
        t4 = (620,850)
        t5 = (770, 850)
        #create tokens
        #0 = white   1 = blue   2 = green   3 - red   4 - brown
        for i in range(4):
            whiteTokens.add(Tokens(t0, 0))
        for i in range(4):
            blueTokens.add(Tokens(t1, 1))
        for i in range(4):
            greenTokens.add(Tokens(t2, 2))
        for i in range(4):
            redTokens.add(Tokens(t3, 3))
        for i in range(4):
            brownTokens.add(Tokens(t4, 4))
        for i in range(5):
            goldTokens.add(Tokens(t5, 5))

        #Creates Nobles
        #0 = white   1 = blue   2 = green   3 - red   4 - brown
        c = (2000, 50)

        nobles.add(Noble(c,0,0,4,4,0,3))
        nobles.add(Noble(c,3,0,0,3,3,3))
        nobles.add(Noble(c,4,4,0,0,0,3))
        nobles.add(Noble(c,4,0,0,0,4,3))
        nobles.add(Noble(c,0,4,4,0,0,3))
        nobles.add(Noble(c,0,3,3,3,0,3))
        nobles.add(Noble(c,3,3,3,0,0,3))
        nobles.add(Noble(c,0,0,0,4,4,3))
        nobles.add(Noble(c,3,3,0,0,3,3))
        nobles.add(Noble(c,0,0,3,3,3,3))
        
        n = list(nobles)

        #listify token groups and will be piles
        wT = list(whiteTokens)
        blT = list(blueTokens)
        gT = list(greenTokens)
        rT = list(redTokens)
        brT = list(brownTokens)
        gldT = list(goldTokens)

        #Tokens in shop
        shop = []

        #put all sprites in a list
        sprites = l1 + l2 + l3 + list(whiteTokens) + list(blueTokens) + list(greenTokens) + list(redTokens) + list(brownTokens) + list(goldTokens)

        # Get font setup
        pg.freetype.init()
        #pull out random cards 
        l1c1 = choice(l1)
        l1.remove(l1c1)
        l1c1.flip(200)
        l1c2 = choice(l1)
        l1.remove(l1c2)
        l1c2.flip(370)
        l1c3 = choice(l1)
        l1.remove(l1c3)
        l1c3.flip(540)
        l1c4 = choice(l1)
        l1.remove(l1c4)
        l1c4.flip(710)

        l2c1 = choice(l2)
        l2.remove(l2c1)
        l2c1.flip(200)
        l2c2 = choice(l2)
        l2.remove(l2c2)
        l2c2.flip(370)
        l2c3 = choice(l2)
        l2.remove(l2c3)
        l2c3.flip(540)
        l2c4 = choice(l2)
        l2.remove(l2c4)
        l2c4.flip(710)

        l3c1 = choice(l3)
        l3.remove(l3c1)
        l3c1.flip(200)
        l3c2 = choice(l3)
        l3.remove(l3c2)
        l3c2.flip(370)
        l3c3 = choice(l3)
        l3.remove(l3c3)
        l3c3.flip(540)
        l3c4 = choice(l3)
        l3.remove(l3c4)
        l3c4.flip(710)

        #Pulls out random nobles
        n1 = choice(n)
        n.remove(n1)
        n1.update(-1000,100)
        n2 = choice(n)
        n.remove(n2)
        n2.update(-1000,300)
        n3 = choice(n)
        n.remove(n3)
        n3.update(-1000,500)
        cur_nobles = [n1,n2,n3]

        #create players
        p1 = Player()
        p2 = Player()

        #Player Token inventory
        p1ti = []
        p2ti = []

        #Turn
        turn = 0

        #Shop positions of tokens
        shoppos = [True,True,True]

        #flags
        buying = False
        selectedCard = None
        grabin = False
        overStock = False
        endTurn = False
        invalid = False
        help = False

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
                # handle MOUSEBUTTONUP used from stackoverflow
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    # get a list of all sprites that are under the mouse cursor
                    cs = [s for s in sprites if s.rect.collidepoint(pos)]
                    x,y = pos
                    if len(cs) > 0 and not invalid:
                        # handles getting/returning tokens
                        if isinstance(cs[0], Tokens) and not (x < 940 and y > 960) and not buying:
                            grabin = True
                            name = "Get tokens:"
                            tp = cs[0].getType()
                            #Return tokens from shop
                            if x > 940:
                                i = shop.index(cs[0])
                                if tp == 0:
                                    shop[i].move(20,850)
                                    wT.append(shop.pop(i))
                                if tp == 1:
                                    shop[i].move(170,850)
                                    blT.append(shop.pop(i))
                                if tp == 2:
                                    shop[i].move(320,850)
                                    gT.append(shop.pop(i))
                                if tp == 3:
                                    shop[i].move(470,850)
                                    rT.append(shop.pop(i))
                                if tp == 4:
                                    shop[i].move(620,850)
                                    brT.append(shop.pop(i))
                                for i in range(len(shop)):
                                    shop[i].move(950, i*114+860)
                            else:
                                if len(shop) > 2:
                                    invalid = True
                                #Grab 2 of same type with another
                                if len(shop) == 2 and tp == 0:
                                    if shop[0].getType() == 0 or shop[1].getType() == 0:
                                        invalid = True
                                if len(shop) == 2 and tp == 1:
                                    if shop[0].getType() == 1 or shop[1].getType() == 1:
                                        invalid = True
                                if len(shop) == 2 and tp == 2:
                                    if shop[0].getType() == 2 or shop[1].getType() == 2:
                                        invalid = True
                                if len(shop) == 2 and tp == 3:
                                    if shop[0].getType() == 3 or shop[1].getType() == 3:
                                        invalid = True
                                if len(shop) == 2 and tp == 4:
                                    if shop[0].getType() == 4 or shop[1].getType() == 4:
                                        invalid = True
                                #Grab 3 of same type
                                if len(shop) == 2 and tp == 0 and len(wT) < 3:
                                    if shop[0].getType() == 0 or shop[1].getType() == 0:
                                        invalid = True
                                if len(shop) == 2 and tp == 1 and len(blT) < 3:
                                    if shop[0].getType() == 1 or shop[1].getType() == 1:
                                        invalid = True
                                if len(shop) == 2 and tp == 2 and len(gT) < 3:
                                    if shop[0].getType() == 2 or shop[1].getType() == 2:
                                        invalid = True
                                if len(shop) == 2 and tp == 3 and len(rT) < 3:
                                    if shop[0].getType() == 3 or shop[1].getType() == 3:
                                        invalid = True
                                if len(shop) == 2 and tp == 4 and len(brT) < 3:
                                    if shop[0].getType() == 4 or shop[1].getType() == 4:
                                        invalid = True
                                #IF valid grab
                                if not invalid:
                                    if tp == 0:
                                        tT = (wT.pop(0))
                                        tT.update(930, len(shop)*114+10)
                                        shop.append(tT)
                                    if tp == 1:
                                        tT = (blT.pop(0))
                                        tT.update(780, len(shop)*114+10)
                                        shop.append(tT)
                                    if tp == 2:
                                        tT = (gT.pop(0))
                                        tT.update(630, len(shop)*114+10)
                                        shop.append(tT)
                                    if tp == 3:
                                        tT = (rT.pop(0))
                                        tT.update(480, len(shop)*114+10)
                                        shop.append(tT)
                                    if tp == 4:
                                        tT = (brT.pop(0))
                                        tT.update(330, len(shop)*114+10)
                                        shop.append(tT)

                        #BUYING
                        if isinstance(cs[0], Card) and len(cs) == 1 and not grabin:
                            buying = True
                            selectedCard = cs[0]

                    #YES CARD
                    if 950 <= x <= 1230 and 970 <= y <= 1070 and buying and not invalid:
                        canUse = player.getCurrency()
                        cost = selectedCard.getCost()
                        if canUse[0] >= cost[0] and canUse[1] >= cost[1] and canUse[2] >= cost[2] and canUse[3] >= cost[3] and canUse[4] >= cost[4]:
                            returns = player.buyCard(selectedCard)
                            if selectedCard == l1c1:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c1 = choice(l1)
                                    l1.remove(l1c1)
                                    l1c1.flip(200)
                                else: 
                                    l1c1 = None
                            if selectedCard == l1c2:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c2 = choice(l1)
                                    l1.remove(l1c2)
                                    l1c2.flip(370)
                                else:
                                    l1c2 = None
                            if selectedCard == l1c3:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c3 = choice(l1)
                                    l1.remove(l1c3) 
                                    l1c3.flip(540)
                                else:
                                    l1c3 = None
                            if selectedCard == l1c4:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c4 = choice(l1)
                                    l1.remove(l1c4)
                                    l1c4.flip(710)
                                else:
                                    l1c4 = None
                            if selectedCard == l2c1:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c1 = choice(l2)
                                    l2.remove(l2c1)
                                    l2c1.flip(200)
                                else:
                                    l2c1 = None
                            if selectedCard == l2c2:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c2 = choice(l2)
                                    l2.remove(l2c2)
                                    l2c2.flip(370)
                                else:
                                    l2c2 = None
                            if selectedCard == l2c3:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c3 = choice(l2)
                                    l2.remove(l2c3)
                                    l2c3.flip(540)
                                else:
                                    l2c3 = None
                            if selectedCard == l2c4:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c4 = choice(l2)
                                    l2.remove(l2c4)
                                    l2c4.flip(710)
                                else:
                                    l2c4 = None
                            if selectedCard == l3c1:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c1 = choice(l3)
                                    l3.remove(l3c1) 
                                    l3c1.flip(200)
                                else:
                                    l3c1 = None
                            if selectedCard == l3c2:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c2 = choice(l3)
                                    l3.remove(l3c2)
                                    l3c2.flip(370)
                                else:
                                    l3c2 = None
                            if selectedCard == l3c3:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c3 = choice(l3)
                                    l3.remove(l3c3)
                                    l3c3.flip(540)
                                else:
                                    l3c3 = None
                            if selectedCard == l3c4:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c4 = choice(l3)
                                    l3.remove(l3c4)
                                    l3c4.flip(710)
                                else:
                                    l3c4 = None
                            selectedCard = None
                            turn = (turn+1)%2
                            buying = False
                            while len(returns) != 0:
                                tp = returns[0].getType()
                                if tp == 0:
                                    returns[0].move(20,850)
                                    wT.append(returns.pop(0))
                                if tp == 1:
                                    returns[0].move(170,850)
                                    blT.append(returns.pop(0))
                                if tp == 2:
                                    returns[0].move(320,850)
                                    gT.append(returns.pop(0))
                                if tp == 3:
                                    returns[0].move(470,850)
                                    rT.append(returns.pop(0))
                                if tp == 4:
                                    returns[0].move(620,850)
                                    brT.append(returns.pop(0))
                        else:
                            invalid = True
                            buying = False

                    #NO CARD
                    if 950 <= x <= 1230 and 1100 <= y <= 1200 and buying:
                        selectedCard = None
                        buying = False

                    #YES RESERVE
                    if 950 <= x <= 1230 and 1230 <= y <= 1330 and buying and not invalid:
                        if len(gldT) > 0:
                            gldT[0].update(1400)
                            able = player.reserveCard(selectedCard, gldT.pop(0))
                        else:
                            able = player.reserveCard(selectedCard)
                        if able == -1:
                            invalid = True
                        else:
                            if selectedCard == l1c1:
                                selectedCard.move(730,1025)
                                if len(l1) > 0:
                                    l1c1 = choice(l1)
                                    l1.remove(l1c1)
                                    l1c1.flip(200)
                                else:
                                    l1c1 = None
                            if selectedCard == l1c2:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c2 = choice(l1)
                                    l1.remove(l1c2)
                                    l1c2.flip(370)
                                else:
                                    l1c2 = None
                            if selectedCard == l1c3:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c3 = choice(l1)
                                    l1.remove(l1c3)
                                    l1c3.flip(540)
                                else:
                                    l1c3 = None
                            if selectedCard == l1c4:
                                selectedCard.update(1400)
                                if len(l1) > 0:
                                    l1c4 = choice(l1)
                                    l1.remove(l1c4)
                                    l1c4.flip(710)
                                else:
                                    l1c4 = None
                            if selectedCard == l2c1:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c1 = choice(l2)
                                    l2.remove(l2c1)
                                    l2c1.flip(200)
                                else:
                                    l2c1 = None
                            if selectedCard == l2c2:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c2 = choice(l2)
                                    l2.remove(l2c2)
                                    l2c2.flip(370)
                                else:
                                    l2c2 = None
                            if selectedCard == l2c3:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c3 = choice(l2)
                                    l2.remove(l2c3)
                                    l2c3.flip(540)
                                else:
                                    l2c3 = None
                            if selectedCard == l2c4:
                                selectedCard.update(1400)
                                if len(l2) > 0:
                                    l2c4 = choice(l2)
                                    l2.remove(l2c4)
                                    l2c4.flip(710)
                                else:
                                    l2c4 = None
                            if selectedCard == l3c1:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c1 = choice(l3)
                                    l3.remove(l3c1)
                                    l3c1.flip(200)
                                else:
                                    l3c1 = None
                            if selectedCard == l3c2:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c2 = choice(l3)
                                    l3.remove(l3c2)
                                    l3c2.flip(370)
                                else:
                                    l3c2 = None
                            if selectedCard == l3c3:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c3 = choice(l3)
                                    l3.remove(l3c3)
                                    l3c3.flip(540)
                                else:
                                    l3c3 = None
                            if selectedCard == l3c4:
                                selectedCard.update(1400)
                                if len(l3) > 0:
                                    l3c4 = choice(l3)
                                    l3.remove(l3c4)
                                    l3c4.flip(710)
                                else:
                                    l3c4 = None
                            selectedCard = None
                            turn = (turn+1)%2
                            buying = False

                    #Stop invalid screen
                    if invalid and 350 <= x <= 950 and 350 <= y <= 650:
                        invalid = False

                    #(150, 5, 40, 40)
                    #HELP BUTTON
                    if help == False and 150 <= x <= 190 and 5 <= y <= 45:
                        help = True

                    if help == True and 15 <= x <= 55 and 15 <= y <= 55:
                        help = False

                    #YES TOKEN
                    if 955 <= x <= 1085 and 1260 <= y <= 1330 and grabin:
                        chips = player.getTokens()
                        inv = chips[0]+chips[1]+chips[2]+chips[3]+chips[4]
                        #if len(shop)+inv > 10:
                        #    overStock = True
                        #    invalid = True
                        #else:
                        player.takeToken(shop)
                        while len(shop) != 0:
                            tp = shop[0].getType()
                            shop[0].update(1500)
                            if player == p1:
                                p2ti.append(shop.pop(0))
                            else:
                                p2ti.append(shop.pop(0))
                        grabin = False
                        name = "Shop:"
                        shoppos = [True, True, True]
                        #Check the player does not have more than ten tokens
                        if not overStock:
                            turn = (turn+1)%2

                    #NO TOKEN
                    if 1095 <= x <= 1225 and 1260 <= y <= 1330 and grabin and not reserve:
                        while len(shop) != 0:
                            tp = shop[0].getType()    
                            if tp == 0:
                                shop[0].move(20,850)
                                wT.append(shop.pop(0))
                            if tp == 1:
                                shop[0].move(170,850)
                                blT.append(shop.pop(0))
                            if tp == 2:
                                shop[0].move(320,850)
                                gT.append(shop.pop(0))
                            if tp == 3:
                                shop[0].move(470,850)
                                rT.append(shop.pop(0))
                            if tp == 4:
                                shop[0].move(620,850)
                                brT.append(shop.pop(0))
                        grabin = False
                        #overStock = False
                        name = "Shop:"
                        shoppos = [True, True, True]

            pt = player.getCurrency()
            cds = player.getCards()
            tokenns = player.getTokens()

            #Card costs
            if l1c1 != None:
                c11 = l1c1.getCost()
            if l1c2 != None:
                c12 = l1c2.getCost()
            if l1c3 != None:
                c13 = l1c3.getCost()
            if l1c4 != None:
                c14 = l1c4.getCost()
            if l2c1 != None:
                c21 = l2c1.getCost()
            if l2c2 != None:
                c22 = l2c2.getCost()
            if l2c3 != None:
                c23 = l2c3.getCost()
            if l2c4 != None:
                c24 = l2c4.getCost()
            if l3c1 != None:
                c31 = l3c1.getCost()
            if l3c2 != None:
                c32 = l3c2.getCost()
            if l3c3 != None:
                c33 = l3c3.getCost()
            if l3c4 != None:
                c34 = l3c4.getCost()

            #Noble Costs
            cn1 = n1.getCost()
            cn2 = n2.getCost()
            cn3 = n3.getCost()

            #Card points
            if l1c1 != None:
                p11 = l1c1.getPoints()
            if l1c2 != None:
                p12 = l1c2.getPoints()
            if l1c3 != None:
                p13 = l1c3.getPoints()
            if l1c4 != None:
                p14 = l1c4.getPoints()
            if l2c1 != None:
                p21 = l2c1.getPoints()
            if l2c2 != None:
                p22 = l2c2.getPoints()
            if l2c3 != None:
                p23 = l2c3.getPoints()
            if l2c4 != None:
                p24 = l2c4.getPoints()
            if l3c1 != None:
                p31 = l3c1.getPoints()
            if l3c2 != None:
                p32 = l3c2.getPoints()
            if l3c3 != None:
                p33 = l3c3.getPoints()
            if l3c4 != None:
                p34 = l3c4.getPoints()

            #Noble points
            pn1 = n1.getPoints()
            pn2 = n2.getPoints()
            pn3 = n3.getPoints()

            if player.getTotalPoints() > 14:
                running = False

            #I don't know how nobles are going to be drawn yet but this takes the image off of the board.
            nob_check = player.checkNoble(cur_nobles)
            if len(nob_check) != 0:
                for i in nob_check:
                    cur_nobles.remove(i)
                    i.update(1400)

            #Draw the board
            screen.fill((0, 0, 0))
            #Shop Draw
            pg.draw.rect(screen, (100,100,100), Rect(940, 790, 300, 580))
            font.render_to(screen, (950, 800), name, (255,69,0), None, size=50)
            if buying:
                spot = selectedCard.getCords()
                pg.draw.rect(screen, (255,255,255), Rect(spot[0]-5, spot[1]-5, 160, 220))
                font.render_to(screen, (950, 855), "Buy Card?", (255,0,0), None, size=50)
                pg.draw.rect(screen, (0,255,0), Rect(950, 970, 280, 100))
                pg.draw.rect(screen, (255,0,0), Rect(950, 1100, 280, 100))
                font.render_to(screen, (1025, 995), "YES", (0,0,0), None, size=60)
                font.render_to(screen, (1045, 1125), "NO", (0,0,0), None, size=60)
                pg.draw.rect(screen, (255,215,0), Rect(950, 1230, 280, 100))
                font.render_to(screen, (975, 1255), "Reserve", (0,0,0), None, size=60)
            if grabin:
                pg.draw.rect(screen, (0,255,0), Rect(955, 1260, 130, 70))
                pg.draw.rect(screen, (255,0,0), Rect(1095, 1260, 130, 70))
                font.render_to(screen, (965, 1270), "YES", (0,0,0), None, size=50)
                font.render_to(screen, (1115, 1270), "NO", (0,0,0), None, size=50)

            #Inventory Draw
            pg.draw.rect(screen, (100,100,100), Rect(5, 965, 925, 430))
            font.render_to(screen, (5, 1025), "Cards:", (255,69,0), None, size=50)
            font.render_to(screen, (5, 1070), " White: " + str(cds[0]) + " Blue: " + str(cds[1]) +" Green: " + str(cds[2]), (255,69,0), None, size=50)
            font.render_to(screen, (5, 1125), " Red: " + str(cds[3]) + " Brown: " + str(cds[4]), (255,69,0), None, size=50)
            font.render_to(screen, (5, 1175), " Points: " + str(player.getTotalPoints()), (255,69,0), None, size=50)
            font.render_to(screen, (5, 1225), "Tokens:", (255,69,0), None, size=50)
            font.render_to(screen, (5, 1270), " White: " + str(tokenns[0]) + " Blue: " + str(tokenns[1]) +" Green: " + str(tokenns[2]), (255,69,0), None, size=50)
            font.render_to(screen, (5, 1325), " Red: " + str(tokenns[3]) + " Brown: " + str(tokenns[4]), (255,69,0), None, size=50)
            #Sprite drawing
            lvl1.draw(screen)
            lvl2.draw(screen)
            lvl3.draw(screen)
            whiteTokens.draw(screen)
            blueTokens.draw(screen)
            greenTokens.draw(screen)
            redTokens.draw(screen)
            brownTokens.draw(screen)
            goldTokens.draw(screen)
            nobles.draw(screen)
            #Title draw
            font.render_to(screen, (920, 5), "Current Player:", FONTCOLOR, None, size=50)
            if player == p1:
                font.render_to(screen, (970, 75), "Player 1", FONTCOLOR, None, size=50)
            else:
                font.render_to(screen, (970, 75), "Player 2", FONTCOLOR, None, size=50)
            font.render_to(screen, (5, 5), "Cards", FONTCOLOR, None, size=50)
            font.render_to(screen, (5, 800), "Tokens", FONTCOLOR, None, size=50)
            font.render_to(screen, (5, 965), "Inventory", FONTCOLOR, None, size=50)

            #Flipped cards info draw
            if l3c1 != None:
                font.render_to(screen, (260, 60), str(p31), (0,0,0), None, size=45)
                drawCardType(screen, font,(325, 65),l3c1)
                font.render_to(screen, (260, 110), "Wh: " + str(c31[0]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 140), "Bl: " + str(c31[1]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 170), "Gr: " + str(c31[2]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 200), "Rd: " + str(c31[3]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 230), "Br: " + str(c31[4]), (0,0,0), None, size=25)
            if l3c2 != None:
                font.render_to(screen, (430, 60), str(p32), (0,0,0), None, size=45)
                drawCardType(screen, font,(490, 65),l3c2)
                font.render_to(screen, (430, 110), "Wh: " + str(c32[0]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 140), "Bl: " + str(c32[1]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 170), "Gr: " + str(c32[2]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 200), "Rd: " + str(c32[3]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 230), "Br: " + str(c32[4]), (0,0,0), None, size=25)
            if l3c3 != None:
                font.render_to(screen, (600, 60), str(p33), (0,0,0), None, size=45)
                drawCardType(screen, font,(660, 65),l3c3)
                font.render_to(screen, (600, 110), "Wh: " + str(c33[0]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 140), "Bl: " + str(c33[1]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 170), "Gr: " + str(c33[2]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 200), "Rd: " + str(c33[3]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 230), "Br: " + str(c33[4]), (0,0,0), None, size=25)
            if l3c4 != None:
                font.render_to(screen, (770, 60), str(p34), (0,0,0), None, size=45)
                drawCardType(screen, font,(830, 65),l3c4)
                font.render_to(screen, (770, 110), "Wh: " + str(c34[0]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 140), "Bl: " + str(c34[1]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 170), "Gr: " + str(c34[2]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 200), "Rd: " + str(c34[3]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 230), "Br: " + str(c34[4]), (0,0,0), None, size=25)

            if l2c1 != None:
                font.render_to(screen, (260, 310), str(p21), (0,0,0), None, size=45)
                drawCardType(screen, font,(325, 315),l2c1)
                font.render_to(screen, (260, 360), "Wh: " + str(c21[0]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 390), "Bl: " + str(c21[1]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 420), "Gr: " + str(c21[2]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 450), "Rd: " + str(c21[3]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 480), "Br: " + str(c21[4]), (0,0,0), None, size=25)
            if l2c2 != None:
                font.render_to(screen, (430, 310), str(p22), (0,0,0), None, size=45)
                drawCardType(screen, font,(490, 315),l2c2)
                font.render_to(screen, (430, 360), "Wh: " + str(c22[0]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 390), "Bl: " + str(c22[1]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 420), "Gr: " + str(c22[2]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 450), "Rd: " + str(c22[3]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 480), "Br: " + str(c22[4]), (0,0,0), None, size=25)
            if l2c3 != None:
                font.render_to(screen, (600, 310), str(p23), (0,0,0), None, size=45)
                drawCardType(screen, font,(660, 315),l2c3)
                font.render_to(screen, (600, 360), "Wh: " + str(c23[0]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 390), "Bl: " + str(c23[1]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 420), "Gr: " + str(c23[2]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 450), "Rd: " + str(c23[3]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 480), "Br: " + str(c23[4]), (0,0,0), None, size=25)
            if l2c4 != None:
                font.render_to(screen, (770, 310), str(p24), (0,0,0), None, size=45)
                drawCardType(screen, font,(830, 315),l2c4)
                font.render_to(screen, (770, 360), "Wh: " + str(c24[0]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 390), "Bl: " + str(c24[1]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 420), "Gr: " + str(c24[2]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 450), "Rd: " + str(c24[3]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 480), "Br: " + str(c24[4]), (0,0,0), None, size=25)

            if l1c1 != None:
                font.render_to(screen, (260, 560), str(p11), (0,0,0), None, size=45)
                drawCardType(screen, font,(325, 565),l1c1)
                font.render_to(screen, (260, 610), "Wh: " + str(c11[0]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 640), "Bl: " + str(c11[1]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 670), "Gr: " + str(c11[2]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 700), "Rd: " + str(c11[3]), (0,0,0), None, size=25)
                font.render_to(screen, (260, 730), "Br: " + str(c11[4]), (0,0,0), None, size=25)
            if l1c2 != None:
                font.render_to(screen, (430, 560), str(p12), (0,0,0), None, size=45)
                drawCardType(screen, font,(490, 565),l1c2)
                font.render_to(screen, (430, 610), "Wh: " + str(c12[0]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 640), "Bl: " + str(c12[1]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 670), "Gr: " + str(c12[2]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 700), "Rd: " + str(c12[3]), (0,0,0), None, size=25)
                font.render_to(screen, (430, 730), "Br: " + str(c12[4]), (0,0,0), None, size=25)
            if l1c3 != None:
                font.render_to(screen, (600, 560), str(p13), (0,0,0), None, size=45)
                drawCardType(screen, font,(660, 565),l1c3)
                font.render_to(screen, (600, 610), "Wh: " + str(c13[0]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 640), "Bl: " + str(c13[1]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 670), "Gr: " + str(c13[2]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 700), "Rd: " + str(c13[3]), (0,0,0), None, size=25)
                font.render_to(screen, (600, 730), "Br: " + str(c13[4]), (0,0,0), None, size=25)
            if l1c4 != None:
                font.render_to(screen, (770, 560), str(p14), (0,0,0), None, size=45)
                drawCardType(screen, font,(830, 565),l1c4)
                font.render_to(screen, (770, 610), "Wh: " + str(c14[0]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 640), "Bl: " + str(c14[1]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 670), "Gr: " + str(c14[2]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 700), "Rd: " + str(c14[3]), (0,0,0), None, size=25)
                font.render_to(screen, (770, 730), "Br: " + str(c14[4]), (0,0,0), None, size=25)
            #Noble info draw
            font.render_to(screen, (1005, 155), str(pn1), (0,0,0), None, size=45)
            font.render_to(screen, (1005, 190), "Wh: " + str(cn1[0]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 210), "Bl: " + str(cn1[1]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 230), "Gr: " + str(cn1[2]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 250), "Rd: " + str(cn1[3]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 270), "Br: " + str(cn1[4]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 355), str(pn2), (0,0,0), None, size=45)
            font.render_to(screen, (1005, 390), "Wh: " + str(cn2[0]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 410), "Bl: " + str(cn2[1]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 430), "Gr: " + str(cn2[2]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 450), "Rd: " + str(cn2[3]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 470), "Br: " + str(cn2[4]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 555), str(pn3), (0,0,0), None, size=45)
            font.render_to(screen, (1005, 590), "Wh: " + str(cn3[0]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 610), "Bl: " + str(cn3[1]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 630), "Gr: " + str(cn3[2]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 650), "Rd: " + str(cn3[3]), (0,0,0), None, size=25)
            font.render_to(screen, (1005, 670), "Br: " + str(cn3[4]), (0,0,0), None, size=25)

            #UE(USER ERROR) HAPPENED
            if invalid:
                pg.draw.rect(screen, (255,255,255), Rect(10, 10, 1280, 1380))
                font.render_to(screen, (375, 150), "!!!INVALID MOVE!!!", (255,0,0), None, size=60)
                pg.draw.rect(screen, (255,0,0), Rect(350, 350, 600, 300))
                font.render_to(screen, (500, 500), "CONFIRM.", (0,0,0), None, size=60)

            #Draw Help Button
            pg.draw.rect(screen, (255,165,0), Rect(150, 5, 40, 40))
            font.render_to(screen, (155, 17.5), "Help", (0,0,0), None, size=15)

            if help == True:
                pg.draw.rect(screen, (100,100,100), Rect(5, 5, 1290, 700))
                pg.draw.rect(screen, (255,0,0), Rect(10, 10, 40, 40))
                font.render_to(screen, (15, 15), "X", (100,0,0), None, size=45)
                font.render_to(screen, (75, 15), "How to play:", (255,0,0), None, size=45)
                font.render_to(screen, (75, 65), "On your turn you can:", (100,0,0), None, size=45)
                font.render_to(screen, (75, 115), "- Take 3 gem tokens of different colors.", (100,0,0), None, size=45)
                font.render_to(screen, (75, 165), "- Take 2 gem tokens of the same color.", (100,0,0), None, size=45)

                font.render_to(screen, (75, 215), "- Reserve 1 development card and take 1 gold token", (100,0,0), None, size=45)
                font.render_to(screen, (75, 265), "- Purchase 1 face-up development card from the middle", (100,0,0), None, size=45)
                font.render_to(screen, (75, 315), "  of the table or a previously reserved one.", (100,0,0), None, size=45)




            pg.display.flip()

    #0 = white   1 = blue   2 = green   3 - red   4 - brown
    
def drawCardType(screen,font,coords,card):
        if card.getCardType() == 0:
            font.render_to(screen, coords, "White", (255,255,255), None, size=25)
        elif card.getCardType() == 1:
            font.render_to(screen, coords, "Blue", (2,13,227), None, size=25)
        elif card.getCardType() == 2:
            font.render_to(screen, coords, "Green", (1,54,2), None, size=25)
        elif card.getCardType() == 3:
            font.render_to(screen, coords, "Red", (255,0,0), None, size=25)
        elif card.getCardType() == 4:
            font.render_to(screen, coords, "Brown", (92,64,51), None, size=25)
# Startup the main method to get things going.
if __name__ == "__main__":
    game = Main()
    game.main()
    pg.quit()
