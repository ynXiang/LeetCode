#https://discuss.leetcode.com/topic/81017/python-easy-understand-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None:
            minimum = abs(root.val - self.getMin(root.right))
            return minimum if root.right.left == None and root.right.right == None else min(minimum, self.getMinimumDifference(root.right))
        elif root.right == None:
            minimum = abs(root.val - self.getMax(root.left))
            return minimum if root.left.left == None and root.left.right == None else min(minimum, self.getMinimumDifference(root.left))
        else:
            minimum = min(abs(root.val - self.getMin(root.right)), abs(root.val - self.getMax(root.left)))
            if root.left.left != None or root.left.right != None:
                minimum = min(minimum, self.getMinimumDifference(root.left))
            if root.right.left != None or root.right.right != None:
                minimum = min(minimum, self.getMinimumDifference(root.right))
            return minimum
            
    def getMax(self, root):
        if root.right == None:
            return root.val
        else:
            return max(root.val, self.getMax(root.right))
    
    def getMin(self, root):
        if root.left == None:
            return root.val
        else:
            return min(root.val, self.getMin(root.left))
