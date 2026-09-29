class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        firstHouse = [0] * (n-1)
        lastHouse = [0] * (n)

        if n <= 3:
            return max(nums)

        firstHouse[0] = nums[0]
        firstHouse[1] = nums[1] 

        lastHouse[1] = nums[1]
        lastHouse[2] = nums[2]

        for i in range(2, n - 1):
            firstHouse[i] = max(firstHouse[i-2], firstHouse[i-3]) + nums[i]
        
        for i in range(3, n):
            lastHouse[i] = max(lastHouse[i-2], lastHouse[i-3]) + nums[i]

        print(firstHouse)
        print(lastHouse)
        return max(firstHouse[-1], lastHouse[-1], firstHouse[-2], lastHouse[-2])