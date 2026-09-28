class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(3, n+1):
            next_val = t0 + t1 + t2

            t0 = t1
            t1 = t2
            t2 = next_val
        
        return t2


        # 0 1 1 2 4 6