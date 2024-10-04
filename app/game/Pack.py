from .Entity import Entity
from .culc import *

class Pack(Entity):
    def __init__(self, size, xposition, yposition, xspeed, yspeed):
        super().__init__(size, xposition, yposition, xspeed, yspeed)

    def move(self):
        self._xposition += self._xspeed
        self._yposition += self._yspeed

        return 

    # dir=Trueで上下の、Falseで左右に対する反射
    def refrect(self, dir):
        rate = 0.95
        if(dir):
            self._yspeed *= -1 * rate
            self._xspeed *= rate
        if(not dir):
            self._xspeed *= -1 * rate
            self._yspeed *= rate
        
        return 


    # packとplayerの完全弾性衝突による衝突後の速度を計算
    def __elastic_collsion(self, player_speed, player_position):
        pack_position = (self._xposition, self._yposition)
        pack_speed = (self._xspeed, self._yspeed)
        n_vec = culc_normal_vec(pack_position, player_position)
        t_vec = (-1 * n_vec[1], n_vec[0])

        v_pack_n = culc_inner_product(pack_speed, n_vec)
        v_pack_t = culc_inner_product(pack_speed, t_vec)
        v_player_n = culc_inner_product(player_speed, n_vec)
        v_player_t = culc_inner_product(player_speed, t_vec)


        V_pack_x = v_player_n * n_vec[0] + v_pack_t * t_vec[0]
        V_pack_y = v_player_n * n_vec[1] + v_pack_t * t_vec[1]

        return (V_pack_x, V_pack_y)

    # プレイヤーと衝突したときの処理
    def hit_player(self, player_speed, player_position):
        speed_after_hit = self.__elastic_collsion(player_speed, player_position)
        self._xspeed = speed_after_hit[0]
        self._yspeed = speed_after_hit[1]

        return 

            


