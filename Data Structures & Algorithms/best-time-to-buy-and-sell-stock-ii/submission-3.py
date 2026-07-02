class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0
        
        minBuy = prices[0]
        profit = 0

        for i in range (1, len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            if prices[i] > minBuy:
                profit += prices[i] - minBuy
                minBuy = prices[i]
        
        return profit