import time
import pickle
 
class Heap:
    def __init__(self, size):
        self.heap = [None for _ in range(size+1)]
        self.max_size = size + 1
        self.size = 0
 
    def downheap(self, src, dst):
        value = self.heap[src]
        i = src
        while i <= int(dst / 2):
            j = i * 2
            if j+1 <= dst and self.heap[j] < self.heap[j+1]:
                j += 1
            if value >= self.heap[j]:
                break
            self.heap[i] = self.heap[j]
            i = j
        self.heap[i] = value
 
    def deletemin(self):
        if self.size < 1:
            print("Heap is empty.")
            return
        value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
 
        self.downheap(1, self.size)
        return value
 
    def upheap(self, size):
        value = self.heap[size]
        while size > 1 and self.heap[int(size/2)] < value:
            self.heap[size] = self.heap[int(size/2)]
            size = int(size/2)
        self.heap[size] = value
 
    def insert(self, value):
        if self.size >= self.max_size:
            print("heap is overflow.")
            return
        self.size += 1
        self.heap[self.size] = value
        self.upheap(self.size)
 
    def heap_sort(self):
        for i in range(self.size, 1, -1):
            tmp = self.heap[1]
            self.heap[1] = self.heap[i]
            self.heap[i] = tmp
            self.downheap(1, i-1)
 
 
h = Heap(len(lst))
for i in lst:
    h.insert(i)

h.heap_sort()