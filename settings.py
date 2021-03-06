import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

HAIR_COLORS = [(190, 123, 22), (170,136,102),(83, 61, 53), (99, 79, 79)]

# game settings
WIDTH = 1280   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

CATEGORIES = ["science", "geography", "history", "entertainment", "misc", "dictionary"]
ISCATEGORYENABLED = {"science" : True, "geography" : True, "history" : True, "entertainment" : True, "misc":True, "dictionary":True}

QUESTIONFOLDER = "questions"
LINESPLITTER = "|"

SETTINGS = {"ISFULLSCREEN":False}

DIFFICULTYLEVELS = ['1', '2', '3', '4', '5']

RESOLUTIONS = [(1920, 1080), (1280, 768), (1440, 900)]

TRIGGER_HAPPY_STARTING_DEATH_CHANCE = 100 #1 in a thousand
TRIGGER_HAPPY_QUESTION_TIME = 15 #MILIS 20 seconds
SHOTGUN_ROTATE_SPEED = .3
SHOTGUN_ROTATE_ANGLE = 15
TIME_BEFORE_NEW_QUESTION = 3
CORRECT_UPDATE_ANIM = 100 #millisecs
RESET_TIME = 3000 # millisecs

#IMAGES
QUESTION_TILE = "metaltile.png"
SELECTED_TILE_IMAGE = "boxOutline.png"
LONG_QUESTION_TILE = "questionTile.png"
CORRECT_TILE = "metalTileCorrect.png"
INCORRECT_TILE = "metalTileIncorrect.png"
SHOTGUN_IMAGE = "shotgun.png"
COUNTDOWN_ICON_IMAGES = ["countdownICON001.png", "countdownICON002.png", "countdownICON003.png", "countdownICON004.png", "countdownICON005.png", "countdownICON006.png", "countdownICON007.png", "countdownICON008.png", "countdownICON009.png", "countdownICON010.png"]
CORRECT_IMAGES = ["correct1.png", "correct2.png", "correct3.png", "correct4.png", "correct5.png", "correct6.png"]
MENU_TILES = ["menuTile001.png", "menuTile002.png", "menuTile003.png", "menuTile004.png", "menuTile005.png" ,"menuTile006.png", "menuTile007.png", "menuTile008.png", "menuTile009.png", "menuTile010.png", "menuTile011.png", "menuTile012.png", "menuTile013.png", "menuTile014.png"]
ARROW_RIGHT = "arrowRight.png"
ARROW_RIGHT_HOVER = "arrowRightHover.png"
SHOTFACE_IMAGE = "shotFace.png"
NAME_TILE = "namePanel.png"
LARGE_PANEL_IMAGE = "largePanel.png"
CONTESTANT_BACKGROUND_IMAGE = "ContestantBackground.png"

#PRIEST IMAGES
PRIEST_IMAGE = "priestIdle.png"

#MAIN MENU
NEW_GAME_TEXT = "NEW GAME"
EXIT_GAME_TEXT = "EXIT"
CUSTOM_CHARACTER_TEXT = "CHARACTER CREATION"
MAIN_MENU_UPDATE_ANIM = 17

DEFAULT_XPADDING = 15
DEFAULT_YPADDING = 15

#CHARACTERS
MALE_HEADS = {"01":"head0002.png"}
MALE_HAIRSTYLES = {"tidy_brown":"hair0001.png", "tidy_red":"hair0001_red.png", "tidy_blone":"hair0001_blonde.png", "tidy_black":"hair0001_black.png", "tidy_fair":"hair0001_fair.png",  "posh_fair":"hair0002_fair.png", "posh_brown":"hair0002_brown.png", "posh_black":"hair0002_black.png", "posh_blonde":"hair0002_blonde.png", "posh_red":"hair0002_red.png", "balding_brown":"hair0003_brown.png", "balding_black":"hair0003_black.png", "balding_blonde":"hair0003_blonde.png", "balding_grey":"hair0003_grey.png"}


MALE_BODIES = {"WHITE_V_NECK":"body0001.png"}

EYES = {"Alert":"eyes0001.png"}
NOSES = {"The Pointer":"nose0001.png", "The ShadowMaker":"nose0002.png"}
EARS = {"default":"ear001.png"}

#names
MALE_NAMES = ["Kilian", "Thomas", "Ian", "Stephen", "Paul", "Sean", "Johnny", "Paddy", "Patrick", "Thom", "Ros", "Brendan", "Rick", "Richard", "Carl", "Karl", "Brian", "David", "Dave", "Peter", "Mark", "Greg", "Owen", "Eoin", "Fergus", "Niall", "Jack", "Jake", "Darragh", "Oliver", "Bill"]
