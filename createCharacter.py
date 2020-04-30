from sprites import ArrowRightIcon
from settings import *

class createChar:
    def __init__(self, game):
        self.game = game
        self.rightArrow = ArrowRightIcon(game, 0, 0)
        print()

    def update(self):
        pass

    def checkKeyDownEvent(self, event):
        if event.key == pg.K_ESCAPE:
            print("test")
            self.game.module = self.game.mainMenu
            self.game.texts = self.game.menu_texts
            self.game.current_sprites = self.game.menu_sprites
            self.game.collidables = self.game.menu_collidable_sprites
