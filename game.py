# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string


class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters_list = self.grid.copy()
        for letter in word:
            if letter in letters_list:
                letters_list.remove(letter)
            else:
                return False
        return True
