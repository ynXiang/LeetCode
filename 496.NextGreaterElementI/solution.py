#https://discuss.leetcode.com/topic/77959/meh-1000-is-small

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list()
        for num in findNums:
            add = False
            for num2 in nums[nums.index(num)+1:]:
                if num2 > num:
                    add = True
                    ans.append(num2)
                    break
            if not add:
                ans.append(-1)
        return ans
