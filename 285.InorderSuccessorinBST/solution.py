# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        while stack:
            node = stack.pop()
            if node.right:
                cur = node.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
            if node == p:
                return stack.pop() if stack else None
