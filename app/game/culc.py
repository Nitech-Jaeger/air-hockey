import math
import sympy as sp


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
    x, y = sp.symbols('x y')
    circle_eq = (x - cx) ** 2 + (y - cy)**2 - r **2
    line_eq = a * x + b * y + c
    solutions = sp.solve([circle_eq,line_eq],(x, y))

    return solutions[0], solutions[1]

# タプル形式で表される２次元ベクトルから外積を計算
def culc_outer_product(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]

# ２次元空間における二つの座標からその２点を結んだ直線に対する法線ベクトルを計算
def culc_normal_vec(pos1, pos2):
    (a, b, c) = culc_linear_function(pos1, pos2)
    scale = math.sqrt(a * a + b* b)
    normal_vec = (a / scale, b / scale)
    
    return normal_vec

# タプル形式で表される２次元ベクトルから内積を計算
def culc_inner_product(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]

    