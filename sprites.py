import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.game_sprites
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
        self.groups = game.game_texts, game.game_sprites, game.scalable, game.collidable_sprites
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
        self.xPadding = DEFAULT_XPADDING
        self.yPadding = DEFAULT_YPADDING

    def changeImage(self, img):
        self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def collide(self):
        if self.isHoveredOn == False:
            self.selected = SelectedTile(self.game, self)
            self.isHoveredOn = True

    def update(self):
        if self.isHoveredOn == False and self.selected != None:
            self.selected.kill()

    def drawText(self):
        if self.text:
            self.game.renderText(self.text, self.x, self.y, self)
            pass

class LongQuestionTile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.game_texts, game.game_sprites, game.scalable
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
        self.xPadding = DEFAULT_XPADDING
        self.yPadding = DEFAULT_YPADDING

    def drawText(self):
        if self.text:
            self.game.renderText(self.text, self.x, self.y, self)
            pass

    def collide(self):
        pass

class SelectedTile(pg.sprite.Sprite):
    def __init__(self, game, questionTile):
        self._layer = 3
        self.groups = game.game_sprites, game.scalable
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
        self.groups = game.game_sprites, game.scalable
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
        self.groups = game.game_sprites, game.scalable
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
        self.answerSelected = False
        self.finished = False

    def update(self):
        if not self.answerSelected:
            timeRunning = pg.time.get_ticks() - self.startTime
            if int(timeRunning/1000) > TRIGGER_HAPPY_QUESTION_TIME:
                self.finished = True
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
        self.groups = game.game_sprites, game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.currImage = 0
        if answerResult == "correct":
            self.originalImage = game.correctImages[self.currImage]
            img = game.correctImages[self.currImage]
            self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = 10 * self.game.tilesizeWidth
        self.y = 2 * self.game.tilesizeHeight
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

class MainMenuTile(pg.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self._layer = 2
        self.groups = game.menu_sprites, game.scalable, game.menu_collidable_sprites, game.menu_texts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.menuTiles[0]
        img = game.menuTiles[0]
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.isHoveredOn = False
        self.selected = None
        self.text = text
        self.clicked = False
        self.currImage = 0
        self.animating = False
        self.xPadding = DEFAULT_XPADDING
        self.yPadding = DEFAULT_YPADDING

    def changeImage(self, img):
        self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def collide(self):
        if self.isHoveredOn == False:
            self.selected = True
            self.isHoveredOn = True
            self.animating = True
            self.lastUpdate = pg.time.get_ticks()

    def update(self):
        self.game.renderText(self.text, 1, 1)
        if self.isHoveredOn == False and self.selected != True:
            self.selected = False
        if self.animating == True and pg.time.get_ticks() - self.lastUpdate > MAIN_MENU_UPDATE_ANIM:
            self.lastUpdate = pg.time.get_ticks()
            self.currImage += 1
            self.currImage = self.currImage % len(self.game.menuTiles)
            img = self.game.menuTiles[self.currImage]
            self.originalImage = img
            self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))
            if self.currImage == len(self.game.menuTiles) - 1:
                self.animating = False


    def drawText(self):
        self.game.renderText(self.text, self.x, self.y, self)

class ArrowRightIcon(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.createChar_sprites, game.scalable, game.createChar_collidable_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.originalImage = game.arrowRightImage
        img = self.originalImage
        self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.isHoveredOn = False
        self.clicked = False

    def changeImage(self, img):
        self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def collide(self):
        if self.isHoveredOn == False:
            self.isHoveredOn = True
            img = self.game.arrowRightHoverImage
            self.originalImage = img
            self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def update(self):
        if self.isHoveredOn == False and self.originalImage == self.game.arrowRightHoverImage:
            img = self.game.arrowRightImage
            self.originalImage = img
            self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))
