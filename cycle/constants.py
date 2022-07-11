class Color:

    def __init__(self, red, green, blue, alpha=255):
        self._red = red
        self._green = green
        self._blue = blue

    def colors(self):
        return self._red, self._green, self._blue
# Constants that the program will use.
COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30
FONT_SIZE = 15
CAPTION = "cycle game"
CYCLE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

SCORE_X = 0
SCORE_Y = 0
