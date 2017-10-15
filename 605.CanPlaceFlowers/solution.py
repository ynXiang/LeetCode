class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed == [0] and n == 1:
                return True
            else:
                 return False
        if len(flowerbed) == 2:
            if flowerbed == [0, 0] and n == 1:
                return True
            else:
                return False
        if flowerbed[0:2] == [0, 0]:
            n -= 1
            flowerbed[0] = 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return True if flowerbed[-2:] == [0, 0] and n == 1 else False
