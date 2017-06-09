# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.path(root)
        
    def path(self, root):
        if not root:
            return []
        lp = self.path(root.left)
        rp = self.path(root.right)
        if not lp and not rp:
            return [str(root.val)]
        ans = [str(root.val)+"->"+i for i in lp+rp]
        return ans
            
