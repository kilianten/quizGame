import pygame as pg

class Module:
    def __init__(self, game):
        self.game = game
        self.components = {"sprites": pg.sprite.LayeredUpdates(), "texts":pg.sprite.Group(), "collidables": pg.sprite.Group()}

    def draw(self):
        pass
