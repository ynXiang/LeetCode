# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, level):
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
        nodes = [[root,0]]
        res = []
        while nodes:
            node, level = nodes.pop()
            if node:
                helper(node, level)
                nodes.append([node.right, level+1])
                nodes.append([node.left, level+1])
        return res
