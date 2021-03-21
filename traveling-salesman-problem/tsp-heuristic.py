# https://github.com/sh2439/Algo_stanford/blob/master/C4:%20Shortest%20Path%20Revisited%2C%20NP-Complete/tsp_heuristic.py

import numpy as np

def read_file(name):
    """Given the path/name of the file, return the graph (dictionary).
    """
    file = open(name,'r')
    data = file.readlines()
    
    # initialize the graph
    graph = {}
    #num = int(data[0][0])
    for line in data[1:]:
        item = line.split()
        graph[int(item[0])] = (float(item[1]), float(item[2]))
        
    return graph
        

def euclidean_sq(a,b):
    """Return the square euclidean distance of a(x1,y1) and b(x2,y2)
    """
    dis = (a[0] - b[0])**2 + (a[1]- b[1])**2
    return dis


def tsp(graph):
    """Given the graph, return the heuristic traveling salesman problem value.
    """
    # number of cities
    num = len(graph)
    
    # Initialize visited and unvisited set
    visited = []
    visited.append(1)
    
    unvisited = list(range(2, len(graph)+1))
    
    final_dis = 0
    # Main loop: stop when all the cities are visited.
    for i in range(num-1):
        
        current_city = visited[-1]
        next_city = unvisited[0]
        
        min_dis = euclidean_sq(graph[current_city], graph[next_city])
    
        if len(unvisited)>1:
            for j in unvisited[1:]:
                dis = euclidean_sq(graph[current_city], graph[j])
                if dis < min_dis:
                    min_dis = dis
                    next_city = j
                # break the tie
                elif dis == min_dis:
                    next_city = min(next_city, j)
            
        visited.append(next_city)
        unvisited.remove(next_city)
        final_dis += np.sqrt(min_dis)
        
    final_dis += np.sqrt(euclidean_sq(graph[visited[-1]], graph[1]))
    
    return final_dis
        

def main():
    graph = read_file('sample-data/tsp-large.txt')
    best_dis = tsp(graph)
    
    print(best_dis)


if __name__ == '__main__':
    main()