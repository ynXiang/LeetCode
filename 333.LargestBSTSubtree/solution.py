# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
    
    # @return isBST, Num. of nodes, Min, Max
    def helper(self, root):
        if not root:
            return True, 0, float('inf'), -float('inf')
        isBSTL, nL, minL, maxL = self.helper(root.left)
        isBSTR, nR, minR, maxR = self.helper(root.right)
        isValid = isBSTL and isBSTR and maxL < root.val < minR
        return isValid, max(nL, nR, isValid and nL + nR + 1), min(minL, root.val), max(maxR, root.val)
