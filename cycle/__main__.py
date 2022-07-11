import constants
from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.casting.score import _Score
from game.directing.director import Director
from game.scripting.control_players import ControlPlayers
from game.scripting.draw_players_movement import DrawPlayersMovement
from game.scripting.do_collisions import DoCollisions
from game.scripting.move_players import MovePlayers
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.coordinate import Coordinate

def main():
    # Main drives the program.

    player_one = Cycle(Coordinate(int(constants.MAX_X - 600), int(constants.MAX_Y / 2)))
    player_two = Cycle(Coordinate(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))

    player_one.set_cycle_color(constants.RED)
    player_two.set_cycle_color(constants.GREEN)
    
    player_1_name = "Player 1"
    player_2_name = "Player 2"

    cast = Cast()
    score1 = _Score()
    score2 = _Score()

    score1.set_player_name(player_1_name)
    score2.set_player_name(player_2_name)

    cast.add_player("player_one", player_one)
    cast.add_player("player_two", player_two)
    cast.add_player("score1", score1)
    cast.add_player("score2", score2)

    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()

    script.add_action("input", ControlPlayers(keyboard_service))
    script.add_action("update", DoCollisions(player_one, player_two))
    script.add_action("update", MovePlayers(player_one, player_two))
    script.add_action("output", DrawPlayersMovement(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
