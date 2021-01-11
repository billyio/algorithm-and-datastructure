from collections import defaultdict 

N,M = map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  
    dict[a].add(b)
    dict[b].add(a)

color = [0 for i in range(N+1)]
res = 'Yes'

def dfs(v,c,queue=[]):
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:
            res = 'No'
        elif i not in queue:
            color[i] = c*-1
            dfs(i,-c,queue)

color[1] = 1
(dfs(1,1))
print(res)


# ver2
from collections import deque, defaultdict

N,M = list(map(int,input().split()))
G = defaultdict(set)

color = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

color[1] = 1
que = deque([1])
bipartite = True

while len(que):
    p = que.popleft()
    for q in list(G[p]):
        if color[q] == 0:
            color[q] = -color[p]
            que.append(q)
        elif color[q] == color[p]:
            bipartite = False
            break

print(bipartite)