class Settings:
    screen_width: int = 250
    screen_height: int = 250
    full_screen: bool = False
    sound_game: bool = False
    sound_menu: bool = False
    fps: int = 60

    # world
    chunks_row = 10
    chunks_column = 10
    cell_row = 10
    cell_column = 10
    cell_w = 20
    cell_h = 20


settings = Settings()
