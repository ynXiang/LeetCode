class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            ans = str(nums[0]) + "/(" + str(nums[1])
            for v in nums[2:]:
                ans += "/" + str(v)
            ans += ")"
            return ans
