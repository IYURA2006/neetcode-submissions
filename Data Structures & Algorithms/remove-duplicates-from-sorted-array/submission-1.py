class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 #begin of numbers
        right = 0 #end of repettion

        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
       
        return left + 1