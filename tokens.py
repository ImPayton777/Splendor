import os
import pygame as pg

class Tokens(pg.sprite.Sprite):

    #Type codes: 0 = White, 1 = Blue, 2 = Green, 3 = Red, 4 = Brown
    tokenType = 0
    #creates a token
    def __init__(self, coord, gem):
        super(Tokens, self).__init__()
        if gem == 0:
            self.image = pg.image.load(os.path.join('assets', 'whiteToken.png')).convert_alpha()
        elif gem == 1:
            self.image = pg.image.load(os.path.join('assets', 'blueToken.png')).convert_alpha()
        elif gem == 2:
            self.image = pg.image.load(os.path.join('assets', 'greenToken.png')).convert_alpha()
        elif gem == 3:
            self.image = pg.image.load(os.path.join('assets', 'redToken.png')).convert_alpha()
        elif gem == 4:
            self.image = pg.image.load(os.path.join('assets', 'brownToken.png')).convert_alpha()
        elif gem == 5:
            self.image = pg.image.load(os.path.join('assets', 'goldToken.png')).convert_alpha()
        else:
            raise ValueError("Not a gem type")
        self.tokenType = gem
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    #draws a token
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #sets type of gem
    def setType(self, gem):
        self.tokenType = gem

    #getter for gemType
    def getType(self):
        return self.tokenType

    #moves a token
    def update(self, deltax, deltay = 0):
        self.rect.x += deltax
        self.rect.y += deltay

    #moves token to x,y
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
