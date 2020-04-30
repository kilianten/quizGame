from sprites import ArrowRightIcon
from settings import *

class createChar:
    def __init__(self, game):
        self.game = game
        self.rightArrow = ArrowRightIcon(game, 0, 0)
        print()

    def update(self):
        pass
