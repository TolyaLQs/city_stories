# city_stories/engins/menu.py
import pygame as pg

class Menu:
    def __init__(self, screen_size):
        self.screen_w, self.screen_h = screen_size
        self.menu_state = 'menu'
        self.selected_pos = 0
        self.font = pg.font.SysFont('Arial', 32)
        self.small_font = pg.font.SysFont('Arial', 20)
        self.menu_buttons = [
            'New game',
            'Load game',
            'Settings',
            'Quit',
        ]
        self.settings_buttons = [
            "Full screen",
            "Sound menu",
            "Sound game",
            "Fps",
            "Back",
        ]
        self.load_game_buttons = []

        self.buttons = self.menu_buttons

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if self.menu_state == "menu":
                self.handle_menu_input(event)
            elif self.menu_state == "settings":
                self.handle_settings_input(event)
            elif self.menu_state == "load_game":
                self.handle_load_game_input(event)

    def handle_menu_input(self, event):
        key = event.key
        if key in (pg.K_UP, pg.K_w):
            self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key in (pg.K_DOWN, pg.K_s):
            self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key == pg.K_RETURN:
            selected_text = self.buttons[self.selected_pos]
            if selected_text == 'New game':
                self.menu_state = 'new_game'
            elif selected_text == 'Quit':
                self.menu_state = 'quit'
            elif selected_text == 'Settings':
                self.menu_state = 'settings'
                self.buttons = self.settings_buttons
                self.selected_pos = 0
            elif selected_text == 'Load game':
                self.menu_state = 'load_game'
                self.buttons = self.load_game_buttons or ['No saves', 'Back']
                self.selected_pos = 0

    def handle_settings_input(self, event):
        key = event.key
        if key in (pg.K_UP, pg.K_w):
            self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key in (pg.K_DOWN, pg.K_s):
            self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key == pg.K_ESCAPE or (self.buttons[self.selected_pos] == 'Back'):
            self.menu_state = 'menu'
            self.buttons = self.menu_buttons
            self.selected_pos = 0

    def handle_load_game_input(self, event):
        key = event.key
        if key in (pg.K_UP, pg.K_w):
            self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key in (pg.K_DOWN, pg.K_s):
            self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key == pg.K_ESCAPE:
            self.menu_state = 'menu'
            self.buttons = self.menu_buttons
            self.selected_pos = 0

    def update(self):
        # Логика обновления может быть расширена позже
        pass

    def draw(self, screen):
        screen.fill((20, 20, 30))
        title = self.font.render("City Stories", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_w // 2, 10))
        screen.blit(title, title_rect)

        for i, text in enumerate(self.buttons):
            color = (255, 215, 0) if i == self.selected_pos else (200, 200, 200)
            label = self.font.render(text, True, color)
            rect = label.get_rect(center=(self.screen_w // 2, 20 + i * 50))
            screen.blit(label, rect)

        hint = self.small_font.render("Use arrows / W,S to navigate, Enter to select", True, (128, 128, 128))
        hint_rect = hint.get_rect(midbottom=(self.screen_w // 2, self.screen_h - 20))
        screen.blit(hint, hint_rect)

