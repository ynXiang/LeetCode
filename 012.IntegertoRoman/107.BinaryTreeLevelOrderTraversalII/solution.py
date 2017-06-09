# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = self.levelOrderBottom(root.left)[::-1]
        r = self.levelOrderBottom(root.right)[::-1]
        reverse = False
        if len(l) > len(r):
            l, r = r, l
            reverse = True
        for i in range(len(l)):
            if reverse:
                r[i] += l[i]
            else:
                r[i] = l[i] + r[i]
        r = [[root.val]] + r
        return r[::-1]
