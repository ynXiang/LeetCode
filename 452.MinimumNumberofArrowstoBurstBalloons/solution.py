class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        arrPos = -float('inf')
        cnt = 0
        for point in points:
            if point[0] > arrPos:
                arrPos = point[1]
                cnt += 1
        return cnt
