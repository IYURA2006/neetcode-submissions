class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #1 2 3 5 
        #     4  - between 2 and 3
    
        low_b = 0
        up_b = len(nums) - 1

        while low_b <= up_b: 
            mid = (low_b + up_b) // 2

            if target == nums[mid]:
                return mid
            
            elif nums[mid] < target:
                low_b = mid + 1
            
            else:
                up_b = mid - 1
    

        return low_b
    
