class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
        target = []
        cur = []
        nums.sort()

        def helper(i):
            target.append(cur.copy())
    
            for j in range(i, length):
                if j > i and (nums[j] == nums[j-1]):
                    continue
                cur.append(nums[j])
                helper(j+1)
                cur.pop()

        helper(0)
        return target