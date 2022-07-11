import constants
from game.scripting.action import Action
from game.shared.coordinate import Coordinate


class ControlPlayers(Action):
    # Controls the method of action of the players.

    def __init__(self, keyboard_service):

        self._keyboard_service = keyboard_service
        
        self._player_one_direction = Coordinate(0, -constants.CELL_SIZE)
        self._player_two_direction = Coordinate(0, -constants.CELL_SIZE)

    def execute(self, cast):

        # Player one keys

        # left
        if self._keyboard_service.press_key_down('a'):
            self._player_one_direction = Coordinate(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.press_key_down('d'):
            self._player_one_direction = Coordinate(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.press_key_down('w'):
            self._player_one_direction = Coordinate(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.press_key_down('s'):
            self._player_one_direction = Coordinate(0, constants.CELL_SIZE)

        cycle_one = cast.get_first_player("player_one")
        cycle_one.turn_cycle(self._player_one_direction)

        # Player two keys

        # left
        if self._keyboard_service.press_key_down('j'):
            self._player_two_direction = Coordinate(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.press_key_down('l'):
            self._player_two_direction = Coordinate(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.press_key_down('i'):
            self._player_two_direction = Coordinate(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.press_key_down('k'):
            self._player_two_direction = Coordinate(0, constants.CELL_SIZE)

        cycle_two = cast.get_second_player("player_two")
        cycle_two.turn_cycle(self._player_two_direction)
