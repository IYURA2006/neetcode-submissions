class Solution:
    def mySqrt(self, x: int) -> int:
        # 1 2 3 4 5 6 7 8 9
        # 3 * 3 = 9
        low = 1 
        up = x

        while low <= up:
            
            mid = (low + up) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                up = mid - 1
        
        return low - 1
