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


    # packとplayerの非弾性衝突による衝突後の速度を計算
    def __elastic_collsion(self, player_speed, player_position):
        # 跳ね返り係数
        e = 0.5

        pack_position = (self._xposition, self._yposition)
        pack_speed = (self._xspeed, self._yspeed)
        # tが接線方向、nがそれの法線方向の単位ベクトル
        t_vec = culc_normal_vec(pack_position, player_position)
        n_vec = (-1 * t_vec[1], t_vec[0])

        # 接線方向とその法線方向の正射影ベクトルを求める
        temp = culc_inner_product(t_vec, pack_speed)
        pack_speed_t = (temp * t_vec[0], temp * t_vec[1])
        pack_speed_n = (pack_speed[0] - pack_speed_t[0], pack_speed[1] - pack_speed_t[1])
        temp = culc_inner_product(t_vec, player_speed)
        player_speed_t = (temp * t_vec[0], temp * t_vec[1])
        player_speed_n = (player_speed[0] -player_speed_t[0], player_speed[1] - player_speed_t[1])

        # プレイヤーとパックの法線方向における弾性衝突語の速度を計算
        temp1 = ((1 + e) * player_speed_n[0] + (e -1) * pack_speed_n[0]) / (2 * e)
        temp2 = ((1 + e) * player_speed_n[1] + (e -1) * pack_speed_n[1]) / (2 * e)
        hitted_pack_speed_n = (temp1, temp2)
        hitted_pack_speed_t = pack_speed_t

        # xy平面上のベクトルに戻す
        hitted_pack_speed = (hitted_pack_speed_n[0] + hitted_pack_speed_t[0], hitted_pack_speed_n[1] + hitted_pack_speed_t[1])

        return hitted_pack_speed

    # プレイヤーと衝突したときの処理
    def hit_player(self, player_speed, player_position):
        speed_after_hit = self.__elastic_collsion(player_speed, player_position)
        self._xspeed = speed_after_hit[0]
        self._yspeed = speed_after_hit[1]

        return 

            


