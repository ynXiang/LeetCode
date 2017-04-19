import copy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        origin_nums = copy.deepcopy(nums)
        nums.sort()
        a = 0
        b = len(nums) - 1
        while nums[a] + nums[b] != target and a < b:
            if nums[a] + nums[b] < target:
                a += 1
            else:
                b -= 1
        if nums[a] == nums[b]:
            first = origin_nums.index(nums[a])
            origin_nums.remove(nums[a])
            return [first, origin_nums.index(nums[b]) + 1]
        else:
            first = origin_nums.index(nums[a])
            second = origin_nums.index(nums[b])
            if first < second:
                return [first, second]
            else:
                return [second, first]
