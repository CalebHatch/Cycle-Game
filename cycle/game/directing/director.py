def _execute_actions(group, cast, script):

    actions = script.get_actions(group)
    for action in actions:
        action.execute(cast, script)


class Director:

    def __init__(self, video_service):

        self._video_service = video_service

    def start_game(self, cast, script):
        
        self._video_service.open_window()
        while self._video_service.is_window_open():
            _execute_actions("input", cast, script)
            _execute_actions("update", cast, script)
            _execute_actions("output", cast, script)
        self._video_service.close_window()

