# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, i, j):
        if i > j:
            return None
        maxIndex, maxVal = i, nums[i]
        for index, val in enumerate(nums[i+1:j+1]):
            if val > maxVal:
                maxVal = val
                maxIndex = index + i + 1
        root = TreeNode(maxVal)
        root.left = self.helper(nums, i, maxIndex-1)
        root.right = self.helper(nums, maxIndex+1, j)
        return root
