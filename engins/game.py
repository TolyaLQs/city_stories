import pygame as pg


class Game:
    def __init__(self, new_game: bool = True):
        self.game_state = 'play' # 'play' or 'pause'
