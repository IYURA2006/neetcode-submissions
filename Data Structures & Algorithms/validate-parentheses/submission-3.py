class Solution:
    def isValid(self, s: str) -> bool:
        #we pop in to stack, opposite brackets
        stack = []
        for item in s:
            if item == "(":
                stack.append(")")
            if item == "{":
                stack.append("}")
            if item == "[":
                stack.append("]")
            
            if item == ")":
                if len(stack) > 0 and stack[-1] == ")":
                    stack.pop()
                else:
                    return False
            
            if item == "]":
                if len(stack) > 0 and stack[-1] == "]":
                    stack.pop()
                else:
                    return False
            
            if item == "}":
                if len(stack) > 0 and stack[-1] == "}":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:

            return True
        else:
            return False
        