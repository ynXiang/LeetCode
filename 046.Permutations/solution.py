class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = [[nums[0]]]
        for v in nums[1:]:
            tmp = []
            for l in ans:
                for i in xrange(len(l)+1):
                    tmp.append(l[:i]+[v]+l[i:])
            ans = tmp
        return ans
