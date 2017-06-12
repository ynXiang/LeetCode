# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.minDepthHelp(root)
        
    def minDepthHelp(self, root):
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepthHelp(root.right) + 1
        elif not root.right:
            return self.minDepthHelp(root.left) + 1
        else:
            return min(self.minDepthHelp(root.left), self.minDepthHelp(root.right)) + 1
