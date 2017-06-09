# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirrorSame(root.left, root.right)
        
    def mirrorSame(self, a, b):
        if not a and not b:
            return True
        elif a and b:
            return a.val == b.val and self.mirrorSame(a.left, b.right) and self.mirrorSame(a.right, b.left)
        else:
            return False
