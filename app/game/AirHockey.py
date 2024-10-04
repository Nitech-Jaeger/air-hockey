from .Pack import Pack
from .Player import Player
# from ..image_process import image_process
import math


class AirHockey:
    def __init__(self, pack, players, width, height, goal_size, goal_position, finish_point):
        self._packs = []
        self._players = []
        self._WIDTH = width
        self._HEIGHT = height
        self._GOAL_SIZE = goal_size
        self._GOAL_POSITION = goal_position
        self._FINISH_POINT = finish_point
        self.__server =True

    # ゲーム開始時に伴う初期化処理
    def start_game(self):
        # パックの初期化
        PACKSIZE = 20
        xposition = self._WIDTH / 2
        yposition = self._HEIGHT / 2
        if self.__server:
            xposition -= xposition / 2
        else :
            xposition += xposition / 2
        self.__server = not self.__server
        pack = Pack(PACKSIZE, xposition, yposition, 100, 0)
        self._packs.append(pack)

        # プレイヤーの初期化
        PLAYER_SIZE = 20
        CENTER_LINE = self._WIDTH / 2
        # players_position_list = image_process()
        players_position_list = []
        for player_position in players_position_list:
            HAND_ID = player_position[0]
            (xposition, yposition) = player_position[1]
            TEAM_ID=0
            if xposition > CENTER_LINE:
                TEAM_ID = 1
            player = Player(PLAYER_SIZE, xposition, yposition, 0, 0, TEAM_ID, HAND_ID)
            self._players.append(player)
        
        return
    
    # タプルの形で渡された２点間の距離を返す
    def __culc_distance_of_two_points(self, pos1, pos2):
        dis = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
        dis = math.sqrt(dis)
        return dis
    
    # 点と直線の距離を返す。
    # 直線はax+by+c=0の形で渡され、点はタプルで渡される。
    def __culc_distance_of_line_and_point(self, a, b, c, point):
        temp = a * point[0] + b * point[1] + c 
        if temp < 0 :
            temp *= -1
        return temp / math.sqrt( a ** 2 + b ** 2)
    
    # タプルの形式で渡される２点を通る直線の式をax+by+c=0の形で求める。
    def __culc_linear_function(self, pos1, pos2):
        if pos1[1] == pos2[1]:
            a = 0
            b = 1
            c = -1 * pos1[1]
            return a, b, c
        elif pos1[0] == pos2[0]:
            a = 1
            b = 0
            c = -1 * pos1[0]
            return a, b, c
        a = -1 * (pos1[1] - pos2[1])
        b = pos1[0] - pos2[0]
        c =-1 * (a * pos1[0] + b *pos1[1])
        return a, b, c

    #ax+by+c=0と(x-cx)^2+(y-cy)^2=r^2の二つの交点の座標を返す 
    def __culc_intersection_of_circle_and_linear(self,a, b, c, cx, cy, r):
        if a == 0:
            y = -1 * c / b
            x1 = cx + math.sqrt(r ** 2 - (y - cy) ** 2)
            x2 = cx - math.sqrt(r ** 2 - (y - cy) ** 2)
            return (x1, y), (x2, y)
        elif b == 0:
            x = -1 * c / b
            y1 = cy + math.sqrt(r ** 2 - (x - cx) ** 2)
            y1 = cy - math.sqrt(r ** 2 - (x - cx) ** 2)
            return (x, y1), (x, y2)
        y1 = cy + math.sqrt(r ** 2 + (b / a + c / a + cx) ** 2)
        y2 = cy - math.sqrt(r ** 2 + (b / a + c / a + cx) ** 2)
        
        x1 = -1 * (b * y1 + c) / a
        x2 = -1 * (b * y2 + c) / a
        return (x1, y1), (x2, y2)
    
    # タプル形式で表される２次元ベクトルから外積を計算
    def __culc_outer_product(self, vec1, vec2):
        return vec1[0] * vec2[1] - vec1[1] * vec2[0]

        
    
    # Playerクラスの位置と大きさ、Packクラスの位置と、大きさと速度を渡し、パックの移動中にプレイヤーと衝突するかを判定
    # 衝突すると判明した場合、パックの位置を衝突する瞬間に移動させる。
    # 返り値は修正後のパックの位置情報を格納したタプルで衝突しない場合は負の値が入ったものを返す。
    def __check_hit_with_player(self, pack_speed, pack_position, pack_size, player_position, player_size):
        (a, b, c) = self.__culc_linear_function(player_position, moved_pack_position)
        NESS_DIS = pack_size + player_size
        moved_pack_position = (pack_position[0] + pack_speed[0], pack_position[1] + pack_speed[1])

        dis = self.__culc_distance_of_line_and_point(a, b, c, player_position)
        border1 = -b * pack_position[0] + a * pack_position[1] 
        border2 = -b * moved_pack_position[0] + a * moved_pack_position[1] 
        temp = -b * player_position[0] + a * player_position[1]

        if dis <= NESS_DIS and (border1 - temp) * (border2 - temp) >= 0:
            # パックの位置の修正
            (intersec1, intersec2) = self.__culc_intersection_of_circle_and_linear
            dis1 = self.__culc_distance_of_two_points(pack_position, intersec1)
            dis2 = self.__culc_distance_of_two_points(pack_position, intersec2)
            if dis1 < dis2 :
                return intersec1
            else :
                return intersec2
        
        dis  =self.__culc_distance_of_two_points(moved_pack_position, player_position)
        if dis <= NESS_DIS :
            # パックの位置の修正
            (intersec1, intersec2) = self.__culc_intersection_of_circle_and_linear
            dis1 = self.__culc_distance_of_two_points(pack_position, intersec1)
            dis2 = self.__culc_distance_of_two_points(pack_position, intersec2)
            if dis1 < dis2 :
                return intersec1
            else :
                return intersec2
        
        return -1, -1
    

    # 線分ABと線分CDの考査判定をベクトルの外積を利用して行い、真理値を返す
    # a,b,c,dはそれぞれタプル形式で現れる線分の端点の座標
    def __check_cross_of_two_linear(self, a, b, c, d):
        ab = (b[0] - a[0], b[1] - a[1])
        ac = (c[0] - a[0], c[1] - a[1])
        ad = (d[0] - a[0], d[1] - a[1])
        cd = (d[0] - c[0], d[1] - c[1])
        ca = (a[0] - c[0], a[1] - c[1])
        cb = (b[0] - c[0], b[1] - c[1])

        outer_of_ab_and_ac= self.__culc_outer_product(ab, ac)
        outer_of_ab_and_ad= self.__culc_outer_product(ab, ad)
        outer_of_cd_and_ca= self.__culc_outer_product(cd, ca)
        outer_of_cd_and_cb= self.__culc_outer_product(cd, cb)

        if outer_of_ab_and_ac * outer_of_ab_and_ad <= 0 and outer_of_cd_and_ca * outer_of_cd_and_cb <= 0:
            return True
        else :
            return False
    
    # パックとプレイヤーの衝突に関する処理を行う
    def __process_hit_with_player(self, pack, player):
        pack_speed = pack.get_speed()
        pack_position = pack.get_position()
        pack_size = pack.get_size()
        player_position = player.get_position()
        player_size = player.get_size()

        hit_pack_position = self.__check_hit_with_player(pack_speed, pack_position, pack_size, player_position, player_size)
        # 衝突するかの判定
        if hit_pack_position[0] == -1 and hit_pack_position[1] == -1:
            return False
        # 衝突したときの位置の修正の処理
        x = math.floor(hit_pack_position[0])
        y = math.floor(hit_pack_position[1])
        pack.set_position((x, y))
        player_speed = player.get_speed()
        pack.hit_player(player_speed, player_position)
        return True
    
    # ４法の壁との衝突判定を行い、衝突するなら位置を調整する。
    # フィールドの座標は左上を(0,0)とすることを想定
    # 衝突の判定は線分の交差判定を利用
    def __process_hit_with_wall(self, pack):
        pack_speed = pack.get_speed()
        pack_position = pack.get_position()
        pack_size = pack.get_size()

        FIELD_POINT = [(pack_size, pack_size), (self._WIDTH - pack_size, pack_size), (self._WIDTH - pack_size, self._HEIGHT - pack_size), (pack_size, self._HEIGHT - pack_size)]
        moved_pack_position = (pack_position[0] + pack_speed[0], pack_position[1] + pack_speed[1])
        position_after_hit = [pack_position[0], pack_position[1]]
        hit_flag = False
        
        print(pack_speed)

        for i in range(4):
            # 壁と衝突するかの判定
            if self.__check_cross_of_two_linear(pack_position, moved_pack_position, FIELD_POINT[i], FIELD_POINT[(i + 1) % 4]):
                hit_flag = True
                (a, b, c) =self.__culc_linear_function(pack_position, moved_pack_position)
                if FIELD_POINT[i][0] == FIELD_POINT[(i + 1) % 4][0]:
                    pack.refrect(False)
                    if b == 0 :
                        continue
                    position_after_hit[0] = FIELD_POINT[i][0]

                    if pack.get_speed()[0] < 0:
                        position_after_hit[0] -= 1
                    else :
                        position_after_hit[0] += 1

                    if a == 0:
                        position_after_hit[1] = -1 * c / b
                    else:
                        position_after_hit[1] = -1 * (a * FIELD_POINT[i][0] + c) / b

                elif FIELD_POINT[i][1] == FIELD_POINT[(i + 1) % 4][1]:
                    pack.refrect(True)      

                    if a == 0:
                        continue
                    position_after_hit[1] = FIELD_POINT[i][1]

                    
                    if pack.get_speed()[1] < 0:
                        position_after_hit[1] -= 1
                    else :
                        position_after_hit[1] += 1
                        
                    
                    
                    if b == 0:
                        position_after_hit[0] = -1 * c / a
                    else :
                        position_after_hit[0] = -1 * (b * position_after_hit[1] + c) / a
                
                pack.set_position(position_after_hit)
                
        return hit_flag


    #パックと壁もしくはプレイヤーとの衝突処理を行う。
    def process_hit_and_move(self):
        for pack in self._packs:
            flag = False
            for player in self._players:
                # パックとプレイヤーの衝突処理
                if self.__process_hit_with_player(pack, player):
                    break
            if flag :
                continue
                
            # パックと壁の衝突処理
            if self.__process_hit_with_wall(pack):
                continue

            pack.move()
        
    def get_entity_list(self):
        rel = []

        for pack in self._packs:
            ID = pack.get_id()
            position = pack.get_position()
            size = pack.get_size()
            rel.append((ID,position,size))
        
        for player in self._players:
            ID = player.get_id()
            position = player.get_position()
            size = player.get_size()
            rel.append((ID,position,size))
        
        return rel

            



            
            


            


    


            

        