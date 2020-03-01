from question import *

class Category:

    def __init__(self, name):
        self.name = name
        self.questions = {'1':[], '2':[], '3':[], '4':[], '5':[]}

    def addQuestionToCategory(self, line):
        newQuestion = Question(line)
        self.questions[newQuestion.difficulty].append(newQuestion)
