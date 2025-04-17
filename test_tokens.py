import unittest
from tokens import Tokens
import pygame as pg

class testTokens(unittest.TestCase):
    pg.init()
    screen = pg.display.set_mode([1300, 1400])
    
    #Tests to see if the initial gem type is the one inputted (0).
    def test_gem1(self):
        x = Tokens((0,0),0)
        self.assertEqual(x.tokenType,0)

    #Tests to see if the initial gem type is the one inputted (1).
    def test_gem2(self):
        x = Tokens((0,0),1)
        self.assertEqual(x.tokenType,1)

    #Tests to see if the initial gem type is the one inputted (2).
    def test_gem3(self):
        x = Tokens((0,0),2)
        self.assertEqual(x.tokenType,2)

    #Tests to see if the initial gem type is the one inputted (3).
    def test_gem4(self):
        x = Tokens((0,0),3)
        self.assertEqual(x.tokenType,3)

    #Tests to see if the initial gem type is the one inputted (4).
    def test_gem5(self):
        x = Tokens((0,0),4)
        self.assertEqual(x.tokenType,4)

    #Tests to see if the initial gem type is the one inputted (4).
    def test_gem6(self):
        x = Tokens((0,0),5)
        self.assertEqual(x.tokenType,5)

    #Tests to see if getType() properly returns the gem type.
    def test_getType(self):
        x = Tokens((0,0),3)
        self.assertEqual(x.getType(),3)

    #Tests if setType sets the gem type correctly.
    def test_setType(self):
        x = Tokens((0,0),0)
        x.setType(2)
        self.assertTrue(x.tokenType,2)

    #Tests if update moves the x if only x is given.
    def test_update1(self):
        k = Tokens((0,0),0)
        k.update(4)
        self.assertEqual(k.rect.x,4)
        self.assertEqual(k.rect.y,0)

    #Tests if update moves the x and y if both are given.
    def test_update2(self):
        k = Tokens((0,0),0)
        k.update(5,7)
        self.assertEqual(k.rect.x,5)
        self.assertEqual(k.rect.y,7)

    def test_move(self):
        k = Tokens((122,412),0)
        k.move(0,0)
        self.assertEqual(k.rect.x,0)
        self.assertEqual(k.rect.y,0)

if __name__ == '__main__':
    unittest.main(verbosity=2)