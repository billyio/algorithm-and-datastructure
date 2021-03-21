import random

def read_file(path):
    file = open(path, 'r')
    data = file.readlines()
    
    num_nodes = 500
    
    graph = [[] for i in range(num_nodes+1)]
    for line in data[1:]:
        item = line.split()
        graph[int(item[0])] += [(int(item[1]), int(item[2]))]
        graph[int(item[1])] += [(int(item[0]), int(item[2]))]

    return graph


def Prim_MST(graph):
    X = set()

    X.add(random.choice([i for i in range(1,len(graph))]))
    ans = 0
    
    while (len(X) < len(graph)-1):
        edge = {}
        
        for node in X:
            for v in graph[node]:
                if v[0] not in X:
                    edge[(node, v[0])] = v[1]

        # find the shortest edge
        (u,v),dist = min(edge.items(), key = lambda x : x[1])
    
        X.add(v)
        ans += dist

    return ans

graph = read_file('sample-data/edges.txt')
ans = Prim_MST(graph)
print(ans)
