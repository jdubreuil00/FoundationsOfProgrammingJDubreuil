"""
@author Jordan Dubreuil
Unit testing for the setupBoard function in BattleShip Game
"""

from Battleship import setupBoard
import unittest

class TestSetupBoard(unittest.TestCase):
    # Tests for number of ships on the game board in setupBoard
    def test_board_setup(self):
        thearray = [ ['']*10 for i in range(10) ]
        setupBoard(thearray)
        self.assertEqual(len(thearray), 10)
        self.assertEqual(len(thearray[0]), 10)
        self.assertEqual(len(thearray[1]), 10)
        self.assertEqual(len(thearray[2]), 10)
        self.assertEqual(len(thearray[3]), 10)
        num_of_ships = 5 # check for 5 ships
        num_of_ships_on_board = 0
        for row in thearray:
            for col in row:
                if col == "S":
                    num_of_ships_on_board += 1
        self.assertEqual(num_of_ships_on_board, num_of_ships)

    def test_board_setup_spaces(self):
        thearray = [ ['']*10 for i in range(10) ]
        num_of_ships = 5
        setupBoard(thearray)
        
        # check that there are 2 ships on the board
        num_of_ships_on_board = sum([row.count("S") for row in thearray])
        self.assertEqual(num_of_ships_on_board, num_of_ships)
        
        # check that the rest of the board is filled with blank spaces
        num_of_blank_spaces = sum([row.count(".") for row in thearray])
        expected_num_of_blank_spaces = len(thearray)**2 - num_of_ships_on_board
        self.assertEqual(num_of_blank_spaces, expected_num_of_blank_spaces)