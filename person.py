from random import choice, randint
from settings import *
from sprites import BodyPart

class Person:
    def __init__(self, game, male, quizGame):
        self.game = game
        self.isMale = male
        self.quizGame = quizGame

    def makeRandom(self):
        self.name = choice(MALE_NAMES if self.isMale else None)
        self.getRandomHair()
        self.getRandomEyes()
        self.getRandomNose()
        headImage = self.game.loadImage(MALE_HEADS["01"])  #TBC
        self.head = BodyPart(self.game, headImage, 2)
        self.body = [self.hair, self.head, self.eyes, self.nose]

    def getRandomHair(self):
        hairStyles = MALE_HAIRSTYLES if self.isMale else None
        hair, hairImage = choice(list(hairStyles.items()))
        hair = self.checkIsImageAlreadyLoaded(hair, hairImage)
        tintImage = hair.convert_alpha()
        tintImage.fill(choice(HAIR_COLORS), special_flags=pg.BLEND_ADD)
        self.hair = BodyPart(self.game, tintImage, 3)

    def getRandomEyes(self):
        eyes, eyeImage = choice(list(EYES.items()))
        eyes = self.checkIsImageAlreadyLoaded(eyes, eyeImage)
        self.eyes = BodyPart(self.game, eyes, 4)


    def getRandomNose(self):
        nose, noseImage = choice(list(NOSES.items()))
        nose = self.checkIsImageAlreadyLoaded(nose, noseImage)
        self.nose = BodyPart(self.game, nose, 3)

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

    def removeAsCurrentPlayer(self):
        for bodyPart in self.body:
            self.quizGame.components["sprites"].remove(bodyPart)
