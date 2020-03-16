import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1280   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

CATEGORIES = ["science", "geography", "history", "entertainment"]
ISCATEGORYENABLED = {"science" : True, "geography" : True, "history" : True, "entertainment" : True}

QUESTIONFOLDER = "questions"
LINESPLITTER = "|"

SETTINGS = {"ISFULLSCREEN":False}

DIFFICULTYLEVELS = ['1', '2', '3', '4', '5']

RESOLUTIONS = [(1920, 1080), (1280, 768)]

TRIGGER_HAPPY_QUESTION_TIME = 10 #MILIS 20 seconds
TIME_BEFORE_NEW_QUESTION = 3
CORRECT_UPDATE_ANIM = 100 #millisecs

#IMAGES
QUESTION_TILE = "metaltile.png"
SELECTED_TILE_IMAGE = "boxOutline.png"
LONG_QUESTION_TILE = "questionTile.png"
CORRECT_TILE = "metalTileCorrect.png"
INCORRECT_TILE = "metalTileIncorrect.png"
SHOTGUN_IMAGE = "shotgun.png"
COUNTDOWN_ICON_IMAGES = ["countdownICON001.png", "countdownICON002.png", "countdownICON003.png", "countdownICON004.png", "countdownICON005.png", "countdownICON006.png", "countdownICON007.png", "countdownICON008.png", "countdownICON009.png", "countdownICON010.png"]
CORRECT_IMAGES = ["correct1.png", "correct2.png", "correct3.png", "correct4.png", "correct5.png", "correct6.png"]
