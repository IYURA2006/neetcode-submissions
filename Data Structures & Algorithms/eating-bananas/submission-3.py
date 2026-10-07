import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        upper = max(piles)

        minimal = float("+inf")
        
        while upper >= low:
            rate =  ( low + upper ) // 2

            hours_required = 0
        
            for pile in piles:
                hours_required += math.ceil(pile / rate)

            if hours_required <= h:
                upper = rate - 1
                minimal = min(rate, minimal)

            else:
                low = rate + 1
    


        return minimal
