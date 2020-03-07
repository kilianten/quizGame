from sprites import QuestionTile

class Round:

    def __init__(self, game):
        self.game = game
        self.createQuestionTiles()

    def createQuestionTiles(self):
        QuestionTile(self.game, 0, 0)
