class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        cur = []

        def helperfunc(start_index):
            if sum(cur) == target:
                res.append(cur.copy())
                return 
          
            if sum(cur) > target:
                return


            for x in range(start_index, len(nums)):
                cur.append(nums[x])
                helperfunc(x)
                cur.pop()
        #we pass started index to look forward only to avoid duplicates like 2,5 and 5,2
        
        helperfunc(0)

        return res


  # 2           5            6          9
# 2 5 6 9.      2 5 6 9.  2 5 6 9    2 5 6 9