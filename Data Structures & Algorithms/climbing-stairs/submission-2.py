class Solution:
    def climbStairs(self, n: int) -> int:
        
        #bottom up 
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        waysToClimb = [0] * (n+1)
        waysToClimb[1] = 1
        waysToClimb[2] = 2

        for i in range(3, n+1):
            waysToClimb[i] = waysToClimb[i-1] + waysToClimb[i-2]
      
                # 3 = 1 + 2
        print(waysToClimb)
        return waysToClimb[n]

        # 4 -> number[i-1] + 1 + number[i-2] + 1; 
        #.   -> 