class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mapNums = {}
        for num in nums:
            mapNums[num] = mapNums.get(num, 0) + 1
        return self.helper(mapNums)
    
    def helper(self, mapNums):
        if not mapNums:
            return [[]]
        permutations = []
        for num in mapNums.keys():
            mapNums[num] -= 1
            if mapNums[num] == 0:
                del mapNums[num]
            permutations += [[num] + reList for reList in self.helper(mapNums)]
            mapNums[num] = mapNums.get(num, 0) + 1
        return permutations
