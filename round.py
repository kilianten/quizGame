import pygame as pg
from sprites import QuestionTile
from sprites import SelectedTile
from sprites import LongQuestionTile
from settings import *
from random import choice

class Round:

    def __init__(self, game):
        self.game = game
        self.createQuestionTiles()
        self.createLongQuestionTile()
        self.questions = game.categories
        self.generateQuestion()

    def createQuestionTiles(self):
        self.bottomLeft = QuestionTile(self.game, 64, 608)
        self.bottomRight = QuestionTile(self.game, 672, 608)
        self.topLeft = QuestionTile(self.game, 64, 464)
        self.topRight = QuestionTile(self.game, 672, 464)
        self.tiles = [self.bottomLeft, self.bottomRight, self.topLeft, self.topRight]

    def createLongQuestionTile(self):
        self.longQuestionTile = LongQuestionTile(self.game, 64, 340)

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
