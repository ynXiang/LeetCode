class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i,v in enumerate(nums):
            if v not in d:
                d[v] = [i]
            else:
                d[v].append(i)
        for i in d.values():
            for j in range(len(i) - 1):
                if abs(i[j] - i[j+1]) <= k:
                    return True
        return False
