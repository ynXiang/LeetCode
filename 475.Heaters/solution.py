#https://discuss.leetcode.com/topic/71456/short-python

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        i, j, m = 0, 0, 0
        if houses[0] < heaters[0]:
            m = heaters[0] - houses[0]
            while i < len(houses) and houses[i] < heaters[0]:
                i += 1
        while i < len(houses) and j < len(heaters) - 1:
            if houses[i] >= heaters[j]:
                while j < len(heaters) - 1 and houses[i] >= heaters[j+1]:
                    j += 1
                if j < len(heaters) - 1 and m < min(houses[i]-heaters[j], heaters[j+1]-houses[i]):
                    m = min(houses[i]-heaters[j], heaters[j+1]-houses[i])
                i += 1
        if j == len(heaters) - 1:
            if m < houses[-1] - heaters[-1]:
                m = houses[-1] - heaters[-1]
        return m
