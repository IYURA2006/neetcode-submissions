from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = 0
        left = 0
        
        unique_chars = set()

        for right in range(len(s)):
            character = s[right]
            while character in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(character)
            maxSubstring = max(maxSubstring, right - left + 1)
        
        return maxSubstring
                
