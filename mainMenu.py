from sprites import MainMenuTile
from settings import *

class mainMenu:
    def __init__(self, game):
        self.game = game
        self.sprites = game.menu_sprites
        self.newGameTile = MainMenuTile(game, 11 * game.tilesizeWidth, game.tilesizeHeight * 6, NEW_GAME_TEXT)

    def update(self):
        self.sprites.update()
