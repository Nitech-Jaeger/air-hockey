import math

# タプルの形で渡された２点間の距離を返す
def culc_distance_of_two_points(pos1, pos2):
    dis = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
    dis = math.sqrt(dis)
    return dis

# 点と直線の距離を返す。
# 直線はax+by+c=0の形で渡され、点はタプルで渡される。
def culc_distance_of_line_and_point(a, b, c, point):
    temp = a * point[0] + b * point[1] + c 
    if temp < 0 :
        temp *= -1
    return temp / math.sqrt( a ** 2 + b ** 2)

# タプルの形式で渡される２点を通る直線の式をax+by+c=0の形で求める。
def culc_linear_function(pos1, pos2):
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
def culc_intersection_of_circle_and_linear(a, b, c, cx, cy, r):
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
def culc_outer_product(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]

# ２次元空間における二つの座標からその２点を結んだ直線に対する法線ベクトルを計算
def culc_normal_vec(pos1, pos2):
    n_x = pos1[0] - pos2[0]
    n_y = pos1[1] - pos2[1]
    scale_n = (n_x * n_x + n_y * n_y)
    scale_n = math.sqrt(scale_n)
    normal_vec = (n_x / scale_n, n_y / scale_n)
    return normal_vec

# タプル形式で表される２次元ベクトルから内積を計算
def culc_inner_product(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]

    