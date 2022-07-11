from game.casting.player import Player
from game.shared.coordinate import Coordinate


class _Score(Player):
    # Keeps record of score and points earned or lost.
    
    def __init__(self):
       
        self._coordinates = 0
        self._player_name = "player"
        self.set_text(f"{self._player_name}")

    def get_score(self):
        
        return self._score

    def lower_score(self):
       
        self._coordinates -= 1
        self.set_text(f"{self._player_name}: {self._coordinates}")