class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        #sort white
        left = 0
        right = len(nums) - 1
        pointer = 0

        while pointer <= right:
            if nums[pointer] == 0:
                temp = nums[left]
                nums[left] = nums[pointer]
                left += 1
                nums[pointer] = temp
                pointer +=1 

            elif nums[pointer] == 2:
                temp = nums[right]
                nums[right] = nums[pointer]
                right -= 1
                nums[pointer] = temp
            else: 
                pointer += 1
        
       