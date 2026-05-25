from collections import defaultdict 


#dictionary (val) - index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_val = {}
        for index, value in enumerate(nums):
            differ = target - value
            if differ in seen_val:
                return [seen_val[differ], index]
            
            seen_val[value] = index
        
     
    
        