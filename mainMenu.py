from sprites import MainMenuTile

class mainMenu:
    def __init__(self, game):
        self.game = game
        self.sprites = game.menu_sprites
        self.newGameTile = MainMenuTile(game, 0, 0)

    def update(self):
        pass
