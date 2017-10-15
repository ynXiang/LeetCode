class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        diff = 720
        timePoints.sort()
        for i in range(len(timePoints)):
            h1, m1 = map(lambda x:int(x), timePoints[i].split(":"))
            h2, m2 = map(lambda x:int(x), timePoints[(i+1)%len(timePoints)].split(":"))
            tmp = abs((h2-h1)*60+(m2-m1))
            if tmp > 720:
                tmp = 1440 - tmp
            if diff > tmp:
                diff = tmp
        return diff
