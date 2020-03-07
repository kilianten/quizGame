import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class QuestionTile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.questionTiles, game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.questionTileImage
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def scale(self):
        self.x = self.x * self.game.scaleWidth
        self.y = self.y * self.game.scaleHeight
        newWidth = int(self.image.get_width()  * self.game.scaleWidth)
        newHeight = int(self.image.get_height() * self.game.scaleHeight)
        self.image = pg.transform.scale(self.image, (newWidth, newHeight))
        self.rect = self.image.get_rect()
