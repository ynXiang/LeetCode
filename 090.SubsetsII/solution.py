class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mapNums = {}
        for num in nums:
            mapNums[num] = mapNums.get(num, 0) + 1
        if not mapNums.items():
            return []
        res = [[]]
        for num, ocur in mapNums.items():
            preList = [[num] * i for i in range(1, ocur + 1)]
            res += [preset + subset for preset in preList for subset in res]
        return res
