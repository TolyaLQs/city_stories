from typing import AnyStr

import pygame as pg

class Cell:
    def __init__(self, x: int, y: int, width: int=20, height: int=20, types=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.types = types
        self.active = False
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.color = (100, 255, 100)

    def update(self):
        pass

    def click_cell(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.active = True
        else:
            self.active = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        if self.active:
            pg.draw.rect(screen, (0, 0, 0), self.rect, width=1)
        else:
            pg.draw.rect(screen, (0, 255, 255), self.rect, width=1)


class Chunk:
    def __init__(self, x, y, cell_w, cell_h, cell_row, cell_column):
        self.x = x
        self.y = y
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.cell_row = cell_row
        self.cell_column = cell_column
        self.active = False
        self.surface = pg.surface.Surface((self.x+(self.cell_w*self.cell_column), self.y+(self.cell_h*self.cell_row)))
        self.rect = self.surface.get_rect(center=(
                self.x+((self.cell_w*self.cell_column)/2),
                self.y+((self.cell_h*self.cell_row)/2)
                        )
        )
        self.list_cell = {}
        self.cell_type = []
        self.load_cell = {}

    def create_chunk(self):
        for row in range(self.cell_row):
            for column in range(self.cell_column):
                cell = Cell(
                    x=(self.x+row*self.cell_w), y=(self.y+column*self.cell_h),
                    types=None, width=self.cell_w, height=self.cell_h
                )
                self.list_cell[(
                    self.x+row*self.cell_w, self.y+column*self.cell_h,
                    (self.x+row*self.cell_w)+self.cell_w, (self.y+column*self.cell_h)+self.cell_h
                )] = cell

        return self.list_cell


    def update(self):
        pass

    def draw(self, screen, camera_rect):
        list_cell = camera_rect.collideobjectsall(list(self.list_cell.keys()))
        for cell in list_cell:
            print(cell)
            self.list_cell[cell].draw(self.surface)
        if self.active:
            pg.draw.rect(self.surface, (150, 150, 150), self.rect, 1)
        else:
            pg.draw.rect(self.surface, (240, 240, 240), self.rect, 1)
        screen.blit(self.surface, self.rect)



