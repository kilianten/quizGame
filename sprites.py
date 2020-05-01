import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.quizGame.components["sprites"]
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
        self.groups = game.quizGame.components["texts"], game.quizGame.components["sprites"], game.scalable, game.quizGame.components["collidables"]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        setImage(self, game.questionTileImage)
        self.x = x
        self.y = y
        setRect(self)
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
        self.groups = game.quizGame.components["texts"], game.quizGame.components["sprites"], game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        setImage(self, game.longQuestionTileImage)
        self.x = x
        self.y = y
        setRect(self)
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
        self.groups = game.quizGame.components["sprites"], game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        setImage(self, game.selectedTimeImage)
        self.x = questionTile.x
        self.y = questionTile.y
        self.rect = self.image.get_rect()

class Shotgun(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.quizGame.components["sprites"], game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        setImage(self, game.shotgunImage)
        self.x = 2 * self.game.tilesizeWidth
        self.y = 8 * self.game.tilesizeHeight
        self.rect = self.image.get_rect()

class CountdownTimer(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.quizGame.components["sprites"], game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        setImage(self, game.countdownIconImages[0])
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
                setImage(self, self.game.countdownIconImages[int(self.tenthOfTime / TRIGGER_HAPPY_QUESTION_TIME * 10) - 2])

class Animation(pg.sprite.Sprite):
    def __init__(self, game, images, updateRate, startImage=0, startAnimating=False):
        self.game = game
        self.currImage = startImage
        self.lastUpdate = pg.time.get_ticks()
        self.images = images
        setImage(self, game.correctImages[startImage])
        self.updateRate = updateRate
        self.animating = startAnimating

    def update(self):
        if pg.time.get_ticks() - self.lastUpdate > self.updateRate:
            self.lastUpdate = pg.time.get_ticks()
            self.currImage += 1
            self.currImage = self.currImage % len(self.images)
            setImage(self, self.images[self.currImage])

class correctIncorrectHUD(Animation):
    def __init__(self, game, answerResult):
        super().__init__(game, game.correctImages, CORRECT_UPDATE_ANIM)
        self._layer = 3
        self.groups = game.quizGame.components["sprites"], game.scalable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = 10 * self.game.tilesizeWidth
        self.y = 2 * self.game.tilesizeHeight
        self.rect = self.image.get_rect()

    def update(self):
        super().update()

class MainMenuTile(Animation):
    def __init__(self, game, x, y, text):
        super().__init__(game, game.menuTiles, MAIN_MENU_UPDATE_ANIM)
        self._layer = 2
        self.groups = game.mainMenu.components["sprites"], game.mainMenu.components["texts"], game.mainMenu.components["collidables"]
        pg.sprite.Sprite.__init__(self, self.groups)
        setImage(self, game.menuTiles[0])
        self.x = x
        self.y = y
        setRect(self)
        self.isHoveredOn = False
        self.selected = None
        self.text = text
        self.clicked = False
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
            if self.currImage == len(self.game.menuTiles) - 1:
                self.animating = False

    def drawText(self):
        self.game.renderText(self.text, self.x, self.y, self)

class ArrowRightIcon(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.game = game
        self.groups = game.createChar.components["sprites"], game.scalable, game.createChar.components["collidables"]
        pg.sprite.Sprite.__init__(self, self.groups)
        setImage(self, game.arrowRightImage)
        self.x = x
        self.y = y
        setRect(self)
        self.isHoveredOn = False
        self.clicked = False

    def changeImage(self, img):
        self.image = pg.transform.scale(img, (int(img.get_width() * self.game.fromOriginalWidth), int(img.get_height() * self.game.fromOriginalHeight)))

    def collide(self):
        if self.isHoveredOn == False:
            self.isHoveredOn = True
            setImage(self, self.game.arrowRightHoverImage)

    def update(self):
        if self.isHoveredOn == False and self.originalImage == self.game.arrowRightHoverImage:
            setImage(self, self.game.arrowRightImage)

def setImage(object, image):
    object.originalImage = image
    object.image = pg.transform.scale(image, (int(image.get_width() * object.game.fromOriginalWidth), int(image.get_height() * object.game.fromOriginalHeight)))

def setRect(object):
    object.rect = object.image.get_rect()
    object.rect.x = object.x
    object.rect.y = object.y
