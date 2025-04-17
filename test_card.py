import unittest
from card import Card
import pygame as pg

class testCards(unittest.TestCase):
    pg.init()
    screen = pg.display.set_mode([1300, 1400])

    #Tests to see if getCords returns the card's coords.
    def test_getCords(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        cords = k.getCords()
        self.assertEqual(cords[0],k.rect.x)
        self.assertEqual(cords[1],k.rect.y)       

    #Tests if update moves the x if only x is given.
    def test_update1(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        k.update(4)
        self.assertEqual(k.rect.x,4)
        self.assertEqual(k.rect.y,0)

    #Tests if update moves the x and y if both are given.
    def test_update2(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        k.update(5,7)
        self.assertEqual(k.rect.x,5)
        self.assertEqual(k.rect.y,7)

    def test_move(self):
        k = Card((122,456),0,1,1,1,1,0,0,1)
        k.move(0,0)
        self.assertEqual(k.rect.x,0)
        self.assertEqual(k.rect.y,0)

    #Tests to see if getPoints properly returns card point value.
    def test_getPoints(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        points = k.getPoints()
        self.assertEqual(points,0)
    
    """
    #Tests to see if the setPoints method sets it's points to given value.
    def test_setPoints(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        k.setPoints(5)
        self.assertEqual(k.getPoints(),5)
    """

    #Tests to see if getCardType properly returns the card's type.
    def test_getCardType(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        type = k.getCardType()
        self.assertEqual(type,0)

    #Tests to see if getCost properly returns a list of the costs of each type.
    def test_getCost(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        cost = k.getCost()
        self.assertEqual(cost,[0,1,1,1,1])

    #Tests tp see of setCost properly sets the cost of each type.
    def test_setCost(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        k.setCost(1,2,3,4,5)
        self.assertEqual(k.getCost(),[1,2,3,4,5])

    def test_flip(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        k.flip(100,100)
        self.assertEqual(k.rect.x,100)
        self.assertEqual(k.rect.y,100)

    def test_getLvl(self):
        k = Card((0,0),0,1,1,1,1,0,0,1)
        self.assertEqual(k.getLvl(),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)