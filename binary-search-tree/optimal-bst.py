# https://github.com/thinklancer/code_algorithm/blob/master/q3q5.py
# week4 problem 

import numpy as np

# calculate the average search time of bianry search tree
def calOBS(w):
    n = len(w)
    m = np.zeros([n,n])
    for s in np.arange(n):
        for i in np.arange(n-s):
            temp = np.zeros(s+1)
            for j in np.arange(s+1):
                r = i+j
                up = min([n-1,i+s])
                temp[j] = sum(w[i:up+1])
                if i<=r-1:
                    temp[j] += m[i,r-1]
                if i+s<n and r+1<= i+s:
                    temp[j] += m[r+1,i+s]
            m[i,i+s]=min(temp)
    return m[0,-1]


if __name__ == "__main__":
    # weight = [0.05,0.4,0.08,0.04,0.1,0.1,0.23]
    weight = [0.2,0.05,0.17,0.1,0.2,0.03,0.25]
    print(calOBS(weight))