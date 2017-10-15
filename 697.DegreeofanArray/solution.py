class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mapNums = {}
        for index, num in enumerate(nums):
            if num in mapNums:
                mapNums[num][0] += 1
                mapNums[num][2] = index
            else:
                mapNums[num] = [1, index, index]
        maxMap = sorted(mapNums.items(), key=lambda x:x[1][0], reverse=True)
        maximum = maxMap[0][1][0]
        minRes = len(nums)
        for i in maxMap:
            if i[1][0] == maximum:
                if minRes >  i[1][2] - i[1][1] + 1:
                    minRes = i[1][2] - i[1][1] + 1
            else:
                break        
        return minRes

