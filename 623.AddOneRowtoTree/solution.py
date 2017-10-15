# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        elif d == 2:
            newNode1 = TreeNode(v)
            newNode2 = TreeNode(v)
            if root.left:
                newNode1.left = root.left
            if root.right:
                newNode2.right = root.right
            root.left = newNode1
            root.right = newNode2
            return root
        else:
            if root.left:
                root.left = self.addOneRow(root.left, v, d-1)
            if root.right:
                root.right = self.addOneRow(root.right, v, d-1)
            return root
