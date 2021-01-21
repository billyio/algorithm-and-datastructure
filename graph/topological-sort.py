from collections import deque, defaultdict

N, M = map(int, input().split())
ab = []
for _ in range(N + M - 1):
    ab.append(tuple(map(int, input().split())))

in_cnt = defaultdict(int)
outs = defaultdict(list)
for a, b in ab:
    in_cnt[b - 1] += 1
    outs[a - 1].append(b - 1)

res = []
queue = deque([i for i in range(N) if in_cnt[i] == 0])
while len(queue) != 0:
    v = queue.popleft()
    res.append(v)
    for v2 in outs[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            queue.append(v2)


# https://yottagin.com/?p=6359
def topological_sort_bfs(graph):
    # トポロジカルソートした結果を蓄積する空リスト
    topological_sorted_list = []
    queue = collections.deque()
    # 入力辺を持たないすべてのノードの集合
    for vertex in graph:
        indegree = vertex.get_indegree()
        if indegree == 0:
            queue.append(vertex)
    # while S が空ではない do
    while len(queue) > 0:
        # S からノード n を削除する
        current_vertex = queue.popleft()
        # L に n を追加する
        topological_sorted_list.append(current_vertex.get_vertex_id())
        # for each n の出力辺 e とその先のノード m do
        for neighbor in current_vertex.get_connections():
            # 辺 e をグラフから削除する
            neighbor.set_indegree(neighbor.get_indegree() - 1)
            # if m がその他の入力辺を持っていなければ then
            if neighbor.get_indegree() == 0:
                # m を S に追加する
                queue.append(neighbor)
    if len(topological_sorted_list) != len(graph.get_vertices()):
        print("Kahn's algorithm:", '閉路があります。DAGではありません。')
    else:
        print("Kahn's algorithm tological sorted list:", topological_sorted_list)