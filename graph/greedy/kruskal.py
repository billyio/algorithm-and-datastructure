V, E = map(int, input().split())

from collections import defaultdict

# 参考：　https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(V)

# 辺のコスト（w）をソート
edges = []
for _ in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))
edges.sort()

# 「閉路ができる」＝「既に2点が繋がっているところに辺を作る」なのでUnionFind木で確認
cost = 0
for edge in edges:
    w, s, t = edge
    if not uf.same(s, t):
        cost += w
        uf.union(s, t)
        
print(cost)