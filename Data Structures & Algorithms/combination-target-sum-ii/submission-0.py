class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        
        def helper(start_index):

            if sum(temp) == target:
                res.append(temp.copy())
                return 
            
            if sum(temp) > target:
                return
            
            for x in range(start_index, len(candidates)):
                #skip second number if we have in a row
                if x > start_index and candidates[x-1] == candidates[x]:
                    continue

                temp.append(candidates[x])
                helper(x+1)
                temp.pop()


        helper(0)
        print(res)
        return res



#     1               2,            3,              ... 4,5
# 2,    3,4,5       1,3,4,5.     1,2,4,5
# 3,4,5
#maybe pass array of used indexes and check if not add if yes skip