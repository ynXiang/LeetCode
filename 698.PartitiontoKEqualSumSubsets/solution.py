class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        avg = 1.0 * sum(nums) / k
        if avg != int(avg):
            return False
        i = 0
        sortNums = sorted(nums, reverse=True)
        remainings = [int(avg) for i in range(k)]
        if sortNums[0] > avg:
            return False
        return self.helper(k, avg, remainings, sortNums)
        
    def helper(self, k, avg, remainings, sortNums):
        if not sortNums:
            return True if len(filter(lambda x: x != 0, remainings)) == 0 else False
        for i in range(k):
            if remainings[i] < avg and remainings[i] >= sortNums[0] or remainings[i] == avg and (i == 0 or remainings[i-1] < avg):
                remainings[i] -= sortNums[0]
                if self.helper(k, avg, remainings, sortNums[1:]):
                    return True
                remainings[i] += sortNums[0]
        return False
