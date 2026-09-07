class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
        target = set()
        cur = []

        def helper(i):
            if i == length:
                elements = cur.copy()
                elements.sort()
                elements = tuple(elements)
                if elements not in target:
                    target.add(elements)

                return
            
            #include
            cur.append(nums[i])
            helper(i+1)

            cur.pop()

            #not include
            helper(i+1)

        helper(0)
        print(target)
        return list(target)