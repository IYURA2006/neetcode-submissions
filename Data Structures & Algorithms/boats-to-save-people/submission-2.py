class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)

        left = 0
        right = len(people) - 1


        # 1 2 2 3 

        # boat 1 = 3
        # 1 + 2
        boats = 0
       
        while right >= left:
            print(right, left)
            print(boats)
            if right == left:
                boats += 1
                right -= 1
                left += 1

            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats +=1 
            
            elif people[right] + people[left] >= limit:
                boats += 1
                right -= 1
        
        return boats
    