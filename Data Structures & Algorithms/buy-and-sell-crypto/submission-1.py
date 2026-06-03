class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        maxProfit = 0

        if len(prices) < 2:
            return maxProfit

        left = 0
        right = 1

        while right <= len(prices) - 1:
            profit = prices[right] - prices[left]
             
            if(profit < 0):
                left = right
            
            right += 1
            maxProfit = max(profit, maxProfit)

     
        
        return maxProfit
