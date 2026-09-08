class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        temp = []
        n = len(digits)

        digits_dict = {
            "2" : ["a","b","c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
         }

        def helper(i):
            if len(temp) == n:
                res.append("".join(temp))
                return 
            if i >= n:
                return
            #include
            cur_item = digits[i]
            for item in digits_dict[cur_item]:
                temp.append(item)
                helper(i+1)
                temp.pop()
        
        helper(0)
        return res