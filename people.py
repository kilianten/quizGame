class Person:
    def __init__(self, name, game):
        self.name = name
        self.game = game

class Priest(Person):
    def __init__(self, name, game):
        self.name = name
        self.game = game
    self.groups = game.players, game.scalable
    pg.sprite.Sprite.__init__(self, self.groups)
    self.originalImage = game.selectedTimeImage
    img = game.selectedTimeImage
    self.image = pg.transform.scale(img, (int(img.get_width() * game.fromOriginalWidth), int(img.get_height() * game.fromOriginalHeight)))
    self.x = questionTile.x
    self.y = questionTile.y
    self.rect = self.image.get_rect()
