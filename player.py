import os
import pygame as pg

class Player(pg.sprite.Sprite):

    #total points between Nobles and cards
    totalPoints = 0
    #lists of tokens and cards in the player's inventory
    tokens = []
    crads = []
    #total units of each gem type(cards+tokens)
    whiteCurrency = 0
    blueCurrency = 0
    greenCurrency = 0
    redCurrency = 0
    brownCurrency = 0

    #creates a player
    def __init__(self, coord):
        super(Player, self).__init__()

    #draws a player's inventory
    def draw(self, screen):
