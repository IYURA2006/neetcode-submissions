class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[-1]

        left = 0
        curSum = 0
        for right in range(len(nums)):
            if curSum < 0:
                left = right
                curSum = 0
            
            curSum += nums[right]
            maxSum = max(curSum, maxSum)
        
        return maxSum
            #extending or starting a new one 

            

        