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
        self.clicked = False

    def changeImage(self, img):
        self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def collide(self):
        if self.isHoveredOn == False:
            self.selected = SelectedTile(self.game, self)
            self.isHoveredOn = True

    def update(self):
        if self.isHoveredOn == False and self.selected != None:
            self.selected.kill()

    def drawQuestions(self):
        if self.text:
            self.game.renderText(self.text, self.x, self.y)
            pass

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

    def collide(self):
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

class Shotgun(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.shotgunImage
        img = game.shotgunImage
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = 2 * self.game.tilesizeWidth
        self.y = 8 * self.game.tilesizeHeight
        self.rect = self.image.get_rect()

class CountdownTimer(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.countdownIconImages[0]
        img = game.countdownIconImages[0]
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = 36 * self.game.tilesizeWidth
        self.y = 1 * self.game.tilesizeHeight
        self.rect = self.image.get_rect()
        self.startTime = pg.time.get_ticks()
        self.lastUpdate = pg.time.get_ticks()
        self.tenthOfTime = TRIGGER_HAPPY_QUESTION_TIME / 10

    def update(self):
        timeRunning = pg.time.get_ticks() - self.startTime
        if int(timeRunning/1000) > TRIGGER_HAPPY_QUESTION_TIME:
            self.game.round.generateQuestion()
            self.startTime = pg.time.get_ticks()
            self.lastUpdate = pg.time.get_ticks()
            self.tenthOfTime =  TRIGGER_HAPPY_QUESTION_TIME / 10

        if timeRunning/1000 > self.tenthOfTime:
            self.tenthOfTime += TRIGGER_HAPPY_QUESTION_TIME / 10
            img = self.game.countdownIconImages[int(self.tenthOfTime / TRIGGER_HAPPY_QUESTION_TIME * 10) - 2]
            self.originalImage = img
            self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

class correctIncorrectHUD(pg.sprite.Sprite):
    def __init__(self, game, answerResult):
        self._layer = 3
        self.groups = game.all_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.currImage = 0
        if answerResult == "correct":
            self.originalImage = game.correctImages[self.currImage]
            img = game.correctImages[self.currImage]
            self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = 10 * self.game.tilesizeWidth
        self.y = 10 * self.game.tilesizeHeight
        self.rect = self.image.get_rect()
        self.lastUpdate = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.lastUpdate > CORRECT_UPDATE_ANIM:
            self.lastUpdate = pg.time.get_ticks()
            self.currImage += 1
            self.currImage = self.currImage % len(self.game.correctImages)
            img = self.game.correctImages[self.currImage]
            self.originalImage = img
            self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))
