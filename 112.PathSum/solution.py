# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return sum in self.hasPathSumHelp(root)
        
    def hasPathSumHelp(self, root):
        if not root:
            return []
        rootl = [root.val] if not root.left and not root.right else []
        return [root.val+i for i in self.hasPathSumHelp(root.left) + self.hasPathSumHelp(root.right)] + rootl
