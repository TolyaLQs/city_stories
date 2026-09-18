import pygame as pg


class Player:
    def __init__(self):
        self.hp = 100
        self.speed = 100
        self.pos = (0, 0)
        self.player_state = 'stop' # 'stop' or 'walking' or 'running'
        self.player_side = 'up' # 'up' or 'left' or 'right' or 'down'

    def update(self):
        pass

    def draw(self, screen):
        pass

