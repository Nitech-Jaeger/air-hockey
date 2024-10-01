from Entity import Entity

class Player(Entity):
    def __init__(self, size, xposition, yposition, xspeed, yspeed, TEAM_ID, HAND_ID):
        super().__init__(size, xposition, yposition, xspeed, yspeed)
        self.__point = 0
        self.__TEAM_ID = TEAM_ID
        self.__HAND_ID = HAND_ID
    
    def get_team_id(self):
        return self.__TEAM_ID
    
    def get_point(self):
        return self.__point
    
    def get_hand_id(self):
        return self.__HAND_ID
    
    def move(self, new_position):
        (new_x_position, new_y_position) = new_position
        rate = 1
        
        # 速度の更新
        # rateを用いて速度の大きさが適切になるように調節
        self._xspeed = (self._xposition - new_x_position) * rate
        self._yspeed = (self._yposition - new_y_position) * rate

        