# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_game_is_valid(self):
        new_game = Game()
        new_game.grid = list('LYDPUZZLE')
        self.assertIs(new_game.is_valid('PUZZLEDLY'), True)
        self.assertEqual(new_game.grid, list('LYDPUZZLE'))

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('TIALUCRIC')
        self.assertIs(new_game.is_valid('EVANOUIRA'), False)
        self.assertEqual(new_game.grid, list('TIALUCRIC'))

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW')
        self.assertIs(new_game.is_valid('FEUN'), False)
