class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = []
        temp = []

        def helper(i):
            if i == n:
                final.append(temp.copy())
                return 
            
            #include
            temp.append(nums[i])
            helper(i+1)
            temp.pop()

            #not include
            helper(i+1)
        
        helper(0)
        return final