# file_path = 'sample-data/knapsack1.txt'
file_path = 'sample-data/knapsack_big.txt'
lines = []
with open(file_path, 'r') as f:
        for line in f:
            parts = list(map(int, line.split()))
            lines.append(parts)
W, N = lines[0]
data = lines[1:]
# print(data)
f.close()

w = []
v = []
for x, y in data:
    v.append(x)
    w.append(y)

dp = [[0]*(W+1) for j in range(N+1)] 

for i in range(N):
    print(i)
    for j in range(W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])

print(dp[N][W])