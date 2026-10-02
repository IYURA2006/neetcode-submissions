class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        
        left = 0
        right = k - 1


        nums.reverse()
        
        while right > left:
            temp = nums[left]

            nums[left] = nums[right]
            nums[right] = temp

            right -= 1
            left += 1
        
        left = k
        right = len(nums) - 1

        while left < right:
            temp = nums[left]

            nums[left] = nums[right]
            nums[right] = temp

            right -= 1
            left += 1

    

        
        