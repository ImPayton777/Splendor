import os
import pygame as pg
from card import Card
from tokens import Tokens

class Player():

    #total points between Nobles and cards
    totalPoints = 0
    #lists of tokens and cards in the player's inventory
    whitetokens = []
    bluetokens = []
    greentokens = []
    redtokens = []
    browntokens = []
    cards = []
    #total units of each gem type(cards+tokens)
    whiteCards = 0
    whiteTokens = 0
    blueCards = 0
    blueTokens = 0
    greenCards = 0
    greenTokens = 0
    redCards = 0
    redTokens = 0
    brownCards = 0
    brownTokens = 0

    #creates a player
    def __init__(self):
        #total points between Nobles and cards
        self.totalPoints = 0
        #lists of tokens and cards in the player's inventory
        self.whitetokens = []
        self.bluetokens = []
        self.greentokens = []
        self.redtokens = []
        self.browntokens = []
        self.cards = []
        #total units of each gem type(cards+tokens)
        self.whiteCards = 0
        self.whiteTokens = 0
        self.blueCards = 0
        self.blueTokens = 0
        self.greenCards = 0
        self.greenTokens = 0
        self.redCards = 0
        self.redTokens = 0
        self.brownCards = 0
        self.brownTokens = 0

    #Give player a card 
    def buyCard(self, card):
        cost = card.getCost()
        returns = []
        if(cost[0] - self.whiteCards > 0):
            i = cost[0] - self.whiteCards
            self.whiteTokens -= i
            while i > 0:
                returns.append(self.whitetokens.pop())
                i -= 1
        if(cost[1] - self.blueCards > 0):
            i = cost[1] - self.blueCards
            self.blueTokens -= i
            while i > 0:
                returns.append(self.bluetokens.pop())
                i -= 1
        if(cost[2] - self.greenCards > 0):
            i = cost[2] - self.greenCards
            self.greenTokens -= i
            while i > 0:
                returns.append(self.greentokens.pop())
                i -= 1
        if(cost[3] - self.redCards > 0):
            i = cost[3] - self.redCards
            self.redTokens -= i
            while i > 0:
                returns.append(self.redtokens.pop())
                i -= 1
        if(cost[4] - self.brownCards > 0):
            i = cost[4] - self.brownCards
            self.brownTokens -= i
            while i > 0:
                returns.append(self.browntokens.pop())
                i -= 1
        self.totalPoints += card.getPoints()
        i = card.getCardType()
        if i == 0:
            self.whiteCards += 1
        if i == 1:
            self.blueCards += 1
        if i == 2:
            self.greenCards += 1
        if i == 3:
            self.redCards += 1
        if i == 4:
            self.brownCards += 1
        self.cards.append(card)
        return returns

    #Give player tokens
    def takeToken(self, tokenns):
        for token in tokenns:
            i = token.getType()
            if i == 0:
                self.whiteTokens += 1
                self.whitetokens.append(token)
            if i == 1:
                self.blueTokens += 1
                self.bluetokens.append(token)
            if i == 2:
                self.greenTokens += 1
                self.greentokens.append(token)
            if i == 3:
                self.redTokens += 1
                self.redtokens.append(token)
            if i == 4:
                self.brownTokens += 1
                self.browntokens.append(token)

    #Player returns tokens
    def returnTokens(self, tokenns):
        for token in tokenns:
            i = token.getType()
            if i == 0:
                self.whiteTokens -= 1
                self.whitetokens.pop()
            if i == 1:
                self.blueTokens -= 1
                self.bluetokens.pop()
            if i == 2:
                self.greenTokens -= 1
                self.greentokens.pop()
            if i == 3:
                self.redTokens -= 1
                self.redtokens.pop()
            if i == 4:
                self.brownTokens -= 1
                self.browntokens.pop()


    #returns currency in a list [white, blue, green, red, brown]
    def getCurrency(self):
        return [self.whiteCards+self.whiteTokens, self.blueCards+self.blueTokens, self.greenCards+self.greenTokens, self.redCards+self.redTokens, self.brownCards+self.brownTokens]

    def getTotalPoints(self):
        return self.totalPoints

    #returns card counts of player
    def getCards(self):
        return [self.whiteCards, self.blueCards, self.greenCards, self.redCards, self.brownCards]

    #returns token counts of player
    def getTokens(self):
        return [self.whiteTokens, self.blueTokens, self.greenTokens, self.redTokens, self.brownTokens]
