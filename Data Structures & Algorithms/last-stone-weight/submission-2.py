import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
    
        while len(stones) > 1:
            w1 = heapq.heappop(stones)
            w2 = heapq.heappop(stones)
            # -3 and -5 => -2
            if w1 > w2:
                w2 = w2 - w1
                heapq.heappush(stones, w2)
            elif w2 > w1:
                w1 = w1 - w2
                heapq.heappush(stones, w1)
            print(stones)
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
            


            

