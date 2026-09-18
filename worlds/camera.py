import pygame as pg

class Camera:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.surface = pg.surface.Surface((self.screen_w, self.screen_h))
        self.rect = self.surface.get_rect(center=(0,0))

    def update(self, player_pos):
        self.rect = self.surface.get_rect(center=(player_pos))

