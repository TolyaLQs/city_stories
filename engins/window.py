import pygame as pg
from .settings import settings as st
from .game import Game
from .menu import Menu


class Windows:
    def __init__(self):
        self.screen_width, self.screen_height = st.screen_width, st.screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        self.full_screen = st.full_screen
        self.fps = st.fps
        pg.init()
        if self.full_screen:
            self.screen = pg.display.set_mode(size=(0, 0), flags=pg.FULLSCREEN)
            self.screen_size = (self.screen_width, self.screen_height) = self.screen.get_window_size()
        else:
            self.screen = pg.display.set_mode(size=self.screen_size)
        self.cycles_state: bool = True
        self.window_state: str = 'menu' # 'menu' or 'game'
        self.menu = Menu()
        self.game = Game()
        self.clock = pg.Clock()

    def run(self):
        while self.cycles_state:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.cycles_state = False
                else:
                    if self.window_state == 'menu':
                        self.menu.handle_event(event)
                    elif self.window_state == 'game':
                        self.game.handle_event(event)
            if self.window_state == 'menu':
                self.menu.update()
                if self.menu.menu_state == 'quit':
                    self.cycles_state = False
                elif self.menu.menu_state == 'new_game':
                    self.window_state = 'game'
                    self.game.new_game()
                self.menu.draw(self.screen)
            else:
                self.game.update()
                self.game.draw(self.screen)

            pg.display.flip()
            self.clock.tick(self.fps)
        pg.quit()

