import heapq
class MedianFinder:

    def __init__(self):
        self.first_part = [] #be reversed bigger first
        self.second_part = [] #smaller first

        
        
    def addNum(self, num: int) -> None:
        #equal
        heapq.heappush(self.first_part, -num)
        
        if len(self.first_part) > 1:
            largest_elem = heapq.heappop(self.first_part)
            heapq.heappush(self.second_part, -largest_elem)
        
        if len(self.second_part) > len(self.first_part):
            item = heapq.heappop(self.second_part)
            heapq.heappush(self.first_part, -item)
        
     

    def findMedian(self) -> float:

        if (len(self.second_part) + len(self.first_part)) % 2 == 0:
            n1 = self.first_part[0]
            n2 = self.second_part[0]
            return (-n1 + n2) / 2
        else:
            return -self.first_part[0]
    
  