# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        total = 0
        stack = [(root, 0)]
        
        while stack:
            node, current = stack.pop()
            current = current * 10 + node.val
            
            if not node.left and not node.right:  # leaf
                total += current
            
            if node.left:
                stack.append((node.left, current))
            if node.right:
                stack.append((node.right, current))
        
        return total
        