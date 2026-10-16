import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        possible = []
        need_more = []

        for i in range(len(capital)):
            if w >= capital[i]:
                heapq.heappush(possible, -profits[i])
            else:
                heapq.heappush(need_more, (capital[i], profits[i]))

        if len(possible) == 0:
            return w

        
        cur_budget = w
        i = 0

        while i < k and len(possible) > 0:
            revenue = heapq.heappop(possible)
            
            cur_budget += -revenue

            while need_more and need_more[0][0] <= cur_budget:
                cap, profit = heapq.heappop(need_more)
                heapq.heappush(possible, -profit)
            i += 1
        

        return cur_budget
        #need to check the biggest profits and capital that matches
        #the current capital

        # need to check what is the highest profit u can make it in 
        #the range of availiable capital