"""
@author Jordan Dubreuil
Unit testing for the BattleShip Game checkHitOrMiss Function
"""

from Battleship import checkHitOrMiss
import unittest

class TestCheckHitOrMiss(unittest.TestCase):
    def test_hit(self):
        myBoard = [['.', '.', '.', '.'], ['.', 'S', '.', '.'], ['.', '.', '.', '.']]
        self.assertEqual(checkHitOrMiss(myBoard, 1, 1), "Hit")
        self.assertEqual(myBoard, [['.', '.', '.', '.'], ['.', 'X', '.', '.'], ['.', '.', '.', '.']])

    def test_miss(self):
        myBoard = [['.', '.', '.', '.'], ['.', 'S', '.', '.'], ['.', '.', '.', '.']]
        self.assertEqual(checkHitOrMiss(myBoard, 0, 0), "Miss")
        self.assertEqual(myBoard, [['O', '.', '.', '.'], ['.', 'S', '.', '.'], ['.', '.', '.', '.']])

    def test_already_hit(self):
        myBoard = [['.', '.', '.', '.'], ['.', 'S', '.', '.'], ['.', '.', '.', '.']]
        myBoard[1][1] = "X"
        self.assertEqual(checkHitOrMiss(myBoard, 1, 1), "Hit")
        self.assertEqual(myBoard, [['.', '.', '.', '.'], ['.', 'X', '.', '.'], ['.', '.', '.', '.']])