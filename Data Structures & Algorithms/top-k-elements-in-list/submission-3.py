class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        buckets = [[] for _ in range(len(nums) + 1)] 

        print(freq)
        for number in nums:
            freq[number] = freq.get(number, 0) + 1

        for key,value in freq.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            
            for item in buckets[i]:
                if k > 0:
                    res.append(item)
                    k -= 1
        
        return res
        

