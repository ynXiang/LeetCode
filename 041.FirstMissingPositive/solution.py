class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == i + 1:
                i += 1
            elif 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]
                nums[tmp-1], nums[i] = tmp, nums[tmp-1]
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                while nums[j] == j + 1:
                    j -= 1
        while i < len(nums) and nums[i] == i + 1:
            i += 1
        return i + 1
