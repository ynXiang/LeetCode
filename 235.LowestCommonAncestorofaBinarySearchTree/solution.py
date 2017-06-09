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
        ans, _ = self.findNode(root, p, q)
        return ans

    def findNode(self, root, p, q):
        if not root:
            return None, 0
        ln, lc = self.findNode(root.left, p, q)
        rn, rc = self.findNode(root.right, p, q)
        if ln:
            return ln, 0
        elif rn:
            return rn, 0
        elif root.val == p.val or root.val == q.val:
            if lc + rc == 1:
                return root, 0
            else:
                return None, 1
        elif lc + rc == 2:
            return root, 0
        else:
            return None, lc + rc
        
