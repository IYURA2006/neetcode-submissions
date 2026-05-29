from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = []
        for i in range(len(nums) + 1):
            arr.append([])
        
        dictionary = Counter(nums)
        for val, freq in dictionary.items():
           arr[freq].append(val)

        res = []
        for item in reversed(arr):
            if item == []: pass
            for n in item:
                res.append(n)
                if len(res) == k:
                    return res
       
        
        