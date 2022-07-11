import constants
from cycle.game.casting.game_over import set_color
from game.casting.player import Player
from game.shared.color import Color
from game.shared.coordinate import Coordinate

class Cycle(Player):
    
    def __init__(self, position):
        
        super().__init__()

        self._segments = []
        self._color = Color(255, 255, 255)
        self._name = ""

    def get_segments(self):
        
        return self._segments

    def get_cycle(self):
        
        return self._segments[0]

    def wall(self, game_over):
        
        wall = self._segments[-1]
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
            velocity = Coordinate(0, 1 * -constants.CELL_SIZE)
            text = "O" if i == 0 else "#"

            set_color(self._color)

    def turn_cycle(self, velocity):
        self.set_velocity(velocity)

    def set_cycle_color(self, color):
        self._color = color

    def set_name(self, name):
        self._name = name
