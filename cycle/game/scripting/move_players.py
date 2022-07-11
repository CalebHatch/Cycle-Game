from game.scripting.action import Action

class MovePlayers(Action):
    # Allows the actors to move.

    def execute(self, cast):
        players = cast.get_players()
        for player in players:
            player.move()
