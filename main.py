# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import sys
from settings import *
from sprites import *
from question import *
from category import *
from os import path
from os import listdir
from round import *

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.categories = {}
        self.load_data()
        self.tilesizeWidth = 32
        self.tilesizeHeight = 32
        self.scaleWidth = 1
        self.scaleHeight = 1
        self.fromOriginalWidth = 1
        self.fromOriginalHeight = 1
        #self.testViewAllQuestions()
        self.myfont = pg.font.SysFont("Roman", 20)

    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.loadQuestions()
        self.loadImages()

    def loadImages(self):
        img_folder = path.join(self.game_folder, 'images')
        self.questionTileImage = pg.image.load(path.join(img_folder, QUESTION_TILE)).convert_alpha()
        self.selectedTimeImage = pg.image.load(path.join(img_folder, SELECTED_TILE_IMAGE)).convert_alpha()
        self.longQuestionTileImage = pg.image.load(path.join(img_folder, LONG_QUESTION_TILE)).convert_alpha()

    def testViewAllQuestions(self):
        for category in self.categories.values():
            for difficultyLevel in category.questions:
                for question in category.questions[difficultyLevel]:
                    print(question.question)
                    print(question.answer)
                    print(question.options)

    def loadQuestions(self):
        questionsPath = path.join(self.game_folder, "questions")
        files = listdir(questionsPath)
        for file in files:
            categoryName = file.split(".")[0] #science.txt becomes sciene
            if (ISCATEGORYENABLED[categoryName]):
                newCategory = Category(categoryName)
                self.categories[categoryName] = newCategory
                f = open(path.join(questionsPath, file),'r')
                for question in f:
                    newCategory.addQuestionToCategory(question)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.questionTiles = pg.sprite.Group()
        self.scalable = pg.sprite.Group()
        self.collidable_sprites = pg.sprite.Group()
        self.round = Round(self)
        self.screenWidth = 1280   # 16 * 64 or 32 * 32 or 64 * 16
        self.screenHeight = 768  # 16 * 48 or 32 * 24 or 64 * 12
        self.player = Player(self, 0, 0)
        self.mouse = Sprite_Mouse_Location(0, 0, self)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.mouse.rect.x, self.mouse.rect.y = pg.mouse.get_pos()
        self.mouse.x, self.mouse.y =  pg.mouse.get_pos()
        self.all_sprites.update()
        self.round.update()

    def draw_grid(self):
        for x in range(0, self.screenWidth, int(self.tilesizeWidth)):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, self.screenHeight))
        for y in range(0, self.screenHeight, int(self.tilesizeHeight)):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (self.screenWidth, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.x, sprite.y))
        for question in self.questionTiles:
            question.drawQuestions()
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def adjustResolution(self):
        SCALE_FACTOR_WIDTH = 2

    def events(self):
        # catch all events here
        for sprite in self.collidable_sprites:
            if pg.sprite.collide_rect(sprite, self.mouse):
                sprite.collide()
            else:
                sprite.isHoveredOn = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_F1:
                    if (SETTINGS["ISFULLSCREEN"] == True):
                        #if fullscreen set to window
                        print("Entering Windowed mode")
                        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))
                        SETTINGS["ISFULLSCREEN"] = False
                    else:
                        print("Entering Fullscreen mode")
                        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight), pg.FULLSCREEN)
                        SETTINGS["ISFULLSCREEN"] = True
                if event.key == pg.K_F2:
                    self.changeResolution(RESOLUTIONS[0])
                if event.key == pg.K_F3:
                    self.changeResolution(RESOLUTIONS[1])
                if event.key == pg.K_F9:
                    self.round.generateQuestion()

    def changeResolution(self, resolution):
        print("Setting resolution to " +  str(resolution))
        self.fromOriginalWidth = resolution[0]/WIDTH
        self.fromOriginalHeight = resolution[1]/HEIGHT
        self.scaleWidth = resolution[0]/self.screenWidth
        self.scaleHeight = resolution[1]/self.screenHeight
        self.scaleSelf()
        self.changeScreenSize()
        self.scaleObjects()

    def scaleObjects(self):
        for object in self.scalable:
            object.x = object.x * self.scaleWidth
            object.y = object.y * self.scaleHeight
            newWidth = int(object.image.get_width()  * self.scaleWidth)
            newHeight = int(object.image.get_height() * self.scaleHeight)
            object.image = pg.transform.scale(object.originalImage, (newWidth, newHeight))
            object.rect = object.image.get_rect()
            object.rect.x = object.x
            object.rect.y = object.y

    def changeScreenSize(self):
        self.screenWidth = self.screenWidth * self.scaleWidth
        self.screenHeight = self.screenHeight * self.scaleHeight
        self.screenWidth = int(self.screenWidth)
        self.screenHeight = int(self.screenHeight)
        if (SETTINGS["ISFULLSCREEN"]):
            self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight), pg.FULLSCREEN)
        else:
            self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))

    def scaleSelf(self):
        self.tilesizeWidth = self.tilesizeWidth * self.scaleWidth
        self.tilesizeHeight = self.tilesizeHeight * self.scaleHeight

    def renderText(self, text, x, y):
        levelText = self.myfont.render("{}".format(text), False, (0, 0, 0))
        self.screen.blit(levelText, (x, y))

class Sprite_Mouse_Location(pg.sprite.Sprite):
    def __init__(self,x,y, game):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x,y,1,1)
        self.x = self.rect.x
        self.y = self.rect.y

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
