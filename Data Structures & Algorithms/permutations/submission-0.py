class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        n = len(nums)

        used_items = set()

        def helper():
            if len(temp) == n:
                res.append(temp.copy())
                return 
            
            for num in nums:
                if num in used_items:
                    continue
                
                temp.append(num)
                used_items.add(num)

                helper()

                temp.pop()
                used_items.remove(num)

        helper()
        return res
            