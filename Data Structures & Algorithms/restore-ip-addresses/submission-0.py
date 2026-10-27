class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 16:
            return []

        
        res = []
        sol = []
        def backtracking(dots_left, start_idx):
            if dots_left == 0:
                if start_idx == len(s):
                    res.append(".".join(sol[:]))
                return True

            print(dots_left)
            for j in range(1, 4):
                if start_idx + j > len(s):
                    break
                
                segment = s[start_idx : start_idx + j]

                if int(segment) > 255 or (segment[0] == "0" and len(segment) > 1):
                    continue
                
                sol.append(segment)
                backtracking(dots_left - 1, start_idx + j)
                sol.pop()

        backtracking(4, 0)
        return res

