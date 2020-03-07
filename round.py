from sprites import QuestionTile
from settings import WIDTH

class Round:

    def __init__(self, game):
        self.game = game
        self.createQuestionTiles()

    def createQuestionTiles(self):
        self.bottomLeft = QuestionTile(self.game, 64, 592)
        self.bottomRight = QuestionTile(self.game, 672, 592)
        self.topLeft = QuestionTile(self.game, 64, 432)
        self.bottomRight = QuestionTile(self.game, 672, 432)
