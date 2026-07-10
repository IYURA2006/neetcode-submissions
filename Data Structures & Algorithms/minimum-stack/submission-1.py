class MinStack:

    def __init__(self):
        self.stack = []
        #first index val, cur_min

    def push(self, val: int) -> None:
        if len(self.stack) != 0:
            prev_val, min_val = self.stack[-1]
            min_val = min(val, min_val)
            self.stack.append((val, min_val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        val, x = self.stack[-1]
        return val

    def getMin(self) -> int:
        val,min_val = self.stack[-1]
        return min_val
        