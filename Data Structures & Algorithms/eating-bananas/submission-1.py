import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 4 3 2 

        #so max should be the max item in pile

        left = 1
        right = max(piles)

        leastSmallest = 0

        #currently we would go starting with left and check whether it is possible to eat it
        #

        while left <= right:
            cur_rate = (left + right) // 2

            required_hours = 0

            for pile in piles:
                required_hours += math.ceil(pile / cur_rate)
            
            if required_hours <= h:
                right = cur_rate - 1
            else:
                left = cur_rate + 1

        return left
