class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        def helper(a, b):
            counter = 0
            while a >= 0 and b <= len(s) - 1 and s[a] == s[b]:
                a -= 1
                b += 1
                counter += 1
            
            return counter

        for ch in range(len(s)):
            #odd
            odd_counter = helper(ch, ch)

            #even
            even_counter = helper(ch, ch+1)
            counter += odd_counter
            counter += even_counter
        return counter


