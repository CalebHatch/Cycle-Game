class Cast:
    # Keeps track and record of the group of players

    def __init__(self):

        self._players = {}

    def add_player(self, group, player):

        if group not in self._players.keys():
            self._players[group] = []

        if player not in self._players[group]:
            self._players[group].append(player)

    def get_players(self):

        results = []
        for group in self._players:
            results.extend(self._players[group])
        return results

    def remove_player(self, group, player):

        if group in self._players:
            self._players[group].remove(player)
