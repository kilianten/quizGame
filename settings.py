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

CATEGORIES = ["science", "geography", "history"]
ISCATEGORYENABLED = {"science" : True, "geography" : True, "history" : True}

QUESTIONFOLDER = "questions"
LINESPLITTER = "|"

SETTINGS = {"ISFULLSCREEN":False}

DIFFICULTYLEVELS = ['1', '2', '3', '4', '5']

RESOLUTIONS = [(1920, 1080), (1280, 768)]


#IMAGES
QUESTION_TILE = "metaltile.png"
SELECTED_TILE_IMAGE = "boxOutline.png"
LONG_QUESTION_TILE = "questionTile.png"
CORRECT_TILE = "metalTileCorrect.png"
INCORRECT_TILE = "metalTileIncorrect.png"
SHOTGUN_IMAGE = "shotgun.png"
COUNTDOWN_ICON_IMAGES = ["countdownICON01.png", "countdownICON02.png", "countdownICON03.png", "countdownICON04.png", "countdownICON05.png", "countdownICON06.png", "countdownICON07.png", "countdownICON08.png", "countdownICON09.png", "countdownICON10.png"]
