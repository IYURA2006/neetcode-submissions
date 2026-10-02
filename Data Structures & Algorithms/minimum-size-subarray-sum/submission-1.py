class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        curVal = 0
        
        minLength = float('inf')

        for right in range(len(nums)):
            curVal += nums[right]

            while curVal >= target:
                minLength = min(minLength, right-left + 1)
                curVal -= nums[left]
                left += 1
                
           
        if minLength == float("inf"):
            return 0
        return minLength
            