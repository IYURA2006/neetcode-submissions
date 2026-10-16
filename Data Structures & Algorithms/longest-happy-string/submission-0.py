import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        queue = []

        if a != 0: queue.append((-a, "a"))
        if b != 0: queue.append((-b, "b"))
        if c != 0: queue.append((-c, "c"))

        heapq.heapify(queue)
        res = []

        prev = None

        temp = None
        temp_counter = None

        while queue:
            quantity, ch = heapq.heappop(queue)
        
            quantity += 1
            res.append(ch)
            

            if temp != None:
                        heapq.heappush(queue, (temp_counter, temp))
                        temp = None
                        temp_counter = None

            if quantity != 0:

                if ch != prev:
                    print(ch, queue)
                    heapq.heappush(queue, (quantity, ch))
                    

                else:
                    temp = ch
                    temp_counter = quantity
          

            prev = ch

   
            
            
        
        return "".join(res)
