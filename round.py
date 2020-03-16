import pygame as pg
from sprites import *
from settings import *
from random import choice

class Round:

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

    def createQuestionTiles(self):
        self.bottomLeft = QuestionTile(self.game, 64, 640)
        self.bottomRight = QuestionTile(self.game, 672, 640)
        self.topLeft = QuestionTile(self.game, 64, 512)
        self.topRight = QuestionTile(self.game, 672, 512)
        self.tiles = [self.bottomLeft, self.bottomRight, self.topLeft, self.topRight]

    def createLongQuestionTile(self):
        self.longQuestionTile = LongQuestionTile(self.game, 64, 384)

    def createSelectedTile(self):
        self.selectedTile = SelectedTile(self.game, self.topLeft)

    def generateQuestion(self):
        self.question = None;

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


    def update(self):
        for tile in self.tiles:
            if tile.clicked:
                if tile.text == self.question.answer:
                    newImage = self.game.correctQuestionTileImage
                    tile.changeImage(newImage)
                else:
                    newImage = self.game.incorrectQuestionTileImage
                    tile.changeImage(newImage)
                tile.clicked = False

class TriggerHappy(Round):
    def __init__(self, game, screen):
        super().__init__(game, screen)
        self.createQuestionTiles()
        self.createLongQuestionTile()
        self.questions = game.categories
        self.generateQuestion()
        self.shotgun = Shotgun(self.game)
        self.timer = CountdownTimer(self.game)

    def draw(self):
        pass
