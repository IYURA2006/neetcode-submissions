from collections import Counter

class Solution:

    def reorganizeString(self, s: str) -> str:
        queue = []
        character_freq = Counter(s)
        
        for character, freq in character_freq.items():
           queue.append((-freq, character)) 
        

        res = []
   
        # a a a x y 
        # a x y a a
        # a x a y a
        # if most frequent > n - frequent - 1
        prev = None
        prev_counter = 0
        while queue:
            freq, character = heapq.heappop(queue)

            if prev == character:
                return ""
            
            res.append(character)
            freq += 1

            if prev_counter != 0:
                heapq.heappush(queue, (prev_counter, prev))

            prev = character
            prev_counter = freq

        if len(s) != len(res):
            return ""
        return "".join(res)

