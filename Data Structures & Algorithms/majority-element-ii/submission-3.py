from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #brute force
        #append it to dictionary counter 
        #go through dictionary and then check whether it more than 


        #if it is n/3 that means at most we can have two elements
        #so we can keep track of top 2 elements
        threshold = len(nums) // 3

        first_number = 0
        first_occurences = 0 
        second_number = 0
        second_occurences = 0
        

        #we check if first-occurences = 0
            #if not add it there and increase counter +1

        #we check if second-number = 0
        
        for item in nums:   


            if first_number == item:
                first_occurences += 1
            
            elif second_number == item:
                second_occurences += 1
            
            else:
                if first_occurences == 0:
                    first_number = item
                    first_occurences += 1
                

                elif second_occurences == 0:
                    second_number = item
                    second_occurences += 1
                    
                else:
                    first_occurences -= 1
                    second_occurences -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == first_number:
                cnt1 += 1
            elif num == second_number:
                cnt2 += 1

        res = []
        if cnt1 > threshold:
            res.append(first_number)
        if cnt2 > threshold:
            res.append(second_number)

        
        return res
            
