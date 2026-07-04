from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.temp = deque()
        
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            elem = self.queue.popleft()
            self.temp.append(elem)
        remove = self.queue[-1]
    
        self.queue = self.temp
        self.temp = deque()

        return remove

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()