import unittest
from player import Player
from tokens import Tokens
from card import Card
from noble import Noble
import pygame as pg

class testPlayer(unittest.TestCase):
    pg.init()
    screen = pg.display.set_mode([1300, 1400])

    #Tests to see if getTotalPoints properly returns the amount of points a player has.
    def test_getTotalPoints(self):
        p = Player()
        p.totalPoints = 5
        points = p.getTotalPoints()
        self.assertEqual(points,5)

    #Test to see whether getCards properly returns a list of a count of each card type.
    def test_getCards(self):
        p = Player()
        p.whiteCards = 3
        p.blueCards = 0
        p.greenCards = 2
        p.redCards = 4
        p.brownCards = 1
        self.assertEqual(p.getCards(), [3,0,2,4,1])

    #Test to see whether getCurrency properly returns a list of the sum of cards and tokens of each type.
    def test_getCurrency(self):
        p = Player()
        p.whiteCards = 3
        p.blueCards = 0
        p.greenCards = 2
        p.redCards = 4
        p.brownCards = 1
        p.whiteTokens = 2
        p.blueTokens = 1
        p.greenTokens = 1
        p.redTokens = 1
        p.brownTokens = 4
        self.assertEqual(p.getCurrency(),[5,1,3,5,5])

    #Test if takeTokens properly gives the player tokens. Tests if the token values goes up and appends a token to the tokens list.
    #0 = white   1 = blue   2 = green   3 - red   4 - brown
    def test_takeToken(self):
        p = Player()
        shop = [Tokens((0,0),0),Tokens((0,0),2),Tokens((0,0),4)]
        p.takeToken(shop)
        self.assertEqual(p.whiteTokens,1)
        self.assertEqual(p.blueTokens,0)
        self.assertEqual(p.greenTokens,1)
        self.assertEqual(p.redTokens,0)
        self.assertEqual(p.brownTokens,1)
        self.assertEqual(p.whitetokens[0],shop[0])
        self.assertEqual(p.bluetokens,[])
        self.assertEqual(p.greentokens[0],shop[1])
        self.assertEqual(p.redtokens,[])
        self.assertEqual(p.browntokens[0],shop[2])

    #Tests to see if player buys card properly with only tokens.
    #0 = white   1 = blue   2 = green   3 - red   4 - brown
    def test_buyCard1(self):
        p = Player()
        t = [Tokens((0,0),0),Tokens((0,0),1),Tokens((0,0),1),Tokens((0,0),2),Tokens((0,0),3)]
        p.takeToken(t)
        card = Card((0,0), 1,2,1,1,0, 0,4,1)
        buy = p.buyCard(card)
        self.assertEqual(len(buy),5)
        self.assertEqual(p.getCurrency(),[0,0,0,0,1])
        self.assertEqual(p.cards,[card])
        self.assertEqual(p.getCards(),[0,0,0,0,1])
        self.assertEqual(p.getTokens(),[0,0,0,0,0])

    #Tests to see if player buys cards with cards already bought and some tokens.
    def test_buyCard2(self):
        p = Player()
        #3,2,2,0,1
        #0 = white   1 = blue   2 = green   3 - red   4 - brown
        t = [Tokens((0,0),0),Tokens((0,0),0),Tokens((0,0),0),Tokens((0,0),1),Tokens((0,0),1),Tokens((0,0),2),Tokens((0,0),2),Tokens((0,0),3),Tokens((0,0),4)]
        p.takeToken(t)
        #Red Card
        card = Card((0,0), 3,5,3,0,3, 3,3,3)
        p.cards.append(Card((0,0),1,0,1,1,1,0,1,1))
        p.cards.append(Card((0,0),1,1,1,1,1,0,1,1))
        p.cards.append(Card((0,0),1,1,1,1,1,0,1,1))
        p.cards.append(Card((0,0),1,1,0,1,1,0,2,1))
        p.cards.append(Card((0,0),1,1,1,1,1,0,4,1))
        p.cards.append(Card((0,0),1,1,0,1,1,0,4,1))
        p.blueCards += 3
        p.greenCards += 1
        p.brownCards += 2
        buy = p.buyCard(card)
        self.assertEqual(len(buy),8)
        self.assertEqual(p.getCurrency(),[0,3,1,2,2])
        self.assertEqual(p.cards[-1],card)
        self.assertEqual(p.getCards(),[0,3,1,1,2])
        self.assertEqual(p.getTokens(),[0,0,0,1,0])

    #Tests to see if getTokens properly returns a list of player tokens.
    def test_getTokens(self):
        p = Player()
        t = [Tokens((0,0),0),Tokens((0,0),1),Tokens((0,0),1),Tokens((0,0),2),Tokens((0,0),4)]
        p.takeToken(t)
        self.assertEqual(p.getTokens(),[1,2,1,0,1])

    #Tests to see if returnTokens properly removes tokens from the player's inventory.
    def test_returnTokens(self):
        p = Player()
        t = [Tokens((0,0),0),Tokens((0,0),1),Tokens((0,0),1),Tokens((0,0),2),Tokens((0,0),3)]
        p.takeToken(t)
        p.returnTokens(t)
        self.assertEqual(p.getTokens(),[0,0,0,0,0])
        self.assertEqual(p.whitetokens,[])
        self.assertEqual(p.bluetokens,[])
        self.assertEqual(p.greentokens,[])
        self.assertEqual(p.redtokens,[])
        self.assertEqual(p.browntokens,[])

    def test_checkNoble1(self):
        p = Player()
        #0 = white   1 = blue   2 = green   3 - red   4 - brown
        p.whiteCards = 4
        p.blueCards = 4
        p.greenCards = 0
        p.redCards = 3
        p.brownCards = 3
        nobles = [Noble((0,0),0,0,4,4,0,3),Noble((0,0),3,0,0,3,3,3),Noble((0,0),4,4,0,0,0,3)]
        self.assertEqual(p.checkNoble(nobles),[nobles[1],nobles[2]])
        self.assertEqual(len(p.nobles),2)
        self.assertEqual(p.getTotalPoints(),6)

    def test_checkNoble2(self):
        p = Player()
        p.whiteCards = 0
        p.blueCards = 0
        p.greenCards = 0
        p.redCards = 0
        p.brownCards = 0
        nobles = [Noble((0,0),0,0,4,4,0,3),Noble((0,0),3,0,0,3,3,3),Noble((0,0),4,4,0,0,0,3)]
        self.assertEqual(p.checkNoble(nobles),[])
        self.assertEqual(len(p.nobles),0)
        self.assertEqual(p.getTotalPoints(),0)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
