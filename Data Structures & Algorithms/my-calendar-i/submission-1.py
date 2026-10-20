class MyCalendar:
    
    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.intervals:
            if start <= startTime < end or start < endTime <= end:
                return False
            if startTime <= start < endTime  or startTime < end <= endTime:
                return False
        self.intervals.append([startTime, endTime])
        return True
        

      


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


#interval can be overlapping if start is beween two or end is betweeen two