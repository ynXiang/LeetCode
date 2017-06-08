# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else self.cal(root)[0]-1
        
    def cal(self, root):
        if root == None:
            return 0, 0
        else:
            lp, lm = self.cal(root.left)
            rp, rm = self.cal(root.right)
            return max(lp, rp, lm+1+rm), max(lm+1, rm+1)
