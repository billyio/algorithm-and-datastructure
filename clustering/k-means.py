# from scratch
# https://github.com/SSQ/Coursera-Stanford-Greedy-Algorithms-Minimum-Spanning-Trees-and-Dynamic-Programming/blob/master/Programming%20Assignment%202/Cluster%201.ipynb
import numpy as np

file_path = "sample-data/clustering1.txt"
X = np.loadtxt(file_path, dtype=int)

clusters = {}
for x in range(1,501):
    clusters[x] = [x]

# sort the distance of nodes
sorted_X = np.argsort(X[:,2], axis=0) 

k = 4

# d: dictionary, k: key
def get_key_by_value(d, k):
    for leader, nodes in d.items():
        if k in nodes:
            return leader

# c: dictionary. cluster , a: key. added value in dict, d: key. deleted value in dict
def update_cluster(c, a, d):
    c[a].extend(c[d])
    del c[d]

iteration = 0

print('whole_edges: ')
print(len(sorted_X))

# core algorithm
for i in sorted_X:
    min_edge = X[i,:]
    # print("minedge",min_edge)
    key1 = get_key_by_value(clusters, min_edge[0])
    key2 = get_key_by_value(clusters, min_edge[1])
    if key1 == key2:
        continue
    elif len(clusters[key1]) >= len(clusters[key2]):
        update_cluster(clusters, key1, key2)
    else:
        update_cluster(clusters, key2, key1)

    if len(clusters) == k:
        break
        
print(clusters)

clusters_keys = list(clusters.keys()) # [102, 384, 414, 462]
print("cluster keys", clusters_keys)

# initialize 
spacing = []

distance=0
# set all spacing of k-clusters
for i in range(len(clusters_keys)-1):
    j = i+1
    for k in range(j, len(clusters_keys)):
        spacing.append([clusters_keys[i], clusters_keys[k], distance])
spacing = np.array(spacing)
print('spacing: ')
print(spacing)

def min_distance(X, clusters, cluster1, cluster2):
    minimum = X[:,2].max()
    for i in clusters[cluster1]:
        for j in clusters[cluster2]:
            if i < j:
                find_position = np.all([X[:,0]==i, X[:,1]==j], axis=0)
                find_edge = np.argwhere(find_position==True)
                actural_position = find_edge[0][0]
                distance = X[actural_position, 2]
                if minimum > distance:
                    minimum = distance
            else:
                find_position = np.all([X[:,0]==j, X[:,1]==i], axis=0)
                find_edge = np.argwhere(find_position==True)
                actural_position = find_edge[0][0]
                distance = X[actural_position, 2]
                if minimum > distance:
                    minimum = distance
    return minimum


for i in range(len(spacing)):
    spacing[i,2] = min_distance(X, clusters, spacing[i,0], spacing[i,1])

print('spacing: ')
print(spacing)
print('max distance clusters: ')
print(spacing[np.argmax(spacing[:,2]), :])
print('max distance: ')
print(np.amax(spacing[:,2]))