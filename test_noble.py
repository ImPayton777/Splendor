import os
import pygame as pg
import unittest
from noble import Noble

class testNobles(unittest.TestCase):
    pg.init()
    screen = pg.display.set_mode([1300, 1400])

    #Tests to see if getCords properly returns a list of a noble's cords.
    def test_getCords(self):
        n = Noble((100,150),0,0,4,4,0,3)
        self.assertEqual(n.getCords(),[100,150])
    
    #Tests if update moves the x if only x is given.
    def test_update1(self):
        n = Noble((100,150),0,0,4,4,0,3)
        n.update(4)
        self.assertEqual(n.rect.x,104)
        self.assertEqual(n.rect.y,150)

    #Tests if update moves the x and y if both are given.
    def test_update2(self):
        n = Noble((100,150),0,0,4,4,0,3)
        n.update(5,7)
        self.assertEqual(n.rect.x,105)
        self.assertEqual(n.rect.y,157)

    #Tests to see if getPoints properly returns noble's point value.
    def test_getPoints(self):
        n = Noble((100,150),0,0,4,4,0,3)
        points = n.getPoints()
        self.assertEqual(points,3)

    #Tests to see if the setPoints method sets it's points to given value.
    def test_setPoints(self):
        n = Noble((100,150),0,0,4,4,0,3)
        n.setPoints(5)
        self.assertEqual(n.getPoints(),5)

    #Tests to see if getCost properly returns a list of the cost of each gem type.
    def test_getCost(self):
        n = Noble((100,150),0,0,4,4,0,3)
        self.assertEqual(n.getCost(),[0,0,4,4,0])

    #Tests if setCost properly sets the cost of the noble when given specific values.
    def test_setCost(self):
        n = Noble((100,150),0,0,4,4,0,3)
        n.setCost(1,2,3,4,5)
        self.assertEqual(n.getCost(),[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main(verbosity=2)