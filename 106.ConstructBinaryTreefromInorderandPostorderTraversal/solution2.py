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
        nullNode = TreeNode(0)
        stack = [nullNode]
        inorderIndex = postorderIndex = len(inorder) - 1
        popNode = None
        conflict = False
        while postorderIndex >= 0:
            cur = TreeNode(postorder[postorderIndex])
            if conflict: popNode.left = cur
            else: stack[-1].right = cur
            stack.append(cur)
            conflict = False
            while len(stack) > 1 and stack[-1].val == inorder[inorderIndex]:
                popNode = stack.pop()
                inorderIndex -= 1
                conflict = True
            postorderIndex -= 1
        return nullNode.right
