class Script:
    # Library for the actions that are to be performed.

    def __init__(self):

        self._actions = {}

    def add_action(self, group, action):
        
        if group not in self._actions.keys():
            self._actions[group] = []

        if action not in self._actions[group]:
            self._actions[group].append(action)

    def remove_action(self, group, action):
        
        if group in self._actions:
            self._actions[group].remove(action)