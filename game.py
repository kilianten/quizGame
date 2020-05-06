from sprites import *
from settings import *
from module import *
from random import choice, randint


class Game(Module):
    def __init__(self, game, screen):
        super().__init__(game)
        self.screen = screen
        self.answerSelected = False
        self.correctText = None
        self.selectedTile = None
        self.tiles = []
        self.timer = None

    def update(self):
        if not self.answerSelected:
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
                    tile.clicked = False
        else:
            self.checkReset()

    def checkKeyDownEvent(self, event):
        if event.key == pg.K_ESCAPE:
            self.game.changeModule(self.game.mainMenu)

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

    def createSprites(self):
        self.createQuestionTiles()
        self.createLongQuestionTile()
        self.questions = self.game.categories
        self.generateQuestion()
        self.shotgun = Shotgun(self.game)
        self.timer = CountdownTimer(self.game)

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

    def createQuestionTiles(self):
        self.killAllObjects()
        self.bottomLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 20)
        self.bottomRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 20)
        self.topLeft = QuestionTile(self.game, self.game.tilesizeWidth * 2, self.game.tilesizeHeight * 16)
        self.topRight = QuestionTile(self.game, self.game.tilesizeWidth * 21, self.game.tilesizeHeight * 16)
        self.tiles = [self.bottomLeft, self.bottomRight, self.topLeft, self.topRight]
        self.timer = CountdownTimer(self.game)

    def createRandomCharacter(self, male=None):
        male = choice([True, False])
        male = True #TBR
        person = self.createPerson(male)
        return person

    def createPerson(self, male):
        if(male):
            name = choice(MALE_NAMES)
            hair, hairImage = choice(list(MALE_HAIRSTYLES.items()))
            if(hair in self.game.loadedPeopleImages):
                hair = self.game.loadedPeopleImages[hair]
            else:
                image = self.game.loadImage(hairImage)
                self.game.loadedPeopleImages[hair] = image
                hair = image
        person = Person(name, self.game, self)
        person.setHair(hair)
        return person

class StandardGameMode(Game):
    def __init__(self, game, screen, numberOfBots, roundsEnabled, customCharacters):
        super().__init__(game, screen)
        self.numberOfBots = numberOfBots
        self.numberOfPlayersAlive = numberOfBots + 1
        self.contestants = customCharacters
        numberOfBotsToCreate = numberOfBots - len(self.contestants)
        while(numberOfBotsToCreate > 0):
            self.contestants.append(self.createRandomCharacter())
            numberOfBotsToCreate -= 1
        round = choice(self.game.options.roundsEnabled)
        if(round == "Trigger Happy"):
            self.round = RoundTriggerHappy(self.game, self.contestants)

class Round:
    def __init__(self, game, contestants):
        self.game = game
        self.contestants = contestants

class RoundTriggerHappy(Round):
    def __init__(self, game, contestants):
        super().__init__(game, contestants)

class Person:
    def __init__(self, name, game, quizGame):
        self.name = name
        self.game = game
        self.quizGame = quizGame

    def setHair(self, hair):
        self.hair = BodyPart(self.game, hair, self.quizGame)
