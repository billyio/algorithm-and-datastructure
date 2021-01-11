https://leetcode.com/problems/maximum-depth-of-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def maxDepth1(self, root):
    deque, depth = collections.deque(), 0
    if root:
        deque.append(root)
    while deque:
        size = len(deque)
        for _ in range(size):
            node = deque.popleft()
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        depth += 1
    return depth