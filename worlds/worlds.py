import pygame as pg
from engins.settings import settings as st
from .chunks import Chunk

class World:
    def __init__(self):
        self.chunks_row = st.chunks_row
        self.chunks_column = st.chunks_column
        self.cell_row = st.cell_row
        self.cell_column = st.cell_column
        self.cell_w = st.cell_w
        self.cell_h = st.cell_h
        self.surface = pg.surface.Surface(
            ((self.chunks_row*self.cell_row*self.cell_w), (self.chunks_column*self.cell_column*self.cell_h))
        )
        self.load_chunks = []
        self.chunks_all = {}
        self.radius = 1
        self.last_current_chunk = None
        self.current_chunk = None


    def create_world(self):
        for row in range(self.chunks_row):
            for column in range(self.cell_column):
                chunk = Chunk(
                    row*(self.cell_row*self.cell_w), column*(self.cell_column*self.cell_h), self.cell_w, self.cell_h,
                    self.cell_row, self.cell_column
                )
                chunk.create_chunk()
                self.chunks_all[(row, column)] = chunk

    def check_chunks(self):
        pass

    def load_chunks_def(self, chunk_x, chunk_y):
        self.current_chunk = self.chunks_all.get((chunk_x, chunk_y))
        self.load_chunks = []
        for x in range(-self.radius, self.radius + 1):
            for y in range(-self.radius, self.radius + 1):
                chunk = self.chunks_all.get((chunk_x, chunk_y))
                if chunk:
                    self.load_chunks.append(chunk)

    def update(self, player_pos, camera_rect):
        chunk_x = int(player_pos[0] // (self.cell_w * self.cell_row))
        chunk_y = int(player_pos[1] // (self.cell_h * self.cell_column))
        self.current_chunk = self.chunks_all.get((chunk_x, chunk_y))
        if self.current_chunk == None:
            self.load_chunks_def(chunk_x, chunk_y)
        if self.current_chunk != self.last_current_chunk:
            self.load_chunks_def(chunk_x, chunk_y)
            self.current_chunk = self.last_current_chunk
        for chunk in self.load_chunks:
            chunk.update()

    def draw(self, screen, camera_rect):
        for chunk in self.load_chunks:
            chunk.draw(self.surface, camera_rect)

        screen.blit(self.surface, camera_rect)
