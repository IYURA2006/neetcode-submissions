class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_substring = 0
        left = 0
        right = 0
        
        cur_window = set()
        while right < len(s):

            if s[right] not in cur_window:
                cur_window.add(s[right])
            else:
                while s[left] != s[right]:
                    cur_window.remove(s[left])
                    left += 1
                left += 1

            max_substring = max(max_substring, right - left + 1)

            right += 1
        
        return max_substring
