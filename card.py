import os
import pygame as pg

class Card(pg.sprite.Sprite):

    #Type codes: 0 = White, 1 = Blue, 2 = Green, 3 = Red, 4 = Brown
    tokenType = 0
    #Advancement points
    points = 0
    #Cost of each type
    whiteCost = 0
    blueCost = 0
    greenCost = 0
    redCost = 0
    brownCost = 0

    #creates a crad
    def __init__(self, coord):
        super(Card, self).__init__()

    #draws a card
    def draw(self, screen):

    #a setter and getter for then point value of a card
    def setPoints(self, points):

    def getPoints(self):
        return points

    #a setter and getter for the cost of a card
    def setCost(self, white, blue, green, red, brown):

    def getCost(self):

