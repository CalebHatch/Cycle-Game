import pyray
import constants


def close_window():

    pyray.close_window()


def draw_player(player, centered=False):

    text = player.get_text()
    x = player.get_position().get_x()
    y = player.get_position().get_y()

    pyray.draw_text(text, x, y)


def draw_players(players, centered=False):

    for player in players:
        draw_player(player, centered)


def flush_buffer():

    pyray.end_drawing()


def is_window_open():

    return pyray.window_should_close()


def open_window():

    pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
    pyray.set_target_fps(constants.FRAME_RATE)


def _draw_grid():

    for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
        pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)

    for x in range(0, constants.MAX_X, constants.CELL_SIZE):
        pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
class VideoService:
    # Allows a video output for the player to see the game.

    def __init__(self, debug = False):
        
        self._debug = debug

    def clear_buffer(self):
        
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug:
            _draw_grid()

