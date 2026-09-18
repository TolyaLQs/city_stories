# city_stories/engins/menu.py
from pygame import mouse

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
        self.rect = self.label.get_rect(center=(self.x, y))

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


class Menu:
    def __init__(self, screen_size):
        self.screen_w, self.screen_h = screen_size
        self.menu_state = 'menu'
        self.selected_pos = None
        self.font = pg.font.SysFont('Arial', 32)
        self.small_font = pg.font.SysFont('Arial', 20)
        self.menu_buttons = [
            Button(self.screen_w//2, self.screen_h//2 - 45, 'New game', 0),
            Button(self.screen_w//2, self.screen_h//2 - 15, 'Load game', 1),
            Button(self.screen_w//2, self.screen_h//2 + 15, 'Settings', 2),
            Button(self.screen_w//2, self.screen_h//2 + 45, 'Quit', 3),
        ]
        self.settings_buttons = [
            Button(self.screen_w//2, self.screen_h//2 - 60, "Full screen", 0),
            Button(self.screen_w//2, self.screen_h//2 - 30, "Sound menu", 1),
            Button(self.screen_w//2, self.screen_h//2, "Sound game", 2),
            Button(self.screen_w//2, self.screen_h//2 + 30, "Fps", 3),
            Button(self.screen_w//2, self.screen_h//2 + 60, "Back", 4),
        ]
        self.load_game_buttons = [
            Button(self.screen_w // 2, self.screen_h // 2 + 60, "Back", 4),
        ]
        self.mouse_pos = (0, 0)
        self.buttons = self.menu_buttons
        self.buttons_hover = False

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
        elif key == pg.K_RETURN:
            for button in self.buttons:
                if self.selected_pos == button.selected_pos:
                    self.click_button(button)
                    break
        elif key == pg.K_ESCAPE:
            if self.menu_state == 'menu':
                self.menu_state = 'quit'
            else:
                self.menu_state = 'menu'
                self.buttons = self.menu_buttons
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
        if button.text == 'New game':
            self.menu_state = 'new_game'
        elif button.text == 'Quit':
            self.menu_state = 'quit'
        elif button.text == 'Settings':
            self.menu_state = 'settings'
            self.buttons = self.settings_buttons
            self.selected_pos = None
        elif button.text == 'Load game':
            self.menu_state = 'load_game'
            self.buttons = self.load_game_buttons
            self.selected_pos = None
        elif button.text == 'Back':
            self.menu_state = 'menu'
            self.buttons = self.menu_buttons
            self.selected_pos = None

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

    def update(self):
        # Логика обновления может быть расширена позже
        # self.check_hover()
        if self.buttons_hover:
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
        else:
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))

    def draw(self, screen):
        screen.fill((20, 20, 30))
        title = self.font.render("City Stories", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_w // 2, 10))
        screen.blit(title, title_rect)
        for button in self.buttons:
            button.draw(screen)

        hint = self.small_font.render("Use arrows / W,S to navigate, Enter to select", True, (128, 128, 128))
        hint_rect = hint.get_rect(midbottom=(self.screen_w // 2, self.screen_h - 20))
        screen.blit(hint, hint_rect)

