# O(EV)
def bellman_ford(s):
    d = [float('inf')] * n 
    d[s] = 0 
    for i in range(n):
        update = False
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d

n, w = [int(x) for x in input().split()] # n:頂点数, w:辺の数
g = []
for _ in range(w):
    # x:始点, y:終点, z:コスト
    x, y, z = [int(x) for x in input().split()] 
    g.append([x, y, z])
    g.append([y, x, z]) # 有向グラフでは削除
    
print(bellman_ford(0))