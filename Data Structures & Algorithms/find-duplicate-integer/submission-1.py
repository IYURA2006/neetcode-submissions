

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        for item in nums:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        newpointer = 0
        for item in nums:
            slow = nums[slow]
            newpointer = nums[newpointer]

            if newpointer == slow:
                break
        
        return newpointer
      
