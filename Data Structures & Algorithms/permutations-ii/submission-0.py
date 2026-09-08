class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        length = len(nums)

        usedItems = [False] * length

        def backtracking():
            if len(temp) == length:
                
                res.append(temp.copy())

                return

            for i in range(length):
                if usedItems[i]:
                    continue
                #if it is used items prev same element false it means it was already tried, skip it
                if i > 0 and nums[i] == nums[i-1] and not usedItems[i-1]:
                    continue
                
                temp.append(nums[i])
                usedItems[i] = True

                backtracking()

                temp.pop()
                usedItems[i] = False

        backtracking()
        return res