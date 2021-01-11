# https://tjkendev.github.io/procon-library/python/geometry/closest_pair.html

# input sample
# n
# x0 y0
# x1 y1
# :
# xn−1 yn−1

# 最近点対を分割統治法で求める
from math import sqrt
INF = 10**9

# cp_rec - 再帰用関数
# 入力: 配列と区間
# 出力: 距離と区間内の要素をY座標でソートした配列
def cp_rec(ps, i, n):
    if n <= 1:
        return INF, [ps[i]]
    m = n/2
    x = ps[i+m][0] # 半分に分割した境界のX座標
    # 配列を半分に分割して計算
    d1, qs1 = cp_rec(ps, i, m)
    d2, qs2 = cp_rec(ps, i+m, n-m)
    d = min(d1, d2)
    # Y座標が小さい順にmergeする
    qs = [None]*n
    s = t = idx = 0
    while s < m and t < n-m:
        if qs1[s][1] < qs2[t][1]:
            qs[idx] = qs1[s]; s += 1
        else:
            qs[idx] = qs2[t]; t += 1
        idx += 1
    while s < m:
        qs[idx] = qs1[s]; s += 1
        idx += 1
    while t < n-m:
        qs[idx] = qs2[t]; t += 1
        idx += 1
    # 境界のX座標x(=ps[i+m][0])から距離がd以下のものについて距離を計算していく
    # bは境界のX座標から距離d以下のものを集めたもの
    b = []
    for i in range(n):
        ax, ay = q = qs[i]
        if abs(ax - x) >= d:
            continue
        # Y座標について、qs[i]から距離がd以下のj(<i)について計算していく
        for j in range(len(b)-1, -1, -1):
            dx = ax - b[j][0]
            dy = ay - b[j][1]
            if dy >= d: break
            d = min(d, sqrt(dx**2 + dy**2))
        b.append(q)
    return d, qs

def closest_pair(ps):
    n = len(ps)
    return cp_rec(ps, 0, n)[0]


# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/

import math 
import copy 

class Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def stripClosest(strip, size, d): 
    min_val = d
    for i in range(size): 
        j = i + 1
        while j < size and (strip[j].y - 
                            strip[i].y) < min_val: 
            min_val = dist(strip[i], strip[j]) 
            j += 1
  
    return min_val  
  
def closestUtil(P, Q, n): 
    if n <= 3:  
        return bruteForce(P, n)  
    mid = n // 2
    midPoint = P[mid]
    dl = closestUtil(P[:mid], Q, mid) 
    dr = closestUtil(P[mid:], Q, n - mid)  
  
    d = min(dl, dr) 
  
    strip = []  
    for i in range(n):  
        if abs(Q[i].x - midPoint.x) < d:  
            strip.append(Q[i]) 
  
    return min(d, stripClosest(strip, len(strip), d)) 
  
def closest(P, n): 
    P.sort(key = lambda point: point.x) 
    Q = copy.deepcopy(P) 
    Q.sort(key = lambda point: point.y)     

    return closestUtil(P, Q, n) 
  
# Driver code 
P = [Point(2, 3), Point(12, 30), 
     Point(40, 50), Point(5, 1),  
     Point(12, 10), Point(3, 4)] 
n = len(P)  
print("The smallest distance is", closest(P, n)) 