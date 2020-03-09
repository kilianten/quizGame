import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = 0
        self.y = 0
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

    def update(self):
        pass

class QuestionTile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.questionTiles, game.all_sprites, game.scalable, game.collidable_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.questionTileImage
        img = game.questionTileImage
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.isHoveredOn = False
        self.selected = None
        self.text = None

    def collide(self):
        if self.isHoveredOn == False:
            self.selected = SelectedTile(self.game, self)
            self.isHoveredOn = True

    def update(self):
        print(self.text)
        if self.isHoveredOn == False and self.selected != None:
            self.selected.kill()

    def drawQuestions(self):
        if self.text:
            self.game.renderText(self.text, self.x, self.y)
            pass

    def printOption(self, option):
        self.text = option

class LongQuestionTile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.questionTiles, game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.longQuestionTileImage
        img = game.longQuestionTileImage
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = None

    def drawQuestions(self):
        if self.text:
            self.game.renderText(self.text, self.x, self.y)
            pass



class SelectedTile(pg.sprite.Sprite):
    def __init__(self, game, questionTile):
        self._layer = 3
        self.groups = game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.selectedTimeImage
        img = game.selectedTimeImage
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = questionTile.x
        self.y = questionTile.y
        self.rect = self.image.get_rect()
