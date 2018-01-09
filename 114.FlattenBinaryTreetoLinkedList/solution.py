# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = [root]
        last = None
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                if last: last.right = cur
                last = cur
                last.left = None
        if last: last.right = None
