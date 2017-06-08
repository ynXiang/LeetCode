# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not len(nums):
            return None
        half = int(len(nums)/2)
        node = TreeNode(nums[half])
        node.left = self.sortedArrayToBST(nums[:half])
        node.right = self.sortedArrayToBST(nums[half+1:])
        return node
