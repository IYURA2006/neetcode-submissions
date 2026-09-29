class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minAmountSum = [1000] * (amount + 1)

        minAmountSum[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                        minAmountSum[i] = min(minAmountSum[i], 1 + minAmountSum[i-coin])

        if minAmountSum[-1] == 1000:
            return -1
        else:
            return minAmountSum[-1]
