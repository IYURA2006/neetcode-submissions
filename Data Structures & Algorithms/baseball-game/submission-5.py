class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for item in operations:
            
            #check is it number
        
            #check is it D
            if item == "C":
                stack.pop()
            #check is it +
            elif item == "D":
                if len(stack) >= 1:
                    last = stack[-1]
                    last = last * 2
                    stack.append(last)
            #check is it C
            elif item == "+":
                sum_num = 0
                if len(stack) >= 1:
                    sum_num += int(stack[-1])
                if len(stack) > 1:
                    sum_num += int(stack[-2])
                stack.append(sum_num)
            else:
                stack.append(int(item))
        return sum(stack)