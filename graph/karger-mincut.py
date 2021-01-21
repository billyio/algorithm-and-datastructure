# https://github.com/RoyWang21/Algorithm_1_Coursera_Stanford/blob/master/Mincut.py
import random
import sys

def find_rand_edge(G1):	
	temp = random.randint(1, (num - len(G1))) 
	row = 0
	for x in [len(y) - 1 for y in G1]:
		temp -= x
		if temp <= 0:
			return [G1[row][0], G1[row][x + temp]]
		row += 1

def merge_vertices(G1,choice):
	v1, v2 = int(choice[0]), int(choice[1])
	for z in range(G1[v1 - 1].count(v2)):			
		G1[v1 - 1].remove(v2)

	for x in G1[v2 - 1]:
		if x != v1 and x != v2:
			#print(f"x = {x}, v1 = {v1}")
			G1[v1 - 1].append(x)
	G1[v2 - 1].clear()

	for y in range(len(G1)): 
		if v2 in G1[y]:
			for z in range(G1[y].count(v2)):			
				G1[y].remove(v2)
				G1[y].append(v1)
	G1[v2 - 1].append(v2)
	return G1

#--------------------------------------------------
mincut = sys.maxsize
G_original = []
temp = []

# with open('SampleCut.txt','r') as f:
with open('graph/kargerMinCut.txt','r') as f:
	G_original=[x.strip().split('\t') for x in f] 

for iter in range(50):

	G1 = [[int(num) for num in item] for item in G_original] 

	num = sum(len(x) for x in G1)

	left_len = [len(y) - 1 for y in G1]
	# print(G1)
	while left_len[2] > 0:
		num = sum(len(x) for x in G1)
		choice = find_rand_edge(G1)
		choice.sort()
		#print(f"  Choose: Vertex_1 = {choice[0]}, Vertex_2 = {choice[1]}")

		G1 = merge_vertices(G1, choice)

		left_len = [len(y) - 1 for y in G1]
		left_len.sort()
		left_len.reverse()

	# print(f"-- Cut number for iteration {iter} = {left_len[0]}")

	if mincut > left_len[0]:
		mincut = left_len[0]

print(f"----- Mincut = {mincut}")