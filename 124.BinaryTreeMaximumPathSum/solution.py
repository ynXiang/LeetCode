# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
        
    # @return maximum path to root, maximum path    
    def helper(self, root):
        if not root:
            return 0, -float('inf')
        lmptr, lmp = self.helper(root.left)
        rmptr, rmp = self.helper(root.right)
        return max(lmptr, rmptr, 0) + root.val, max(lmp, rmp, max(lmptr, 0) + root.val + max(rmptr, 0))
