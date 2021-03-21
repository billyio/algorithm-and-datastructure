import random
import numpy as np

# union find with path compression
class union_find_pc(object):    
    def __init__(self, nodes):
        self.parent = [i for i in range(len(nodes))]
        self.rank = [0 for i in range(len(nodes))]
        self.clusters = set([i for i in range(len(nodes))])
        
    def FIND(self, x):           
        n = x
        
        while self.parent[n] != n:
            n = self.parent[n]
            
        self.parent[x] = n   
        return n
     
    def UNION(self, a, b):   
        
        a = self.FIND(a)
        b = self.FIND(b)
        if (a == b):
            return 
        
        if (self.rank[a] == self.rank[b]):
            # make a the parent of b and all its object            
            flip = random.random() > 0.5
            if flip==1:
                self.parent[b] = a                             
                self.rank[a] += 1
            else:
                self.parent[a] = b                             
                self.rank[b] += 1
                
        elif (self.rank[a] > self.rank[b]):
            # make a the parent of b and all its object
            self.parent[b] = a                             
        else:
            self.parent[a] = b 
            
    def getClusters(self):
        n_clusters = []
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                n_clusters.append(i)
        return n_clusters

FILE = "sample-data/clustering1.txt"
K =  4 
fp = open(FILE, 'r')

n_nodes = int(fp.readline())

edges = []
vertices = set()
MAX_WEIGHT = 0

for row in fp.readlines():
    r = row.strip().split(" ")
    
    vertices.add(int(r[0]))
    vertices.add(int(r[1]))
    weight = int(r[2])
    if weight > MAX_WEIGHT:
        MAX_WEIGHT = weight
        
    edges.append([int(r[0]),int(r[1]), int(r[2])])
    
# weight（距離）小→大、ソート
sortedEdges = sorted(edges, key=lambda x: x[2])
print("sortedEdges", sortedEdges[:10])

vertices = list(vertices)
v_to_idx = {vertices[i]:i for i in range(len(vertices))}
# print("v_to_idx", v_to_idx)

obj = union_find_pc([i for i in range(n_nodes)])
# print("obj", obj)

for i, edge in enumerate(sortedEdges):
    v1 = v_to_idx[edge[0]]
    v2 = v_to_idx[edge[1]]
    w = edge[2]
    # print(i, edge, v1, v2, w)
    
    obj.UNION(v1, v2)
    
    if len(obj.getClusters()) == 4:
        print ("final Clusters", obj.getClusters())
        break
        
minW = MAX_WEIGHT
for i, edge in enumerate(sortedEdges):  
    v1 = v_to_idx[edge[0]]
    v2 = v_to_idx[edge[1]]
    w = edge[2]
    
    if obj.FIND(v1) != obj.FIND(v2):
        if w < minW:
            minW = w
print ("maximum spacing", minW)
# 106