from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSize = 0


        #number of letters in alphabet
        freq = defaultdict(int)
        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            mostFreq = max(freq.values())
            totalLength = right - left + 1
            print(right)

            while totalLength - mostFreq > k:
                freq[s[left]] -=1
                left +=1

                mostFreq = max(freq.values())
                totalLength -= 1
            
            maxSize = max(right-left + 1, maxSize)

        return maxSize