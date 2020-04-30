from sprites import ArrowRightIcon
from settings import *
from module import *

class createChar(Module):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        pass

    def checkKeyDownEvent(self, event):
        if event.key == pg.K_ESCAPE:
            self.game.changeModule(self.game.mainMenu)

    def createSprites(self):
        self.rightArrow = ArrowRightIcon(self.game, 0, 0)
