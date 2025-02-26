import unittest
from tokens import Tokens
import pygame as pg

class testMain(unittest.TestCase):
    pg.init()
    screen = pg.display.set_mode([1300, 1400])
    
    #Tests to see if the initial gem type is the one inputted (0)
    def test_gem1(self):
        x = Tokens((0,0),0)
        self.assertEqual(x.tokenType,0)

    #Tests to see if the initial gem type is the one inputted (1)
    def test_gem2(self):
        x = Tokens((0,0),1)
        self.assertEqual(x.tokenType,1)

    #Tests to see if the initial gem type is the one inputted (2)
    def test_gem3(self):
        x = Tokens((0,0),2)
        self.assertEqual(x.tokenType,2)

    #Tests to see if the initial gem type is the one inputted (3)
    def test_gem4(self):
        x = Tokens((0,0),3)
        self.assertEqual(x.tokenType,3)

    #Tests to see if the initial gem type is the one inputted (4)
    def test_gem5(self):
        x = Tokens((0,0),4)
        self.assertEqual(x.tokenType,4)

    #Tests if setType sets the gem type correctly.
    def test_setType(self):
        x = Tokens((0,0),0)
        x.setType(2)
        self.assertTrue(x.tokenType,2)

    #Tests if update moves the x if only x is given.
    def test_update1(self):
        k = Tokens((0,0),0)
        x = k.rect.x
        y = k.rect.y
        k.update(4)
        self.assertEqual(k.rect.x,x+4)
        self.assertEqual(k.rect.y,y)

    #Tests if update moves the x and y if both are given.
    def test_update2(self):
        k = Tokens((0,0),0)
        x = k.rect.x
        y = k.rect.y
        k.update(5,7)
        self.assertEqual(k.rect.x,x+5)
        self.assertEqual(k.rect.y,y+7)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

#x = Tokens((0,0),0)