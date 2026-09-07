class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        
        def helper(i):
            if len(temp) == k:
                res.append(temp.copy())
                return
            if i > n:
                return
    
            #include
            temp.append(i)
            helper(i+1)
            temp.pop()

            helper(i+1)

        
        helper(1)
        return res