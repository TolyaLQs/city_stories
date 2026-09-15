import pygame as pg
from ..objects.player import Player
from ..worlds.worlds import World
from .pause import Pause

class Game:
    def __init__(self):
        self.game_state = 'play' # 'play' or 'pause'
        self.worlds = World()
        self.player = Player()
        self.pause = Pause()
        self.run_cycles = True

    def handle_event(self, event):
        pass

    def new_game(self):
        pass

    def update(self):
        if self.pause.pause_active == True:
            self.game_state = 'pause'
        else:
            self.game_state = 'play'
        if self.game_state == 'play':
            self.worlds.update()
            self.player.update()
        else:
            self.pause.update()

    def draw(self, screen):
        if self.game_state == 'play':
            self.worlds.draw(screen)
            self.player.draw(screen)
        else:
            self.pause.draw(screen)

    def game_cycles(self, screen, fps):
        while self.run_cycles:
            self.update()
            self.draw(screen)

