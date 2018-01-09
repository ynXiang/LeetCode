# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root, p, q)[1]
        
    def helper(self, root, p ,q):
        if not root:
            return 0, None
        cntl, nodel = self.helper(root.left, p, q)
        cntr, noder = self.helper(root.right, p, q)
        if cntl == 2:
            return cntl, nodel
        elif cntr == 2:
            return cntr, noder
        elif cntl + cntr + (root == p or root == q) == 2:
            return 2, root
        elif root == p or root == q:
            return 1, root
        else:
            return cntl + cntr, None
