from Pack import Pack
from Player import Player
from .. import image_process


class AirHockey:
    def __init__(self, pack, players, width, height, goal_size, goal_position, finish_point):
        self._pack = []
        self._players = []
        self._width = width
        self._height = height
        self._goal_size = goal_size
        self._goal_position = goal_position
        self._finish_point = finish_point
        self.__server =True

    # ゲーム開始時に伴う初期化処理
    def start_game(self):
        # パックの初期化
        PACKSIZE =20
        xposition=self._width/2
        yposition = self._height/2
        if self.__server:
            xposition -=xposition/2
        else :
            xposition +=xposition/2
        self.__server= not self.__server
        pack = Pack(PACKSIZE,xposition,yposition,0,0)
        self._pack.append(pack)

        # プレイヤーの初期化
        PLAYER_SIZE = 20
        CENTER_LINE = self._width/2
        players_position_list = image_process()
        for player_position in players_position_list:
            HAND_ID = players_position_list[0]
            (xposition,yposition) = players_position_list[1]
            TEAM_ID=0
            if xposition>CENTER_LINE:
                TEAM_ID=1
            player = Player(PLAYER_SIZE,xposition,yposition,0,0,TEAM_ID,HAND_ID)
            self._players.append(player)


            

        