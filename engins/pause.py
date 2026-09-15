import pygame as pg

class Pause:
    def __init__(self):
        self.pause_active = False
        self.pause_buttons = [
            'Game map',
            'Settings',
            'Quit in menu'
            'Quit',
        ]
        self.settings_buttons = [
            "Full screen",
            "Sound menu",
            "Sound game",
            "Fps",
            "Back",
        ]
        self.pause_state = 'pause' # 'pause' or 'settings'
        self.selected_pos = 0
        self.font = pg.font.SysFont('Arial', 32)
        self.small_font = pg.font.SysFont('Arial', 20)
        self.buttons = self.pause_buttons

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if self.pause_state == "pause":
                self.handle_pause_input(event)
            elif self.pause_state == "settings":
                self.handle_settings_input(event)


    def handle_pause_input(self, event):
        key = event.key
        if key in (pg.K_UP, pg.K_w):
            self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key in (pg.K_DOWN, pg.K_s):
            self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key == pg.K_RETURN:
            selected_text = self.buttons[self.selected_pos]
            if selected_text == 'pause':
                self.pause_state = 'pause'
                self.buttons = self.pause_buttons
            elif selected_text == 'settings':
                self.pause_state = 'settings'
                self.buttons = self.settings_buttons
        elif key == pg.K_ESCAPE:
            self.pause_active = False

    def handle_settings_input(self, event):
        key = event.key
        if key in (pg.K_UP, pg.K_w):
            self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key in (pg.K_DOWN, pg.K_s):
            self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key == pg.K_ESCAPE or (self.buttons[self.selected_pos] == 'Back'):
            self.pause_state = 'pause'
            self.buttons = self.pause_buttons
            self.selected_pos = 0

    def update(self):
        pass

    def draw(self, screen):
        screen_w, screen_h = screen.get_window_size()
        screen.fill((20, 20, 30))
        title = self.font.render("City Stories", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_w // 2, 10))
        screen.blit(title, title_rect)

        for i, text in enumerate(self.buttons):
            color = (255, 215, 0) if i == self.selected_pos else (200, 200, 200)
            label = self.font.render(text, True, color)
            rect = label.get_rect(center=(screen_w // 2, 20 + i * 50))
            screen.blit(label, rect)

        hint = self.small_font.render("Use arrows / W,S to navigate, Enter to select", True, (128, 128, 128))
        hint_rect = hint.get_rect(midbottom=(screen_w // 2, screen_h - 20))
        screen.blit(hint, hint_rect)

