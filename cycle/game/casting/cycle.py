import constants
from cycle.game.casting.game_over import set_color
from game.casting.player import Player
from game.shared.coordinate import Coordinate

class Color:

    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    def colors(self):
        return self._red, self._green, self._blue
class Cycle(Player):
    # Gets player's cycles to move around and have color
    
    def __init__(self):
        self._color = Color(255, 255, 255)
        self._name = ""

    def wall(self, game_over):
        wall = self.position(Player)

        if not game_over:
            set_color(self._color)
        else:
            set_color(constants.WHITE)

    def _start_cycle(self, position):
    
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Coordinate(x, y + i * constants.CELL_SIZE)
            set_color(self._color)

    def turn_cycle(self, velocity):
        self.set_velocity(velocity)

    def set_cycle_color(self, color):
        self._color = color

    def set_name(self, name):
        self._name = name
