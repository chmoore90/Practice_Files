# self explanatory

class tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class ship:
    def __init__(self, tile, size, state) -> None:
        self.tile = tile
        self.size = size
        self.state = state


def draw_board():
    pass
