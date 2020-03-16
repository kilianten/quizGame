import pygame as pg
from sprites import *
from settings import *
from random import choice

class Round:

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.answerSelected = False
        self.correctText = None
        self.selectedTile = None
        self.tiles = []
        self.timer = None

    def createQuestionTiles(self):
        self.killAllObjects()
        self.bottomLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 20)
        self.bottomRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 20)
        self.topLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 16)
        self.topRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 16)
        self.tiles = [self.bottomLeft, self.bottomRight, self.topLeft, self.topRight]

    def createLongQuestionTile(self):
        self.longQuestionTile = LongQuestionTile(self.game, 64, 384)

    def createSelectedTile(self):
        self.selectedTile = SelectedTile(self.game, self.topLeft)

    def generateQuestion(self):
        self.question = None;
        self.createQuestionTiles()
        self.answerSelected = False

        while self.question == None:
            randomCategory = choice(CATEGORIES)
            category = self.questions[randomCategory]
            difficulty = choice(DIFFICULTYLEVELS)
            if category.questions[difficulty]:
                self.question = choice(category.questions[difficulty])
        self.drawQuestion(self.question)

    def drawQuestion(self, question):
        self.longQuestionTile.text = question.question
        tileTemp = []
        for tile in self.tiles:
            tile.text = None
            tileTemp.append(tile)
        optionsTemp = []
        for option in  question.options:
            optionsTemp.append(option)
        optionsTemp.append(question.answer)
        while optionsTemp:
            option = choice(optionsTemp)
            tile = choice(tileTemp)
            tile.text = option
            tileTemp.remove(tile)
            optionsTemp.remove(option)

    def checkReset(self):
        if pg.time.get_ticks() - self.lastUpdate > RESET_TIME:
            self.lastUpdate = 0
            self.generateQuestion()

    def update(self):
        if not self.answerSelected:
            for tile in self.tiles:
                if tile.clicked:
                    self.answerSelected = True
                    self.lastUpdate = pg.time.get_ticks()
                    if tile.text == self.question.answer:
                        newImage = self.game.correctQuestionTileImage
                        tile.changeImage(newImage)
                        self.correctText = correctIncorrectHUD(self.game, "correct")
                    else:
                        newImage = self.game.incorrectQuestionTileImage
                        tile.changeImage(newImage)
                    tile.clicked = False
        else:
            self.checkReset()

    def killAllObjects(self):
        objects = [self.correctText, self.selectedTile, self.timer]
        for tile in self.tiles:
            objects.append(tile.selected)
            objects.append(tile)

        for object in objects:
            try:
                object.kill()
            except:
                pass

class TriggerHappy(Round):
    def __init__(self, game, screen):
        super().__init__(game, screen)
        self.createQuestionTiles()
        self.createLongQuestionTile()
        self.questions = game.categories
        self.generateQuestion()
        self.shotgun = Shotgun(self.game)
        self.timer = CountdownTimer(self.game)

    def update(self):
        super().update()
        if self.timer.finished == True:
            self.generateQuestion()

    def generateQuestion(self):
        super().generateQuestion()
        try:
            self.timer.kill()
        except:
            pass
        self.timer = CountdownTimer(self.game)
