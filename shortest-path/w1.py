import numpy as np


def readgraph(file):
    f = open(file, 'r')
    f.readline()
    g = {i: {} for i in range(1, 1001)}
    ls = f.readline()
    while ls:
        data = list(map(int, ls.split(' ')))
        g[data[0]][data[1]] = data[2]
        ls = f.readline()
    f.close()
    return g


g1 = readgraph('sample-data/g1.txt')
g2 = readgraph('sample-data/g2.txt')
g3 = readgraph('sample-data/g3.txt')


def askmin(g):
    n = 1000
    A = np.zeros([n, n, n])
    for i in range(n):
        for j in range(n):
            A[i, j, 0] = 0 if i == j else g[i+1][j+1] if j+1 in g[i+1] else np.inf
    for k in range(1, n):
        if k % 100 == 0:
            print(k)
        for i in range(n):
            for j in range(n):
                A[i, j, k] = min(A[i, j, k-1], A[i, k, k-1]+A[k, j, k-1])
    for i in range(n):
        if A[i, i, n-1] < 0:
            print('error at %i' % (i+1))
    print('min=%i' % A[:, :, n-1].min())


print('g1')
askmin(g1)
min=-2071316704362602850764451004124039207993124859771173604577175248860775411028888922664524986188001790136114155283438314033691018392021047994731790457806377243835009479894659117406571018059776

print('g2')
askmin(g2)
min=-3899702161487579445697468714183694474757193767112950599934066599841558021597174060881825621692985562330024072811163886203876136521954175232371611332763598101631790481408

print('g3')
askmin(g3)
min=-19