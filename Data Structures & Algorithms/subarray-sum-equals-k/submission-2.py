

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #number - freq
        pref_dictionary = {0:1}

        total = 0
        pref_number = 0

        for i in range(len(nums)):
            pref_number += nums[i]
            #if 
            if pref_number - k in pref_dictionary:
                total += pref_dictionary[pref_number - k]

    
            pref_dictionary[pref_number] = pref_dictionary.get(pref_number, 0) + 1

            
           
    
 
       
        return total

