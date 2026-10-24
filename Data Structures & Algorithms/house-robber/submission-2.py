class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        houses = [0 for i in range(len(nums))]

        houses[0] = nums[0]
        houses[1] = max(nums[0], nums[1])

        for h in range(2, len(nums)):
            houses[h] = max(houses[h-2] + nums[h], houses[h-1])
        
        print(houses)
        return houses[-1]
  