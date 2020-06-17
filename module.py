import pygame as pg

class Module:
    def __init__(self, game):
        self.paused = False
        self.game = game
        self.components = {"sprites": pg.sprite.LayeredUpdates(), "texts":pg.sprite.Group(), "collidables": pg.sprite.Group(), "timers":[]}
        self.tempTexts = []

    def draw(self):
        pass

    def killAll(self, component):
        for object in component:
            object.kill()
