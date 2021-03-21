# https://zehnpaard.hatenablog.com/entry/2018/06/26/201512
# v:ノードの数、n:辺の数、es:各辺を表す親ノード、小ノードのペア

# outs: 各ノードから出ていく先のノードのリストの辞書
# ins: 各ノードの入次数の辞書

# q: 入次数が0のノードのキュー
# res: 求める答え。各頂点の親を出力、木の根なら0を出力

# キューの頭のノードを取り出し、ソートされたリストの次のメンバとしてappend
# そのノードから伸びる各辺について
#   その行き先のノードの入次数を１減らし
#   もしそのノードの入次数が0に落ちたらキューに入れる

# outsとinsの作成にO(E)、qの作成にO(V)
# resの作成のループはO(V+E)（外側のループがO(V)回、内側のループは合計でO(E)回）
# 全体的にO(E+V)の計算量


from collections import defaultdict, deque

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

print(outs)
print(ins)

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    print(q)
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

print(res)