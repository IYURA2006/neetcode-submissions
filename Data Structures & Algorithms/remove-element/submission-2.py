class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, k = 0,0
        while left<len(nums):
            if nums[left] != val:
                nums[k]=nums[left]
                k+=1
            left+=1
        return k