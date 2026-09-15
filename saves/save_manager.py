import pygame as pg
import os
from pathlib import Path

class SaveManager:
    def __init__(self):
        self.SAVE_DIR = Path(__file__).parent
        self.save_files = None


    def get_save_files(self):
        for file in os.listdir(self.SAVE_DIR):
            if file.endswith('.dat'):
                self.save_files.append(file)
        return self.save_files
