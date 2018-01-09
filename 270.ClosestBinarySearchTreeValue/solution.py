# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        minimum = float('inf')
        return int(self.helper(root, target, minimum) + target)
        
    def helper(self, root, target, minimum):
        if not root:
            return minimum
        mini = minimum if abs(minimum) < abs(root.val - target) else root.val - target
        if root.val == target:
            return 0
        elif root.val > target:
            return self.helper(root.left, target, mini)
        else:
            return self.helper(root.right, target, mini)
