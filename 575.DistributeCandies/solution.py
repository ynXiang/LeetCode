class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique = set(candies)
        if len(unique) >= len(candies) / 2:
            return len(candies) / 2
        else:
            return len(unique)
