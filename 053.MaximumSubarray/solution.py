class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sumnums = [0]
        for v in nums:
            sumnums.append(sumnums[-1] + v)
        ans = nums[0]
        small = 0
        large = nums[0]
        for i,v in enumerate(sumnums[1:]):
            if v <= small:
                small, large = v, va
                if ans < sumnums[i+1] - sumnums[i]:
                    ans = sumnums[i+1] - sumnums[i]
            if v > large:
                large = v
                if ans < large - small:
                    ans = large - small
        return ans
