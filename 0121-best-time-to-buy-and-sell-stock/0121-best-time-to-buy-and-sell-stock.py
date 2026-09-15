class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        mini_price=float("inf")
        for i in range(0,len(prices)):
            mini_price=min(mini_price,prices[i])
            max_profit=max(max_profit,prices[i]-mini_price)

        return max_profit
        