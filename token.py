import os
import pygame as pg

class Token(pg.sprite.Sprite):

    #Type codes: 0 = White, 1 = Blue, 2 = Green, 3 = Red, 4 = Brown
    tokenType = 0
    #creates a token
    def __init__(self, coord, gem):
        super(Token, self).__init__()
        if gem == 0:                                                                         self.image = pg.image.load(os.path.join('assets', 'whiteToken.png')).convert_alpha()
        elif gem == 1:
            self.image = pg.image.load(os.path.join('assets', 'blueToken.png')).convert_alpha()
        elif gem == 2:
            self.image = pg.image.load(os.path.join('assets', 'greenToken.png')).convert_alpha()
        elif gem == 3:
            self.image = pg.image.load(os.path.join('assets', 'redToken.png')).convert_alpha()
        elif gem == 4:
            self.image = pg.image.load(os.path.join('assets', 'brownToken.png')).convert_alpha()
        else:
            raise ValueError("Not a gem type")
        self.tokenType = gem

    #draws a token
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #sets type of gem
    def setType(self, gem):
        self.tokenType = gem
