import pygame as pg
from sprites import QuestionTile
from sprites import SelectedTile
from settings import WIDTH

class Round:

    def __init__(self, game):
        self.game = game
        self.createQuestionTiles()

    def createQuestionTiles(self):
        self.bottomLeft = QuestionTile(self.game, 64, 608)
        self.bottomRight = QuestionTile(self.game, 672, 608)
        self.topLeft = QuestionTile(self.game, 64, 464)
        self.bottomRight = QuestionTile(self.game, 672, 464)

    def createSelectedTile(self):
        self.selectedTile = SelectedTile(self.game, self.topLeft)

    def update(self):
        pass
