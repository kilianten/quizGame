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

CATEGORIES = ["science", "Geography"]
ISCATEGORYENABLED = {"science" : True, "geography" : True}

QUESTIONFOLDER = "questions"
LINESPLITTER = "|"

SETTINGS = {"ISFULLSCREEN":False}

RESOLUTIONS = [(1920, 1080), (1280, 768)]

#IMAGES
QUESTION_TILE = "metaltile.png"
SELECTED_TILE_IMAGE = "boxOutline.png"
