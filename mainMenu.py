from sprites import MainMenuTile
from settings import *
from module import *
from game import StandardGameMode

class mainMenu(Module):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if self.newGameTile.clicked:
            try:
                self.game.quizGame.kill()
            except:
                pass
            self.game.quizGame = StandardGameMode(self.game, self.game.screen, self.game.options.numberOfBots, self.game.options.roundsEnabled, self.game.options.customerCharacters)
            self.game.quizGame.createSprites()
            self.game.changeModule(self.game.quizGame)
            self.newGameTile.clicked = False
        if self.customChar.clicked:
            self.game.changeModule(self.game.createChar)
            self.customChar.clicked = False
        if self.exitGameTile.clicked:
            self.game.quit()

    def checkKeyDownEvent(self, event):
        if event.key == pg.K_ESCAPE:
            self.game.quit()

    def createSprites(self):
        self.newGameTile = MainMenuTile(self.game, 11 * self.game.tilesizeWidth, self.game.tilesizeHeight * 6, NEW_GAME_TEXT)
        self.customChar = MainMenuTile(self.game, 11 * self.game.tilesizeWidth, self.game.tilesizeHeight * 12, CUSTOM_CHARACTER_TEXT)
        self.exitGameTile = MainMenuTile(self.game, 11 * self.game.tilesizeWidth, self.game.tilesizeHeight * 18, EXIT_GAME_TEXT)
