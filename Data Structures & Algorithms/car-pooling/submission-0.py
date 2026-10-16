import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        getIn = []
        getOut = []

        for trip in trips:
            num_p, s, d = trip[0], trip[1], trip[2]
            getIn.append((s, num_p))
            getOut.append((d, num_p))
        
        heapq.heapify(getIn)
        heapq.heapify(getOut)

        peopleInCar = 0
        while getIn and getOut:
            start = getIn[0][0]
            end = getOut[0][0]

            print(start, end)
            if start < end:
                start_trip, num = heapq.heappop(getIn)
                peopleInCar += num
                if peopleInCar > capacity:
                    return False
         
            else:
                start_trip, num = heapq.heappop(getOut)
                peopleInCar -= num
            print(peopleInCar)
        
        return True
