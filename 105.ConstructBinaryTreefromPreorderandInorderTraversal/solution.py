# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        indexRoot = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:indexRoot+1], inorder[:indexRoot])
        root.right = self.buildTree(preorder[indexRoot+1:], inorder[indexRoot+1:])
        return root
