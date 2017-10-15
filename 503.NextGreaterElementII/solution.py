class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        elif len(nums) == 1:
            return [-1]
        wait = [(0,nums[0])]
        ans = [-1] * len(nums)
        index = 1
        fr = True
        while wait:
            if index == wait[-1][0]:
                break
            while wait and nums[index] > wait[-1][1]:
                ans[wait[-1][0]] = nums[index]
                wait.pop()
            if fr:
                wait.append((index, nums[index]))
            index += 1
            if index == len(nums):
                index = 0
                fr = False
        return ans
