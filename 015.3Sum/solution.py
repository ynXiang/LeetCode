class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        i = 0
        while i < len(nums)-2:
            s, e = i+1, len(nums)-1
            while s < e:
                sum3 = nums[i] + nums[s] + nums[e]
                if sum3 > 0:
                    e -= 1
                elif sum3 < 0:
                    s += 1
                else:
                    res.append([nums[i], nums[s], nums[e]])
                    while s+1 < e and nums[s] == nums[s+1]:
                        s += 1
                    while s < e-1 and nums[e] == nums[e-1]:
                        e -= 1
                    s += 1
                    e -= 1
            while i < len(nums)-3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
