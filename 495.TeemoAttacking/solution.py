class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        count = 0
        curEnd = -1
        for i in timeSeries:
            if i > curEnd:
                count += duration
            else:
                count += duration - curEnd + i - 1
            curEnd = i + duration - 1
        return count
