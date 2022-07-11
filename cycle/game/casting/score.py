from game.casting.player import Player
from game.shared.coordinate import Coordinate


class _Score(Player):
    
    def __init__(self):
       
        self._coordinates = 0
        position = Coordinate(0, 0)
        self._player_name = "player"
        self.set_text(f"{self._player_name}: {self._coordinates}")
        self.set_position(position)

    def add_coordinates(self, coordinates):
        
        self._coordinates += coordinates
        self.set_text(f"{self._player_name}: {self._coordinates}")

    def get_score(self):
        
        return self._score

    def lower_score(self):
       
        self._coordinates -= 1
        self.set_text(f"{self._player_name}: {self._coordinates}")

    def set_player_name(self,name):
        
        self._player_name = name
        self.set_text(f"{self._player_name}: {self._coordinates}")