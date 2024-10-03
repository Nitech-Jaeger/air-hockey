from .Entity import Entity

class Pack(Entity):
    def __init__(self, size, xposition, yposition, xspeed, yspeed):
        super().__init__(size, xposition, yposition, xspeed, yspeed)

    def move(self):
        self._xposition += self._xspeed
        self._yposition += self._yspeed

        return 

    # dir=Trueで上下の、Falseで左右に対する反射
    def refrect(self,dir):
        rate=0.95
        if(dir):
            self._yspeed *= -1 * rate
            self._xspeed *= rate
        if(not dir):
            self._xspeed *= -1 * rate
            self._yspeed *= rate
        
        return 

    # ２次元空間における二つの座標からその２点を結んだ直線に対する法線ベクトルを計算
    def __culc_normal_vec(pos1,pos2):
        n_x = pos1[0]-pos2[0]
        n_y = pos1[1]-pos2[1]
        scale_n = (n_x*n_x+n_y*n_y)
        normal_vec = (n_x/scale_n,n_y/scale_n)
        return normal_vec

    # タプル形式で表される２次元ベクトルから内積を計算
    def __culc_inner_product(vec1,vec2):
        return vec1[0]*vec2[0]+vec1[1]*vec2[1]
    
    # packとplayerの完全弾性衝突による衝突後の速度を計算
    def __elastic_collsion(self,player_speed,player_position):
        pack_position = (self._xposition,self._yposition)
        pack_speed = (self._xspeed,self._yspeed)
        n_vec = self.__culc_normal_vec(pack_position,player_position)
        t_vec = (-1*n_vec[1],n_vec[0])

        v_pack_n = self.__culc_inner_product(pack_speed,n_vec)
        v_pack_t = self.__culc_inner_product(pack_speed,t_vec)
        v_player_n = self.__culc_inner_product(player_speed,n_vec)
        v_player_t = self.__culc_inner_product(player_speed,t_vec)


        V_pack_x = v_player_n*n_vec[0]+v_pack_t*t_vec[0]
        V_pack_y = v_player_n*n_vec[1]+v_pack_t*t_vec[1]

        return (V_pack_x,V_pack_y)

    # プレイヤーと衝突したときの処理
    def hit_player(self,player_speed,player_position):
        speed_after_hit = self.__elastic_collsion(player_speed,player_position)
        self._xspeed = speed_after_hit[0]
        self._yspeed = speed_after_hit[1]

        return 

            


