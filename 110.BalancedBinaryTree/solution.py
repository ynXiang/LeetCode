# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans, _ = self.isBalancedHelp(root)
        return ans
        
    def isBalancedHelp(self, root):
        if not root:
            return True, 0
        lb, ld = self.isBalancedHelp(root.left)
        rb, rd = self.isBalancedHelp(root.right)
        return lb and rb and abs(ld-rd) <= 1, max(ld, rd)+1
