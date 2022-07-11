from game.scripting.action import Action


class DrawPlayersMovement(Action):
    # Draws out the players' cycles.
  
    def __init__(self, video_service):
       
        self._video_service = video_service

    def execute(self, cast, script):
       
        score1 = cast.get_first_player("score1")
        score2 = cast.get_second_player("score2")

        self._video_service.clear_buffer()
        self._video_service.flush_buffer()
        
        self._video_service.draw_player(score1)
        self._video_service.draw_player(score2)
