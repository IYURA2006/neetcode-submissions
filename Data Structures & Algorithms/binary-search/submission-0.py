class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_b = 0
        up_b = len(nums) - 1

        while low_b <= up_b:
            mid = (up_b + low_b) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                up_b = mid - 1
            else:
                low_b = mid + 1
        
        return -1
