class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        minimum = prices[0]
        maximum = minimum
        profit = 0
        for i in prices:
            if i < minimum:
                minimum = i
                maximum = i
            if i > maximum:
                maximum = i
                if maximum - minimum > profit:
                    profit = maximum - minimum
        return profit
