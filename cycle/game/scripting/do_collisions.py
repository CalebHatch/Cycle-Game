import constants
from cycle.game.casting.player import Player

from game.scripting.action import Action
from game.shared.coordinate import Coordinate
from game.casting.game_over import GameOver


class DoCollisions(Action):
    # Handles the collision interaction between the players.

    def __init__(self):

        self._is_game_over = False
        self._game_over_message = ""

    def execute(self, cast):

        if not self._is_game_over:
            self._do_collision(cast)
        self._do_game_over(cast)

    def _do_collision(self):
        pass

    def _do_game_over(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Coordinate(x, y)

        if self._is_game_over:
            game_over = GameOver(position)
            game_over.set_text(GameOver(Player))
            game_over.set_font_size(45)


