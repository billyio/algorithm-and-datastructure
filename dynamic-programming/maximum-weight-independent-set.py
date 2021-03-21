f = open('sample-data/mwis.txt', 'r')
path = list(map(int, f.readlines()))
f.close()

mwis = [0]*1001
solution = [[] for i in range(1001)]
mwis[0] = 0
mwis[1] = path[1]
solution[1] = [1]

for i in range(2, 1001):
    mwis[i] = max(mwis[i-2]+path[i], mwis[i-1])
    if mwis[i-2]+path[i] > mwis[i-1]:
        solution[i] = solution[i-2]+[i]
    else:
        solution[i] = solution[i-1].copy()
    
ans = solution[-1]
print(ans)
ask = [1, 2, 3, 4, 17, 117, 517, 997]
ans = ['1' if i in solution[-1] else '0' for i in ask]
print(''.join(ans))