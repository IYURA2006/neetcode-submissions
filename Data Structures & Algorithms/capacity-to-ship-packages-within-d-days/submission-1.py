class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #whats the maximum
        # len(weights) * max / days

        low_boundary = max(weights)
        up_boundary = sum(weights)

        while low_boundary <= up_boundary:
            size = (low_boundary + up_boundary) // 2

            ships = 1
            free_space = size
            for weight in weights:
                if weight <= free_space:
                    free_space -= weight
                else:
                    ships += 1
                    free_space = size - weight
            
            if ships <= days:
                up_boundary = size - 1 
            else:
                low_boundary = size + 1
        
        return low_boundary
    
