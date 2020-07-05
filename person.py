from random import choice, randint
from settings import *
from sprites import BodyPart

class Person:
    def __init__(self, game, male, quizGame):
        self.game = game
        self.isMale = male
        self.quizGame = quizGame
        self.isDead = False
        self.isBot = False

    def makeRandom(self):
        self.name = choice(MALE_NAMES if self.isMale else None)
        self.getRandomHair()
        self.getRandomEyes()
        self.getRandomNose()
        self.getRandomEars()
        self.getRandomBody()
        headImage = self.game.loadImage(MALE_HEADS["01"])  #TBC
        self.head = BodyPart(self.game, headImage, 3)
        self.body = [self.hair, self.head, self.eyes, self.nose, self.ears, self.body]

    def getRandomHair(self):
        hairStyles = MALE_HAIRSTYLES if self.isMale else None
        hair, hairImage = choice(list(hairStyles.items()))
        hair = self.checkIsImageAlreadyLoaded(hair, hairImage)
        #tintImage = hair.convert_alpha()
        #tintImage.fill(choice(HAIR_COLORS), special_flags=pg.BLEND_ADD)
        self.hair = BodyPart(self.game, hair, 4)

    def getRandomEyes(self):
        eyes, eyeImage = choice(list(EYES.items()))
        eyes = self.checkIsImageAlreadyLoaded(eyes, eyeImage)
        self.eyes = BodyPart(self.game, eyes, 5)

    def getRandomEars(self):
        ears, earImage = choice(list(EARS.items()))
        ears = self.checkIsImageAlreadyLoaded(ears, earImage)
        self.ears = BodyPart(self.game, ears, 5)

    def getRandomNose(self):
        nose, noseImage = choice(list(NOSES.items()))
        nose = self.checkIsImageAlreadyLoaded(nose, noseImage)
        self.nose = BodyPart(self.game, nose, 4)

    def getRandomBody(self):
        body, bodyImage = choice(list(MALE_BODIES.items()))
        body = self.checkIsImageAlreadyLoaded(body, bodyImage)
        self.body = BodyPart(self.game, body, 4)

    def checkIsImageAlreadyLoaded(self, imageName, image):
        if(imageName in self.game.loadedPeopleImages):
            image = self.game.loadedPeopleImages[imageName]
        else:
            image = self.game.loadImage(image)
            self.game.loadedPeopleImages[imageName] = image
        return image

    def setToCurrentPlayer(self):
        for bodyPart in self.body:
            self.quizGame.components["sprites"].add(bodyPart)

    def scaleDownToFitPanel(self):
        for bodyPart in self.body:
            bodyPart.scaleDownToFitPanel()

    def removeAsCurrentPlayer(self):
        for bodyPart in self.body:
            self.quizGame.components["sprites"].remove(bodyPart)
        self.quizGame.round.nameTile.text = None

    def scalePlayer(self):
        for bodyPart in self.body:
            bodyPart.scale(bodyPart.image)
            self.quizGame.components["sprites"].add(bodyPart)

    def setX(self, x):
        for bodyPart in self.body:
            bodyPart.x = x

    def setY(self, y):
        for bodyPart in self.body:
            bodyPart.y = y

    def resetState(self):
        for bodyPart in self.body:
            bodyPart.y = 0
            bodyPart.setImage(bodyPart.originalImage)
            bodyPart.x = 13 * self.game.tilesizeWidth

    def guessCorrectAnswer(self):
        chance = choice([1, 2, 3, 4, 5, 6])
        if chance == 1:
            return False
        else:
            return True
