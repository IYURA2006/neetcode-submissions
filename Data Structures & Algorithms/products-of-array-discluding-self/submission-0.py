class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array1 = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                array1[i] = nums[i]
            else:
                product = array1[i-1] * nums[i]
                array1[i] = product


        array2 = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                array2[i] = nums[i]
            else:
                product = array2[i+1] * nums[i]
                array2[i] = product

        print(array1)
        print(array2)

        res = []


        for i in range(len(nums)):
            if i > 0:
                prefix = array1[i-1]
            else:
                prefix = 1
            
            if i < len(nums) - 1:
                postfix = array2[i+1]
            else:
                postfix = 1
            
            result = postfix * prefix
            res.append(result)

        return res

