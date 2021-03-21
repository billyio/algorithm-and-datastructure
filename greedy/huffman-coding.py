# https://gside.org/blog/2019/12/15/
class Node():
	def __init__(self, node, freq):
		self.freq = freq
		self.node_list = []
		self.node_list.append(node)
	
	def extend(self, node):
		self.node_list.extend(node.node_list)

	def __lt__(self, other):
		return self.freq < other.freq

from heapq import heappush, heappop

def huffman(nodes):
	huffmanQueue = []
	ans = {}

    # 優先度つきキューにノードを格納する
	for node in nodes:
		heappush(huffmanQueue, (node.freq, node))

	while len(huffmanQueue) > 1:
		(leftFreq, leftNode) = heappop(huffmanQueue)
		(rightFreq, rightNode) = heappop(huffmanQueue)
		
	
	# 一番頻度が少ないノードに'0'を追加
	for s in leftNode.node_list:
		ans[s] = '0' + ans.get(s, '')

	# 二番目に頻度が少ないノードに'1'を追加
	for s in rightNode.node_list:
		ans[s] = '1' + ans.get(s, '')

	totalFreq = leftFreq + rightFreq
	leftNode.extend(rightNode)
	heappush(huffmanQueue, (totalFreq, leftNode))

	return ans

# nodes = [Node('a', 320), Node('b', 250), Node('c', 200), Node('d', 180), Node('e', 50)]
nodes = [Node('a', 280), Node('b', 270), Node('c', 200), Node('d', 150), Node('e', 100)]

print(huffman(nodes))