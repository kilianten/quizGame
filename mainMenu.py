from sprites import MainMenuTile
from settings import *

class mainMenu:
    def __init__(self, game):
        self.game = game
        self.sprites = game.menu_sprites
        self.newGameTile = MainMenuTile(game, 11 * game.tilesizeWidth, game.tilesizeHeight * 6, NEW_GAME_TEXT)
        self.customChar = MainMenuTile(game, 11 * game.tilesizeWidth, game.tilesizeHeight * 12, CUSTOM_CHARACTER_TEXT)
        self.exitGameTile = MainMenuTile(game, 11 * game.tilesizeWidth, game.tilesizeHeight * 18, EXIT_GAME_TEXT)

    def update(self):
        self.sprites.update()
        if self.newGameTile.clicked:
            self.game.texts = self.game.game_texts
            self.game.current_sprites = self.game.game_sprites
            self.game.collidables = self.game.collidable_sprites
        if self.customChar.clicked:
            self.game.texts = self.game.createChar_texts
            self.game.current_sprites = self.game.createChar_sprites
            self.game.collidables = self.game.createChar_collidable_sprites
        if self.exitGameTile.clicked:
            self.game.quit()
