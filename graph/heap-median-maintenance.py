# https://docs.python.org/ja/3/library/heapq.html

import heapq

with open('sample-data/Median.txt') as f:
    nums = [int(x) for x in f]

sort_a = []
median = []

for i in range(1,len(nums)+1):
    sorted_a = heapq.nsmallest(i,nums[:i])
    if i % 2 == 0:
        median.append(sorted_a[i//2 - 1])
    else:
        median.append(sorted_a[(i+1)//2 - 1])

mode = sum(median) % len(nums)
print(mode)