class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        middle = nums[0]
        while len(nums) > 1 and nums[-1] == middle:
            del nums[-1]
        left = True if target < middle else False
        nums = nums * 2
        i, j = 0, len(nums)
        k = (i + j) // 2
        while i < j:
            if target < nums[k]:
                if left and nums[k] >= middle:
                    i = k + 1
                else:
                    j = k
            elif target > nums[k]:
                if not left and nums[k] < middle:
                    j = k
                else:
                    i = k + 1
            else:
                return True
            k = (i + j) // 2
        return False
