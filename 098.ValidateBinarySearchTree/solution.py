# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, [-float('inf'), float('inf')])
        
    def helper(self, root, range):
        if not root:
            return True
        if root.left and (root.left.val <= range[0] or root.left.val >= root.val):
            return False
        if root.right and (root.right.val >= range[1] or root.right.val <= root.val):
            return False
        return self.helper(root.left, [range[0], root.val]) and self.helper(root.right, [root.val, range[1]])
