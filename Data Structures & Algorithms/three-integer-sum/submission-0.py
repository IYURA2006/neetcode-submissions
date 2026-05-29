class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for middle in range(len(nums)):
            
            left = middle + 1
            right = len(nums) - 1

            while left < right:
                if(-nums[middle] == nums[left] + nums[right]):
                    res.append((nums[middle], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif(-nums[middle] > nums[left] + nums[right]):
                    left += 1
                else:
                    right -= 1

        result = set(res)
        return list(result)