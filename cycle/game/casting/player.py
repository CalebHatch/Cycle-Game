import constants
from game.shared.coordinate import Coordinate


class Player:
    # Keeps track of position and velocity of each player.

    def __init__(self):
        self._text = ""
        self._font_size = 15
        
        self._position = Coordinate(0, 0)
        self._velocity = Coordinate(0, 0)

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity

    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_text(self, text):
        self._text = text

    def set_velocity(self, velocity):
        self._velocity = velocity

    def move_player(self):
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y

        self._position = Coordinate(x, y)


