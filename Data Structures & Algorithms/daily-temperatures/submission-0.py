class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #
        result = [0] * (len(temperatures))
        stack= []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and stack[-1][0] < temp:
                t, index = stack.pop()
                result[index] = (i-index)

            stack.append((temp, i))
        
        return result


