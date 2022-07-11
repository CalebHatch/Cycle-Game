import constants
from cycle.game.casting.game_over import set_color
from game.casting.player import Player
from game.shared.color import Color
from game.shared.coordinate import Coordinate

class Cycle(Player):
    
    def __init__(self):
        self._color = Color(255, 255, 255)
        self._name = ""

    def get_cycle(self):
        
        return self._segments[0]

    def wall(self, game_over):
        wall = self.position(Player)

        velocity = wall.get_velocity()
        offset = velocity.go_back()
        position = wall.get_position().add(offset)

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
