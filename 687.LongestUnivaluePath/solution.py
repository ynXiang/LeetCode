# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = set()
        h.add(root)
        print root.right in h
        return self.helper(root)[1]        
        
    def helper(self, root):
        if not root:
            return 0, 0 #maxLen, maxPath
        lLen, lPath = self.helper(root.left)
        rLen, rPath = self.helper(root.right)
        lLen = lLen if lLen > 0 and root.left.val == root.val else 0
        rLen = rLen if rLen > 0 and root.right.val == root.val else 0
        return max(lLen, rLen) + 1, max(lPath, rPath, lLen + rLen)
