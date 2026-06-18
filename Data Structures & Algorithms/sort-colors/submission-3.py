class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        #sort white
        left = 0
        right = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                temp = nums[left]
                nums[left] = 0
                nums[right] = temp
                left += 1
        
        for right in range(left, len(nums)):
            if nums[right] == 1:
                temp = nums[left]
                nums[left] = 1
                nums[right] = temp
                left += 1
        
       