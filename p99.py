# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        curr = root

        while curr:
            if curr.left is None:

                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right

            else:
            
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right

                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:

                    pre.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr
                    prev = curr

                    curr = curr.right
        first.val, second.val = second.val, first.val
