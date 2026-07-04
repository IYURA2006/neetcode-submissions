from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        
        #idea track last elem and remove it
        #track last index and try to remove by it
        #have a separate array to rebuil during pop again dont include the last elem

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        
        # while len(self.queue) > 1:
        #     elem = self.queue.popleft()
        #     self.temp.append(elem)
        # remove = self.queue[-1]
    
        # self.queue = self.temp
        # self.temp = deque()

        # return remove

        for i in range(len(self.queue) - 1):
            pushitem = self.queue.popleft()
            self.queue.append(pushitem)
        item = self.queue.popleft()
        return item


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