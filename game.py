from sprites import *
from settings import *
from module import *
from person import *

class Game(Module):
    def __init__(self, game, screen):
        super().__init__(game)
        self.screen = screen

    def update(self):
        self.round.update()

    def checkKeyDownEvent(self, event):
        if event.key == pg.K_ESCAPE:
            self.game.changeModule(self.game.mainMenu)

    def createRandomCharacter(self, male=None):
        male = choice([True, False])
        male = True #TBC
        person = Person(self.game, male, self)
        person.makeRandom()
        return person

    def draw(self):
        self.round.draw()

class StandardGameMode(Game):
    def __init__(self, game, screen, numberOfBots, roundsEnabled, customCharacters):
        super().__init__(game, screen)
        self.numberOfBots = numberOfBots
        self.numberOfPlayersAlive = numberOfBots + 1
        self.contestants = list(customCharacters)
        numberOfBotsToCreate = numberOfBots - len(self.contestants)
        while(numberOfBotsToCreate > 0):
            self.contestants.append(self.createRandomCharacter())
            numberOfBotsToCreate -= 1
        round = choice(self.game.options.roundsEnabled)
        if(round == "Trigger Happy"):
            self.round = RoundTriggerHappy(self.game, self.contestants, self)

class Round:
    def __init__(self, game, contestants):
        self.game = game
        self.contestants = contestants

    def wrongAnswer(self):
        pass

    def changeToNextPlayer(self):
        index = self.contestants.index(self.currentPlayer)
        self.currentPlayer.removeAsCurrentPlayer()
        self.currentPlayer = self.contestants[(index + 1) % len(self.contestants)]
        self.currentPlayer.setToCurrentPlayer()

    def endRound(self):
        pass

class RoundTriggerHappy(Round):
    def __init__(self, game, contestants, quizGame):
        super().__init__(game, contestants)
        startingPlayer = choice(contestants)
        self.currentPlayer = startingPlayer
        startingPlayer.setToCurrentPlayer()
        self.chanceOfDeath = TRIGGER_HAPPY_STARTING_DEATH_CHANCE
        self.answerSelected = False
        self.correctText = None
        self.selectedTile = None
        self.tiles = []
        self.quizGame = quizGame
        self.timer = CountdownTimer(self.game, quizGame)
        self.createLongQuestionTile()
        self.questions = self.game.categories
        self.generateQuestion()
        self.shotgun = Shotgun(self.game, quizGame)

    def createQuestionTiles(self):
        self.killAllObjects()
        self.bottomLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 20, self.quizGame)
        self.bottomRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 20, self.quizGame)
        self.topLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 16, self.quizGame)
        self.topRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 16, self.quizGame)
        self.tiles = [self.bottomLeft, self.bottomRight, self.topLeft, self.topRight]
        self.timer = CountdownTimer(self.game, self.quizGame)

    def wrongAnswer(self):
        super().wrongAnswer()
        playerIsDead = self.isPlayerDead()
        if playerIsDead:
            self.killPlayer()
        else:
            pass

    def killPlayer(self):
        self.shotgun.rotationDegree = 0
        self.shotgun.rotating = True

    def isPlayerDead(self):
        self.chanceOfDeath
        randomNumber = randint(0, self.chanceOfDeath)
        if randomNumber == 0:
            return True
        else:
            self.chanceOfDeath -= randomNumber
            return False

    def draw(self):
        self.game.renderText("Chance Of Death: {}".format(self.chanceOfDeath), 10, 10)
        self.game.renderText("Currnt Player: {}".format(self.currentPlayer.name), 10, 30)

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

    def createLongQuestionTile(self):
        self.longQuestionTile = LongQuestionTile(self.game, 64, 384, self.quizGame)

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
            self.changeToNextPlayer()

    def update(self):
        if not self.answerSelected:
            self.checkIfAnswerIsCorrect()
        else:
            self.checkReset()

    def checkIfAnswerIsCorrect(self):
        for tile in self.tiles:
            if tile.clicked:
                self.answerSelected = True
                self.timer.answerSelected = True
                self.lastUpdate = pg.time.get_ticks()
                if tile.text == self.question.answer:
                    newImage = self.game.correctQuestionTileImage
                    tile.changeImage(newImage)
                    self.correctText = correctIncorrectHUD(self.game, "correct")
                else:
                    newImage = self.game.incorrectQuestionTileImage
                    tile.changeImage(newImage)
                    self.wrongAnswer()
                tile.clicked = False

    def endRound(self):
        print("test")
