# ノード間のコストが行列で渡される → プリム法
# 2点のノードとそのコストの組み合わせで渡される → クラスカル法

import heapq

n = int(input())

next = []   # 隣接管理のリスト
for _ in range(n):
    l = list(map(int, input().split()))
    next.append([(c, i) for i, c in enumerate(l) if c != -1])

visited = [0] * n
connection = 0
q = [(0, 0)]    # (cost, v)
heapq.heapify(q)
ans = 0

while len(q):
    cost, v = heapq.heappop(q)
    if visited[v]:
        continue

    visited[v] = 1
    connection += 1
    ans += cost

    # 新たに繋げたノードから行けるところをエンキュー
    for i in next[v]:
        heapq.heappush(q, i)

    # 全部のノードが繋がったら終了
    if connection == n:
        break
    
print(ans)