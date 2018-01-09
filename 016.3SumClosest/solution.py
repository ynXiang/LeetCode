class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        m = float('inf')
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                delta = nums[i] + nums[j] + nums[k] - target
                if abs(delta) < m:
                    m = min(abs(delta), m)
                    res = delta + target
                if delta < 0:
                    j += 1
                elif delta > 0:
                    k -= 1
                else:
                    return target
        return res
