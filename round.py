import pygame as pg
from sprites import QuestionTile
from sprites import SelectedTile
from settings import *
from random import choice

class Round:

    def __init__(self, game):
        self.game = game
        self.createQuestionTiles()
        self.questions = game.categories
        self.generateQuestion()

    def createQuestionTiles(self):
        self.bottomLeft = QuestionTile(self.game, 64, 608)
        self.bottomRight = QuestionTile(self.game, 672, 608)
        self.topLeft = QuestionTile(self.game, 64, 464)
        self.bottomRight = QuestionTile(self.game, 672, 464)

    def createSelectedTile(self):
        self.selectedTile = SelectedTile(self.game, self.topLeft)

    def generateQuestion(self):
        question = None;

        while question == None:
            randomCategory = choice(CATEGORIES)
            category = self.questions[randomCategory]
            difficulty = choice(DIFFICULTYLEVELS)
            if category.questions[difficulty]:
                question = choice(category.questions[difficulty])
        print(question.question)


    def update(self):
        pass
