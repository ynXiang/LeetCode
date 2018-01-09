# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        rootIndex = inorder.index(root.val)
        root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
        return root
