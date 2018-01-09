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
        nullNode = TreeNode(0)
        stack = [nullNode]
        preorderIndex = inorderIndex = 0
        popNode = None
        conflict = False
        while preorderIndex < len(preorder):
            cur = TreeNode(preorder[preorderIndex])
            if conflict: popNode.right = cur
            else: stack[-1].left = cur
            stack.append(cur)
            conflict = False
            while len(stack) > 1 and stack[-1].val == inorder[inorderIndex]:
                popNode = stack.pop()
                inorderIndex += 1
                conflict = True
            preorderIndex += 1
        return nullNode.left
