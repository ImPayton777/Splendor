import os
import pygame as pg

class Noble(pg.sprite.Sprite):
    def __init__(self, coord, white, blue, green, red, brown, points):
        super(Noble, self).__init__()
        self.whiteCost = white
        self.blueCost = blue
        self.greenCost = green
        self.redCost = red
        self.brownCost = brown
        self.points = points
        self.image = pg.image.load(os.path.join('assets', 'nobleCard.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def getCords(self):
        return [self.rect.x, self.rect.y]

    def update(self, deltax, deltay = 0):
        self.rect.x += deltax
        self.rect.y += deltay

    def getPoints(self):        
        return self.points

    def setPoints(self, points):
        self.points = points

    def getCost(self):
        return [self.whiteCost, self.blueCost, self.greenCost, self.redCost, self.brownCost]

    def setCost(self, white, blue, green, red, brown):
        self.whiteCost = white
        self.blueCost = blue
        self.greenCost = green
        self.redCost = red
        self.brownCost = brown
