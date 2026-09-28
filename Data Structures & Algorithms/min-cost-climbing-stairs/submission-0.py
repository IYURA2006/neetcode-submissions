class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minimum_cost = [0] * (n)
        minimum_cost[0] = cost[0]
        minimum_cost[1] = cost[1]
    
        for i in range(2, n):
            minimum_cost[i] = min(minimum_cost[i-1], minimum_cost[i-2]) + cost[i]
        
        print(minimum_cost)
        return min(minimum_cost[n-1], minimum_cost[n-2] )