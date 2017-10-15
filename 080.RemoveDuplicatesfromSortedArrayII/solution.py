class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        double = False
        i, j = 1, 1
        last = nums[0]
        while j < len(nums):
            if last == nums[j]:
                if not double:
                    double = True
                    nums[i] = nums[j]
                    i += 1
            else:
                double = False
                last = nums[j]
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
