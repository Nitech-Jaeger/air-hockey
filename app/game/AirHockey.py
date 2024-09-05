from Pack import Pack
from Player import Player

class AirHockey:
    def __init__(self, pack, players, width, height, goal_size, goal_position, finish_point):
        self._pack = []
        self._players = []
        self._width = width
        self._height = height
        self._goal_size = goal_size
        self._goal_position = goal_position
        self._finish_point = finish_point

    def end_of_game(self):
        for player in self._players:
            if (player.get_point() == self._finish_point):
                finish_game()