import pygame as pg

class Button:
    def __init__(self, x, y, text, selected_pos, color=(200, 200, 200), bgcolor=None):
        self.x = x
        self.y = y
        # self.width = width
        # self.height = height
        self.text = text
        self.color = color
        self.bg_color = bgcolor
        self.active = False
        self.hover = False
        self.selected_pos = selected_pos
        self.font = pg.font.SysFont('Arial', 30)
        self.label = self.font.render(text, True, color)
        self.rect = self.label.get_rect(center=(self.x, self.y))

    def check_click(self):
        if self.hover and self.active:
            return True
        else:
            return False

    def check_hover(self):
        if self.hover:
            return True
        else:
            return False

    def hover_selected(self):
        if self.hover:
            return self.selected_pos
        else:
            return None

    def mouse_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

    def draw(self, screen):
        if self.hover:
            self.color = (255, 215, 0)
        else:
            self.color = (200, 200, 200)
        self.label = self.font.render(self.text, True, self.color)
        self.rect = self.label.get_rect(center=(self.x, self.y))
        screen.blit(self.label, self.rect)

class Pause:
    def __init__(self, screen_size):
        self.screen_w, self.screen_h = screen_size
        self.pause_active = False
        self.pause_buttons = [
            Button(self.screen_w // 2, self.screen_h // 2 - 60, 'Resume', 0),
            Button(self.screen_w // 2, self.screen_h // 2 - 30, 'Game map', 0),
            Button(self.screen_w // 2, self.screen_h // 2, 'Settings', 1),
            Button(self.screen_w // 2, self.screen_h // 2 + 30, 'Quit in menu', 2),
            Button(self.screen_w // 2, self.screen_h // 2 + 60, 'Quit', 3),
        ]
        self.settings_buttons = [
            Button(self.screen_w // 2, self.screen_h // 2 - 60, "Full screen", 0),
            Button(self.screen_w // 2, self.screen_h // 2 - 30, "Sound menu", 1),
            Button(self.screen_w // 2, self.screen_h // 2, "Sound game", 2),
            Button(self.screen_w // 2, self.screen_h // 2 + 30, "Fps", 3),
            Button(self.screen_w // 2, self.screen_h // 2 + 60, "Back", 4),
        ]
        self.pause_state = 'pause' # 'pause' or 'settings'
        self.selected_pos = None
        self.font = pg.font.SysFont('Arial', 32)
        self.small_font = pg.font.SysFont('Arial', 20)
        self.buttons = self.pause_buttons

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            self.key_down(event)
        if event.type == pg.MOUSEMOTION:
            self.mouse_move(event)
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                self.handle_mouseup(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_mousedown(event)

    def key_down(self, event):
        key = event.key
        if key in (pg.K_s, pg.K_DOWN):
            if self.selected_pos == None:
                self.selected_pos = 0
            else:
                self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
        elif key in (pg.K_UP, pg.K_w):
            if self.selected_pos == None:
                self.selected_pos = (len(self.buttons)-1)
            else:
                self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
        elif key == pg.K_ESCAPE:
            self.selected_pos = None
            if self.pause_state == 'pause':
                self.pause_active = False
            else:
                self.pause_state = 'pause'
        elif key == pg.K_RETURN:
            for button in self.buttons:
                if self.selected_pos == button.selected_pos:
                    self.click_button(button)
                    break
        for button in self.buttons:
            if button.selected_pos == self.selected_pos:
                button.hover = True
            else:
                button.hover = False

    def handle_mousedown(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(event.pos):
                button.active = True
            else:
                button.active = False

    def handle_mouseup(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(event.pos):
                if button.check_click():
                    self.selected_pos = button.check_hover()
                    self.click_button(button)

    def click_button(self, button):
        if button.text == 'Quit':
            self.pause_state = 'quit'
        elif button.text == 'Settings':
            self.pause_state = 'settings'
            self.buttons = self.settings_buttons
            self.selected_pos = None
        elif button.text == 'Back':
            self.pause_state = 'pause'
            self.buttons = self.pause_buttons
            self.selected_pos = None
        elif button.text == 'Resume':
            self.pause_active = False
            self.selected_pos = None
        elif button.text == 'Quit in menu':
            self.pause_active = False
            self.selected_pos = None
            self.pause_state = 'quit in menu'

    def check_hover(self):
        for button in self.buttons:
            if button.check_hover():
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                self.selected_pos = button.hover_selected()
                break
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))

    def mouse_move(self, event):
        self.buttons_hover = False
        for button in self.buttons:
            button.mouse_hover(event.pos)
            if button.check_hover():
                self.selected_pos = button.hover_selected()
                self.buttons_hover = True

    # def handle_event(self, event):
    #     if event.type == pg.KEYDOWN:
    #         if self.pause_state == "pause":
    #             self.handle_pause_input(event)
    #         elif self.pause_state == "settings":
    #             self.handle_settings_input(event)
    #
    # def handle_pause_input(self, event):
    #     key = event.key
    #     if key in (pg.K_UP, pg.K_w):
    #         self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
    #     elif key in (pg.K_DOWN, pg.K_s):
    #         self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
    #     elif key == pg.K_RETURN:
    #         selected_text = self.buttons[self.selected_pos]
    #         if selected_text == 'pause':
    #             self.pause_state = 'pause'
    #             self.buttons = self.pause_buttons
    #         elif selected_text == 'settings':
    #             self.pause_state = 'settings'
    #             self.buttons = self.settings_buttons
    #     elif key == pg.K_ESCAPE:
    #         self.pause_active = False
    #
    # def handle_settings_input(self, event):
    #     key = event.key
    #     if key in (pg.K_UP, pg.K_w):
    #         self.selected_pos = (self.selected_pos - 1) % len(self.buttons)
    #     elif key in (pg.K_DOWN, pg.K_s):
    #         self.selected_pos = (self.selected_pos + 1) % len(self.buttons)
    #     elif key == pg.K_ESCAPE or (self.buttons[self.selected_pos] == 'Back'):
    #         self.pause_state = 'pause'
    #         self.buttons = self.pause_buttons
    #         self.selected_pos = 0

    def update(self):
        pass

    def draw(self, screen):
        screen_w, screen_h = screen.get_window_size()
        screen.fill((20, 20, 30))
        title = self.font.render("Pause", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_w // 2, 10))
        screen.blit(title, title_rect)

        for button in self.buttons:
            button.draw(screen)

        hint = self.small_font.render("Use arrows / W,S to navigate, Enter to select", True, (128, 128, 128))
        hint_rect = hint.get_rect(midbottom=(screen_w // 2, screen_h - 20))
        screen.blit(hint, hint_rect)

