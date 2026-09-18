import pygame as pg
from objects.player import Player
from worlds.worlds import World
from worlds.camera import Camera
from .pause import Pause
import time

class Game:
    def __init__(self, screen_size):
        self.screen_w, self.screen_h = screen_size
        self.game_state = 'play' # 'play' or 'pause' or 'quit'
        self.worlds = World()
        self.player = Player()
        self.pause = Pause(screen_size)
        self.run_cycles = True
        self.clock = pg.Clock()
        self.font = pg.font.SysFont('Arial', 30)

    def handle_event(self, event):
        if self.game_state == 'play':
            self.handle_event_board(event)
        elif self.game_state == 'pause':
            self.pause.handle_event(event)

    def handle_event_board(self, event):
        pass

    def handle_event_mause(self, event):
        pass

    def new_game(self, screen):
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        screen.fill((20, 20, 30))
        pg.display.flip()
        label = self.font.render('Load new game ...', True, (255, 255, 255))
        rect = label.get_rect(center=(self.screen_w//2, self.screen_h//2))
        screen.blit(label, rect)
        pg.display.flip()
        print('load')
        self.worlds = World()
        self.worlds.create_world()
        self.camera = Camera(self.screen_w, self.screen_h)
        self.player = Player()
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))

    def load_game(self):
        pass

    def update(self):
        if self.pause.pause_active == True:
            self.game_state = 'pause'
        else:
            self.game_state = 'play'
        if self.game_state == 'play':
            self.worlds.update(self.player.pos, self.camera.rect)
            self.camera.update(self.player.pos)
            self.player.update()
        else:
            self.pause.update()
            if self.pause.pause_state == 'quit in menu':
                self.pause.pause_state = 'pause'
                self.run_cycles = False
            elif self.pause.pause_state == 'quit':
                self.game_state = 'quit'
                self.run_cycles = False

    def draw(self, screen):
        if self.game_state == 'play':
            self.worlds.draw(screen, self.camera.rect)
            self.player.draw(screen)
        else:
            self.pause.draw(screen)

    def game_cycles(self, screen, fps):
        while self.run_cycles:
            self.update()
            self.draw(screen)
            pg.display.flip()
            self.clock.tick(fps)

