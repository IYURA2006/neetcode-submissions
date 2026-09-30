class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        
        curMax = 1
        curMin = 1
        curSum = 1

        for right in range(len(nums)):
            #start fresh
            opt1 = nums[right]

            #add it to curMaxSum
            opt2 = curMax * nums[right]

            #add it to CurMin if it is 2 neg
            opt3 = curMin * nums[right]

            curMax = max(opt1,opt2,opt3)   
            curMin = min(opt1, opt2, opt3)

            maxProduct = max(curMax, maxProduct)

        
        
        return maxProduct
