class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        if s[0] == "0":
            return ways

        dp = [0] * (len(s))
        dp[0] = 1

        for ch in range(1, len(s)):
            #single step
            if s[ch] != "0":
                dp[ch] += dp[ch-1]
            
            #check whether previous char and cur char in a limit
            double_digit = s[ch-1: ch+1]
            if 10 <= int(double_digit) <= 26:
                if ch == 1:
                    dp[ch] += 1
                else:
                    dp[ch] += dp[ch-2]
        
        return dp[-1]