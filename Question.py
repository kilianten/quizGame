from settings import LINESPLITTER

class Question:

    def __init__(self, line):
        data = line.split(LINESPLITTER)
        self.question = data[0]
        self.answer = data[1]
        self.options = []
        self.options.append(data[2])
        self.options.append(data[3])
        self.options.append(data[4])
        self.difficulty = data[5]
