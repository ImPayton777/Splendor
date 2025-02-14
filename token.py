import os
import pygame as pg

class Token(pg.sprite.Sprite):

    #Type codes: 0 = White, 1 = Blue, 2 = Green, 3 = Red, 4 = Brown
    tokenType = 0
    #creates a token
    def __init__(self, coord):
        super(Token, self).__init__()

    #draws a token
    def draw(self, screen):

    #sets type of gem
    def setType(self, gem):
        tokenType = gem
