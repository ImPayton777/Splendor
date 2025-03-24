import os
import pygame as pg

class Card(pg.sprite.Sprite):

    #Type codes: 0 = White, 1 = Blue, 2 = Green, 3 = Red, 4 = Brown
    tokenType = 0
    #Advancement points
    points = 0
    #Card level
    level = 1
    #Cost of each type
    whiteCost = 0
    blueCost = 0
    greenCost = 0
    redCost = 0
    brownCost = 0

    #creates a card
    def __init__(self, coord, white, blue, green, red, brown, points, gem, lvl):
        super(Card, self).__init__()
        self.whiteCost = white
        self.blueCost = blue
        self.greenCost = green
        self.redCost = red
        self.brownCost = brown
        self.points = points
        if lvl == 1:
            self.image = pg.image.load(os.path.join('assets', 'lvl1Card.png')).convert_alpha()
        elif lvl == 2:
            self.image = pg.image.load(os.path.join('assets', 'lvl2Card.png')).convert_alpha()
        elif lvl == 3:
            self.image = pg.image.load(os.path.join('assets', 'lvl3Card.png')).convert_alpha()
        else:
            raise ValueError("Not a card level")
        self.tokenType = gem
        self.lvl = lvl
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    #draws a card
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #For removing a card from the deck
    def flip(self, deltax, deltay = 0):
        #save current coords and change image and hitbox
        x = self.rect.x
        y = self.rect.y
        if lvl == 1:
            self.image = pg.image.load(os.path.join('assets', 'lvl1CardBack.png')).convert_alpha()
        elif lvl == 2:
            self.image = pg.image.load(os.path.join('assets', 'lvl2CardBack.png')).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join('assets', 'lvl3CardBack.png')).convert_alpha()
        self.rect = self.image.get_rect()
        #Reset coords and move(flip card)
        self.rect.x = x
        self.rect.y = y
        self.rect.x += deltax
        self.rect.y += deltay

    #moves a card by delta
    def update(self, deltax, deltay = 0):
        self.rect.x += deltax
        self.rect.y += deltay

    #a getter for then point value of a card
    def getPoints(self):
        return self.points

    #a setter and getter for the cost of a card
    def setCost(self, white, blue, green, red, brown):
        self.whiteCost = white
        self.blueCost = blue
        self.greenCost = green
        self.redCost = red
        self.brownCost = brown

    def getCost(self):
        return [self.whiteCost, self.blueCost, self.greenCost, self.redCost, self.brownCost]

    def getCardType(self):
        return self.tokenType
