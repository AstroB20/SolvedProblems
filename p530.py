# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_diff = float('inf')
        prev_val = None 
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left  
            
            root = stack.pop()
            if prev_val is not None:
                min_diff = min(min_diff, root.val - prev_val)
            prev_val = root.val
            
            root = root.right 
        
        return min_diff
