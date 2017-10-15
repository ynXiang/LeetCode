class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = nums.count(0)
        index = -1
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            index = nums.index(0)
        mul = 1
        for v in nums:
            if v != 0:
                mul *= v
        for i in range(len(nums)):
            nums[i] = mul / nums[i] if index == -1 else 0
        if index >= 0:
            nums[index] = mul
        return nums
