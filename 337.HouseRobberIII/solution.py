# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
    
    def helper(self, root):
        if not root:
            return 0, 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        return max(l[1] + r[1] + root.val, l[0] + r[0]), l[0] + r[0]
