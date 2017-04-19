class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 < p2:
            minHeight = min(height[p1], height[p2])
            if area < (p2 - p1) * minHeight:
                area = (p2 - p1) * minHeight
            if minHeight == height[p1]:
                p1 += 1
            else:
                p2 -= 1
        return area
