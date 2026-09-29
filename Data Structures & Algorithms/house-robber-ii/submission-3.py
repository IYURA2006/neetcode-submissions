class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)      

        if n <= 3:
            return max(nums)

        prevFirst = nums[0]
        curFirst = max(nums[0], nums[1]) 

        prevNext = nums[1]
        curNext = max(nums[1], nums[2])

        for i in range(2, n - 1):
            #check whether we pick this house  or not
            temp = max(prevFirst + nums[i],    curFirst) 
            prevFirst = curFirst
            curFirst = temp

        for i in range(3, n):
            temp = max(prevNext + nums[i], curNext) 
            prevNext = curNext
            curNext = temp

        return max(curFirst, curNext)