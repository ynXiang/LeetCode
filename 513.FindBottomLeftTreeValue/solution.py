# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findBottomLeftValueHelp(root)[0]
        
    def findBottomLeftValueHelp(self, root):
        if not root:
            return None, 0
        lv, ld = self.findBottomLeftValueHelp(root.left)
        rv, rd = self.findBottomLeftValueHelp(root.right)
        if lv == None and rv == None:
            v, d = root.val, 1
        elif lv == None:
            v, d = rv, rd+1
        elif rv == None:
            v, d = lv, ld+1
        else:
            v, d = (lv, ld+1) if ld >= rd else (rv, rd+1)
        return v, d
