class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        

        def helper(a, b):
            while a >= 0 and b <= len(s) - 1 and s[a] == s[b]:
                a -= 1
                b += 1

            return (a + 1, b - 1)

        
        res = ''

        for ch in range(len(s)):
            #even 
            x1, y1 = helper(ch, ch+1)
            #odd
            x2, y2 = helper(ch, ch)

            
            even_res = s[x1:y1+1]
            odd_res = s[x2:y2+1]
   
            if len(even_res) >= len(res):
                res = even_res
            
            if len(odd_res) >= len(res):
                res = odd_res
        
        return res

         


