# https://leetcode.com/problems/validate-binary-search-tree/solution/

# recursive traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))
        
        return validate(root)

# iterative traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
            
        stack = [(root, -math.inf, math.inf)] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True 

# recursive inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
        
        self.prev = -math.inf
        return inorder(root)

# iterative inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
