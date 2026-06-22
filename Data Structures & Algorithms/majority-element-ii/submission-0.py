from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #brute force
        #append it to dictionary counter 
        #go through dictionary and then check whether it more than 
        dictionary = Counter(nums)
        print(dictionary)
        threshold = len(nums) / 3
        res = []
        for item in dictionary:
            if dictionary[item] > threshold:
                res.append(item)
        
        return res
            
